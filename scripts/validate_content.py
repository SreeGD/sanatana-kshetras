#!/usr/bin/env python3
import argparse
import json
import re
import subprocess
import sys
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path

import yaml
from jsonschema import Draft7Validator
from referencing import Registry, Resource

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_CONTENT = ROOT / "content"
CONTRACTS = ROOT / "specs" / "001-temples-directory" / "contracts"

FRONT_MATTER_RE = re.compile(r"\A---\n(.*?)\n---\n?(.*)\Z", re.DOTALL)

SCHEMA_FILES = {
    "temples": "temple.schema.json",
    "divya-desam": "divya-desam.schema.json",
    "beyond-earth": "realm.schema.json",
    "deities": "deity.schema.json",
}


def build_registry():
    resources = []
    for path in CONTRACTS.glob("*.schema.json"):
        contents = json.loads(path.read_text(encoding="utf-8"))
        resources.append((contents["$id"], Resource.from_contents(contents)))
    return Registry().with_resources(resources)


REGISTRY = build_registry()


def load_validator(schema_filename):
    schema = json.loads((CONTRACTS / schema_filename).read_text(encoding="utf-8"))
    return Draft7Validator(schema, registry=REGISTRY)


def parse_front_matter(text):
    match = FRONT_MATTER_RE.match(text)
    if not match:
        return None, "missing YAML front matter (file must start with '---')"
    try:
        data = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        return None, f"invalid YAML front matter ({exc})"
    return (data or {}), None


def load_entries(content_root):
    """Returns (errors, entries) where entries[kind] is a list of (path, front_matter)."""
    errors = []
    entries = {kind: [] for kind in SCHEMA_FILES}
    for kind, schema_filename in SCHEMA_FILES.items():
        validator = load_validator(schema_filename)
        base = content_root / kind
        if not base.exists():
            continue
        for path in sorted(base.rglob("*.md")):
            if path.name.startswith("_"):
                continue  # coordination/manifest file, not a content entry
            rel = path.relative_to(ROOT) if ROOT in path.parents else path
            front_matter, err = parse_front_matter(path.read_text(encoding="utf-8"))
            if err:
                errors.append(f"{rel}: {err}")
                continue
            for e in sorted(validator.iter_errors(front_matter), key=str):
                loc = "/".join(str(p) for p in e.path) or "<root>"
                errors.append(f"{rel}: {loc}: {e.message}")
            entries[kind].append((rel, front_matter))
    return errors, entries


def cmd_validate(content_root):
    errors, entries = load_entries(content_root)
    total = sum(len(v) for v in entries.values())
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} violation(s) found across {total} entries.")
        return 1
    print(
        f"{len(entries['temples'])} temples, "
        f"{len(entries['divya-desam'])} divya-desam entries, "
        f"{len(entries['beyond-earth'])} beyond-earth entries, "
        f"{len(entries['deities'])} deity categories — all valid."
    )
    return 0


def cmd_divya_desam_report(content_root):
    errors, entries = load_entries(content_root)
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} schema violation(s) found; fix before checking completeness.")
        return 1

    dd_entries = entries["divya-desam"]
    temple_ids = {fm.get("id") for _, fm in entries["temples"]}
    seqs = [fm.get("seq") for _, fm in dd_entries]

    problems = []
    if len(dd_entries) != 108:
        problems.append(f"Expected 108 Divya Desam entries, found {len(dd_entries)}.")

    seq_set = set(seqs)
    missing = sorted(set(range(1, 109)) - seq_set)
    dupes = sorted({s for s in seqs if seqs.count(s) > 1})
    if missing:
        problems.append(f"Missing seq numbers: {missing}")
    if dupes:
        problems.append(f"Duplicate seq numbers: {dupes}")

    for path, fm in dd_entries:
        if fm.get("physical") and fm.get("temple_ref") not in temple_ids:
            problems.append(f"{path}: temple_ref {fm.get('temple_ref')!r} does not resolve to a known temple.")

    if problems:
        for p in problems:
            print(p)
        return 1
    print(f"Divya Desam collection complete: {len(dd_entries)}/108, all temple_ref values resolved.")
    return 0


def cmd_coverage_report(content_root):
    errors, entries = load_entries(content_root)
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} schema violation(s) found; fix before running the coverage report.")
        return 1

    by_continent = defaultdict(int)
    by_country = defaultdict(int)
    for _, fm in entries["temples"]:
        by_continent[fm.get("continent", "unknown")] += 1
        country = fm.get("country", "unknown")
        if country.strip().lower() != "india":
            by_country[country] += 1

    print("Temples by continent:")
    for continent, count in sorted(by_continent.items()):
        print(f"  {continent}: {count}")
    print(f"\nCountries outside India ({len(by_country)}):")
    for country, count in sorted(by_country.items()):
        print(f"  {country}: {count}")
    return 0


def cmd_deity_report(content_root, export_path=None):
    errors, entries = load_entries(content_root)
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} schema violation(s) found; fix before running the deity report.")
        return 1

    categories = []
    for path, fm in entries["deities"]:
        pattern = re.compile(
            r"\b(" + "|".join(re.escape(kw) for kw in fm["match_keywords"]) + r")\b",
            re.IGNORECASE,
        )
        categories.append({"id": fm["id"], "name": fm["name"], "pattern": pattern, "temples": []})

    by_id = {c["id"]: c for c in categories}
    fallback_target = {"vaishnava": "vishnu-other", "shaiva": "shiva", "shakta": "devi-shakti"}

    matched_any = set()
    fallback_used = set()
    for path, fm in entries["temples"]:
        deity_text = " | ".join(fm.get("deities", []))
        hit = False
        for cat in categories:
            if cat["pattern"].search(deity_text):
                cat["temples"].append((path, fm.get("name", ""), fm.get("city", "")))
                hit = True
        if hit:
            matched_any.add(str(path))
            continue
        # Fallback tier: free-text deity epithets (esp. Divya Desam Tamil names) often carry
        # none of our keyword strings even though the temple's `traditions` field unambiguously
        # identifies it. If exactly one of vaishnava/shaiva/shakta applies, bucket it into that
        # tradition's general category rather than leaving it uncategorized.
        traditions = set(fm.get("traditions", []))
        relevant = traditions & set(fallback_target)
        if len(relevant) == 1:
            target_id = fallback_target[next(iter(relevant))]
            by_id[target_id]["temples"].append((path, fm.get("name", ""), fm.get("city", "")))
            matched_any.add(str(path))
            fallback_used.add(str(path))

    uncategorized = [
        (path, fm.get("name", ""), fm.get("deities", []))
        for path, fm in entries["temples"]
        if str(path) not in matched_any
    ]

    result = {
        "categories": [
            {
                "id": c["id"],
                "name": c["name"],
                "count": len(c["temples"]),
                "temples": [{"path": str(p), "name": n, "city": ci} for p, n, ci in c["temples"]],
            }
            for c in categories
        ],
        "uncategorized_count": len(uncategorized),
        "uncategorized": [{"path": str(p), "name": n, "deities": d} for p, n, d in uncategorized],
    }

    if export_path:
        Path(export_path).write_text(json.dumps(result, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"Wrote full deity index to {export_path}")

    total_temples = len(entries["temples"])
    print(f"Deity categories computed from {total_temples} temples (a temple may match more than one category):\n")
    for c in sorted(categories, key=lambda c: -len(c["temples"])):
        print(f"  {c['name']} ({c['id']}): {len(c['temples'])}")
    print(f"\nOf which matched via traditions-only fallback (no deity keyword matched; bucketed by their single vaishnava/shaiva/shakta tradition instead): {len(fallback_used)}")
    print(f"Uncategorized (matched no deity category, keyword or fallback): {len(uncategorized)} of {total_temples}")
    if uncategorized and not export_path:
        print("(pass --export-json to see the full uncategorized list and per-category temple listings)")
    return 0


def cmd_duplicates(content_root):
    errors, entries = load_entries(content_root)
    if errors:
        for e in errors:
            print(e)
        print(f"\n{len(errors)} schema violation(s) found; fix before checking duplicates.")
        return 1

    by_city = defaultdict(list)
    for path, fm in entries["temples"]:
        key = (fm.get("city", "").strip().lower(), fm.get("country", "").strip().lower())
        by_city[key].append((path, fm))

    found = False
    for (city, _country), group in by_city.items():
        if not city or len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                path_a, fm_a = group[i]
                path_b, fm_b = group[j]
                if fm_a.get("id") == fm_b.get("id"):
                    continue
                names_a = [fm_a.get("name", "")] + [n.get("value", "") for n in fm_a.get("alt_names", [])]
                names_b = [fm_b.get("name", "")] + [n.get("value", "") for n in fm_b.get("alt_names", [])]
                pairs = [(a, b) for a in names_a for b in names_b if a and b]
                if not pairs:
                    continue
                best = max(SequenceMatcher(None, a.lower(), b.lower()).ratio() for a, b in pairs)
                if best > 0.8:
                    found = True
                    print(f"Possible duplicate ({best:.2f}): {path_a} <-> {path_b}")
    if not found:
        print("No duplicate candidates found.")
    return 0


def cmd_check_locked(base_ref):
    diff = subprocess.run(
        ["git", "diff", "--name-only", base_ref, "--", "content/divya-desam"],
        cwd=ROOT, capture_output=True, text=True, check=True,
    )
    changed = [line for line in diff.stdout.splitlines() if line.strip()]
    if not changed:
        print("No changes under content/divya-desam/.")
        return 0

    problems = []
    for rel_path in changed:
        old = subprocess.run(
            ["git", "show", f"{base_ref}:{rel_path}"],
            cwd=ROOT, capture_output=True, text=True,
        )
        if old.returncode != 0:
            continue  # new file in this diff; nothing locked to compare against
        old_fm, old_err = parse_front_matter(old.stdout)
        if old_err:
            problems.append(f"{rel_path}: could not parse base version ({old_err})")
            continue

        new_path = ROOT / rel_path
        if not new_path.exists():
            problems.append(f"{rel_path}: deleted (locked entries must not be removed).")
            continue
        new_fm, new_err = parse_front_matter(new_path.read_text(encoding="utf-8"))
        if new_err:
            problems.append(f"{rel_path}: could not parse working version ({new_err})")
            continue

        for field in ("seq", "region_group", "physical"):
            if old_fm.get(field) != new_fm.get(field):
                problems.append(
                    f"{rel_path}: locked field '{field}' changed ({old_fm.get(field)!r} -> {new_fm.get(field)!r})."
                )

    if problems:
        for p in problems:
            print(p)
        return 1
    print("No locked-field changes detected.")
    return 0


def main():
    parser = argparse.ArgumentParser(description="Validate the temple directory content dataset.")
    parser.add_argument("--content-dir", help="Override content directory root (for fixture testing).")
    parser.add_argument("--divya-desam-report", action="store_true", help="Check 108 Divya Desam completeness.")
    parser.add_argument("--coverage-report", action="store_true", help="Report temple counts by continent/country.")
    parser.add_argument("--duplicates", action="store_true", help="Flag likely duplicate temple entries.")
    parser.add_argument("--deity-report", action="store_true", help="Compute temple groupings by deity-worship category.")
    parser.add_argument("--export-json", metavar="PATH", help="With --deity-report, write the full computed index to PATH as JSON.")
    parser.add_argument("--check-locked", metavar="BASE_REF", help="Check for locked-field changes vs. BASE_REF.")
    args = parser.parse_args()

    content_root = Path(args.content_dir) if args.content_dir else DEFAULT_CONTENT

    if args.check_locked:
        sys.exit(cmd_check_locked(args.check_locked))
    if args.divya_desam_report:
        sys.exit(cmd_divya_desam_report(content_root))
    if args.coverage_report:
        sys.exit(cmd_coverage_report(content_root))
    if args.duplicates:
        sys.exit(cmd_duplicates(content_root))
    if args.deity_report:
        sys.exit(cmd_deity_report(content_root, args.export_json))
    sys.exit(cmd_validate(content_root))


if __name__ == "__main__":
    main()
