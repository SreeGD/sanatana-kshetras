# Implementation Plan: Global Sanatana Temple Directory (Data Phase)

**Branch**: `001-temples-directory` | **Date**: 2026-09-23 | **Spec**: [spec.md](./spec.md)

**Input**: Feature specification from `/specs/001-temples-directory/spec.md`

**Note**: Per explicit user direction, this plan covers the **data-authoring phase only**: producing the sourced, verified, tradition-grounded temple/cosmology dataset itself. The website/application that will eventually browse this data (Stories 1, 2, 4 in the spec) is deferred to a follow-up `/speckit-plan` once the dataset exists — see `research.md` § Deferred decisions.

## Summary

Build a git-based content repository of Markdown+YAML entries — one per temple, one per Divya Desam, one per Beyond-Earth realm — organized by continent/country (and India's states) plus a separate fixed 108-entry Divya Desam collection and a Beyond-Earth cosmology section. Every entry is schema-validated (JSON Schemas in `contracts/`) to mechanically enforce sourcing (FR-020), the celestial/physical distinction (FR-004, FR-022), and multi-tradition attribution (FR-021), operationalizing the "verify for accuracy" and "ground in tradition" directive as an automated gate rather than relying on review alone.

## Technical Context

**Language/Version**: Python 3.9+ (validation tooling only; content itself is Markdown/YAML, not code)

**Primary Dependencies**: PyYAML, `jsonschema` (both stdlib-adjacent, no build step)

**Storage**: Flat files in git (`content/**/*.md`); no database in this phase (see `research.md`)

**Testing**: `scripts/validate_content.py` run against the full `content/` tree; treated as the test suite for this phase (schema conformance = correctness here, not unit tests of business logic)

**Target Platform**: N/A — a version-controlled text content repository, readable/editable on any platform

**Project Type**: Content/data repository (single project; no frontend/backend split in this phase)

**Performance Goals**: N/A for this phase (no runtime service); validation script should complete in well under a minute at the target scale below

**Constraints**: Every entry must pass schema validation before merge (FR-020/FR-022/FR-021 as automated gates); the 108 Divya Desam collection is structurally locked (`locked: true`, enforced by schema + directory separation) per FR-014

**Scale/Scope**: Exactly 108 Divya Desam entries (SC-002); temples spanning ≥15 countries outside India and all 6 inhabited continents (SC-003, SC-010); Beyond-Earth section covering the traditional fourteen-loka system plus major spiritual-world abodes (Vaikuntha, Goloka, Kailasa, Manidvipa) per tradition

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

`.specify/memory/constitution.md` is still the unfilled bootstrap template — no project-specific principles have been ratified yet, so there are no constitutional gates to evaluate against for this feature. This is not a violation to justify (Complexity Tracking is not applicable), but it is a gap: recommend running `/speckit-constitution` to ratify at least the principles this plan already assumes de facto (schema-validated content, no unreviewed edits to the 108 Divya Desam, sourcing required for every claim) so future features are held to the same bar explicitly rather than by convention. Re-checked after Phase 1: unchanged — no constitution to gate against.

## Project Structure

### Documentation (this feature)

```text
specs/001-temples-directory/
├── plan.md              # This file (/speckit-plan command output)
├── research.md          # Phase 0 output (/speckit-plan command)
├── data-model.md        # Phase 1 output (/speckit-plan command)
├── quickstart.md        # Phase 1 output (/speckit-plan command)
├── contracts/           # Phase 1 output (/speckit-plan command)
│   ├── common.schema.json
│   ├── temple.schema.json
│   ├── divya-desam.schema.json
│   └── realm.schema.json
└── tasks.md             # Phase 2 output (/speckit-tasks command - NOT created by /speckit-plan)
```

### Source Code (repository root)

```text
content/
├── temples/
│   └── <continent>/<country>/<region-or-na>/<slug>.md
├── divya-desam/
│   └── <seq-3-digit>-<slug>.md      # exactly 108 files
└── beyond-earth/
    └── <slug>.md

scripts/
└── validate_content.py   # schema validation + coverage/completeness reports
```

**Structure Decision**: Single content/data repository (no frontend/backend split — there is no application yet in this phase). Content lives under `content/`, organized by entity type and, for temples, by continent/country as decided in `research.md` § Directory layout. `scripts/validate_content.py` is the only executable code this phase produces, implementing the JSON Schema contracts in `contracts/`.

## Complexity Tracking

*Not applicable — no constitution is ratified yet (see Constitution Check above), so there are no gates to violate, and this plan introduces a single, minimal validation script rather than additional projects/patterns requiring justification.*
