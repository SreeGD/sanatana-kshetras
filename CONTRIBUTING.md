# Contributing to Sanatana Kshetras

This repository holds the Sanatana Kshetras temple directory as structured content files (see `specs/001-temples-directory/` for the full spec, data model, and schemas). Content lives under `content/` as one Markdown file per temple, Divya Desam entry, Beyond-Earth (cosmology) entry, or deity worship-category.

## Workflow

1. Add or edit a file under `content/temples/`, `content/divya-desam/`, or `content/beyond-earth/`, following the field definitions in `specs/001-temples-directory/data-model.md` and the schemas in `specs/001-temples-directory/contracts/`.
2. Run `python3 scripts/validate_content.py` locally and fix any reported violations.
3. Open a pull request. Opening the PR *is* the "submission" — until it's merged, your changes are pending review and are not part of the published, verified directory (this substitutes for a bespoke pending/approved status field during the data phase).
4. A reviewer checks the PR against the checklist in `.github/PULL_REQUEST_TEMPLATE.md`, including:
   - Every new or edited entry cites at least one source (a named scripture/text, or an explicit "oral tradition" note).
   - `python3 scripts/validate_content.py` passes.
   - `python3 scripts/validate_content.py --duplicates` doesn't flag the new entry against an existing one for the same city under a different name.
5. On approval, the PR is merged and the content becomes part of the published dataset.

## The 108 Divya Desam collection is locked

Files under `content/divya-desam/` carry `locked: true`. Their `seq`, `region_group`, and `physical` fields are editorially fixed and must not change through a routine contribution. Before merging any PR that touches `content/divya-desam/`, run:

```bash
python3 scripts/validate_content.py --check-locked <base-ref>
```

This fails if any locked field changed relative to `<base-ref>` (e.g., `main`), catching accidental or unreviewed changes to the canonical list.

## Duplicate entries

Before adding a new temple, run:

```bash
python3 scripts/validate_content.py --duplicates
```

This flags any two entries in the same city with near-identical names, so the same physical temple doesn't end up listed twice under different spellings.
