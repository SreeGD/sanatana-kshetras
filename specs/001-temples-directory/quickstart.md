# Quickstart: Global Sanatana Temple Directory (Data Phase)

Validates that the content dataset described in `plan.md`/`data-model.md` works end-to-end: an entry can be added, it's placed correctly, and it passes the accuracy/sourcing gates from the spec.

## Prerequisites

- Python 3.9+
- `pip install pyyaml jsonschema`

## Add a temple entry

1. Create the file at `content/temples/<continent>/<country>/<region-or-na>/<slug>.md`, e.g.:
   `content/temples/asia/india/tamil-nadu/sri-ranganathaswamy-temple-srirangam.md`
2. Fill YAML front matter per `contracts/temple.schema.json` (see `data-model.md` § Temple for field meanings). At minimum: `id`, `name`, `deities`, `traditions`, `continent`, `country`, `region` (if India), `city`, `worship_status`, `best_time_to_visit`, `how_to_reach`, `sources` (≥1), `documented_vs_legend`, `status: pending`.
3. Write the history/legend narrative as the Markdown body below the front matter.

## Add a Divya Desam entry

1. Create `content/divya-desam/<seq-3-digit>-<slug>.md`, e.g. `content/divya-desam/001-srirangam.md`.
2. Set `physical: true`, `temple_ref` pointing to the matching file under `content/temples/...`, and `country: india` (or `nepal`), plus `region_group`. For the 2 celestial entries, set `physical: false` and write `celestial_note` instead of a `temple_ref`.

## Add a Beyond-Earth (loka / spiritual-world) entry

1. Create `content/beyond-earth/<slug>.md`, e.g. `content/beyond-earth/vaikuntha.md`.
2. Set `category` (`loka` or `spiritual-world`) and at least one entry in `tradition_accounts`, each with its own `sources`. Do not add `address`, `coordinates`, `darshan_hours`, or `how_to_reach` — the schema rejects them.

## Validate the dataset

```bash
python3 scripts/validate_content.py
```

**Expected outcome**:
- Exit code 0 and a summary line (e.g., `142 temples, 108/108 Divya Desam, 16 beyond-earth entries — all valid`) when everything passes.
- A non-zero exit and a per-file list of schema violations (missing `sources`, wrong enum value, Beyond-Earth entry with a forbidden visit field, etc.) otherwise — this is the automated form of "verify for accuracy" (FR-020) and "ground in tradition."

## Check Divya Desam completeness (SC-002)

```bash
python3 scripts/validate_content.py --divya-desam-report
```

Expected: reports exactly 108 entries with `seq` covering 1–108 with no gaps or duplicates, and 0 physical entries missing a `temple_ref`.

## Check global/continent coverage (SC-003, SC-010)

```bash
python3 scripts/validate_content.py --coverage-report
```

Expected: a table of temple count per continent and per country outside India, to track progress toward "≥15 countries outside India" and "all six inhabited continents represented."
