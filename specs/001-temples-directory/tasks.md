---

description: "Task list for feature implementation"
---

# Tasks: Global Sanatana Temple Directory (Data Phase)

**Input**: Design documents from `/specs/001-temples-directory/`

**Prerequisites**: plan.md, spec.md, research.md, data-model.md, contracts/, quickstart.md (all present)

**Tests**: Not explicitly requested in the spec beyond the schema-validation gate itself; "tests" for this phase are the `scripts/validate_content.py` checks run against authored content, not a separate unit-test suite.

**Organization**: Tasks are grouped by user story (from spec.md) to enable independent authoring and validation of each story's content.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: Which user story this task belongs to (US1–US6, matching spec.md)

## Path Conventions

Single content/data repository (see plan.md § Project Structure):
- `content/temples/<continent>/<country>/<region-or-na>/<slug>.md`
- `content/divya-desam/<seq-3-digit>-<slug>.md`
- `content/beyond-earth/<slug>.md`
- `scripts/validate_content.py`

## Phase 1: Setup (Shared Infrastructure)

- [x] T001 Create the content repository skeleton: `content/temples/`, `content/divya-desam/`, `content/beyond-earth/`, and `scripts/` directories at repo root (each with a `.gitkeep` if empty)
- [x] T002 [P] Add `requirements.txt` at repo root pinning `pyyaml` and `jsonschema` (per plan.md Technical Context)
- [x] T003 [P] Add `CONTRIBUTING.md` at repo root describing the pending→review→approved workflow as a GitHub PR (per research.md's deferred-decisions note substituting PR state for a bespoke status field) and stating the rule that `content/divya-desam/**`'s `locked: true` fields (`seq`, `region_group`, `physical`) cannot change via unreviewed submission (FR-014)

---

## Phase 2: Foundational (Blocking Prerequisites)

**⚠️ CRITICAL**: No user story content-authoring can begin until this phase is complete — every story's content is validated by this tooling.

- [x] T004 Implement `scripts/validate_content.py`: walk `content/`, parse each Markdown file's YAML front matter, and validate `content/temples/**` against `specs/001-temples-directory/contracts/temple.schema.json`, `content/divya-desam/**` against `divya-desam.schema.json`, and `content/beyond-earth/**` against `realm.schema.json` (resolving their shared `common.schema.json` refs); print a per-file list of violations and exit non-zero on any failure (quickstart.md "Validate the dataset")
- [x] T005 [P] Add a `--divya-desam-report` flag to `scripts/validate_content.py`: assert exactly 108 files exist under `content/divya-desam/`, that their `seq` values form the exact integer set {1..108} with no gaps or duplicates (data-model.md invariant; SC-002), and that every entry with `physical: true` has a `temple_ref` resolving to an existing file under `content/temples/`
- [x] T006 [P] Add a `--coverage-report` flag to `scripts/validate_content.py`: print a table of temple counts grouped by `continent` and by `country` (excluding India) to track SC-003 ("≥15 countries outside India") and SC-010 ("all 6 inhabited continents represented")
- [x] T007 [P] Add duplicate-candidate detection to `scripts/validate_content.py`: flag any two Temple entries whose `city` values match and whose `name`/`alt_names` values are near-identical (simple normalized string comparison), printing them as warnings per FR-015
- [x] T008 Create fixture files under `scripts/fixtures/`: one minimal valid Temple entry, one minimal valid physical Divya-Desam entry, one minimal valid celestial Divya-Desam entry, and one minimal valid Realm entry; confirm `python3 scripts/validate_content.py` (pointed at the fixtures dir) reports all four as valid before authoring real content

**Checkpoint**: Foundation ready — schema validation and reporting work end-to-end on fixture data.

---

## Phase 3: User Story 1 - Plan a pilgrimage visit (Priority: P1) 🎯 MVP

**Goal**: A general, growing catalog of Indian temples with complete visit-planning fields.

**Independent Test**: `python3 scripts/validate_content.py` passes on the authored entries, and each file's front matter includes non-empty `worship_status`, `best_time_to_visit`, `how_to_reach`, `sources` (≥1), and `darshan_hours` (required per temple.schema.json unless `worship_status: heritage`).

### Implementation for User Story 1

- [ ] T009 [P] [US1] Author 10+ major South Indian temple entries (Tamil Nadu, Kerala, Karnataka, Andhra Pradesh, Telangana) under `content/temples/asia/india/<state>/<slug>.md`, each satisfying temple.schema.json's required fields: `id, name, deities (≥1), traditions (≥1), continent, country, region (required because country="India"), city, worship_status, best_time_to_visit, how_to_reach, sources (≥1), documented_vs_legend, status`
- [ ] T010 [P] [US1] Author 10+ major North/East/West Indian temple entries (Uttar Pradesh, Odisha, Gujarat, Rajasthan, West Bengal, Uttarakhand) under `content/temples/asia/india/<state>/<slug>.md`, same required-field set as T009
- [ ] T011 [US1] Run `python3 scripts/validate_content.py` and fix any violations in T009/T010 entries until exit code is 0 (depends on T009, T010)
- [ ] T012 [US1] Run `python3 scripts/validate_content.py --coverage-report` and save the per-state India counts as a baseline snapshot in `specs/001-temples-directory/coverage-log.md` (depends on T011)

**Checkpoint**: US1 independently functional — a schema-valid, growing Indian temple catalog with full visit-planning fields.

---

## Phase 4: User Story 2 - Follow the 108 Divya Desam pilgrimage circuit (Priority: P1)

**Goal**: The complete, locked 108-entry Divya Desam collection.

**Independent Test**: `python3 scripts/validate_content.py --divya-desam-report` reports 108/108 present, no `seq` gaps/duplicates, and 0 unresolved `temple_ref` values.

**Status**: Complete (108/108), but via a different path than originally planned — see `research.md` § "The 108 Divya Desam identity/region/coordinate/Alvar data is generated from the `108divyadesam` project's dataset". Six parallel web-research passes surfaced real name-collision misattributions and a region-group error (Nadu Nadu vs. Thondai Nadu conflated), so identity/region/coordinates/Alvar-attribution were regenerated from an authoritative dataset instead. **Trade-off**: each entry's `history` is currently a short, accurate, fact-grounded stub rather than a full researched legend — see US3/T020-T023 below, which are NOT yet satisfied by this data and remain open follow-up work.

### Implementation for User Story 2

- [x] T013 [P] [US2] Author Divya Desam entries for the Chola Nadu region group under `content/divya-desam/0XX-<slug>.md` with matching Temple files under `content/temples/asia/india/tamil-nadu/<slug>.md`, cross-linking both directions (`divya_desam_ref` on the Temple, `temple_ref` on the Divya-Desam entry); set `region_group: chola-nadu`, `physical: true`, `country: india`, `locked: true` per divya-desam.schema.json
- [x] T014 [P] [US2] Author Divya Desam entries for the Pandya Nadu region group, same cross-linking/required-field rules as T013 but `region_group: pandya-nadu`
- [x] T015 [P] [US2] Author Divya Desam entries for the Malai Nadu (Kerala) region group, `region_group: malai-nadu`
- [x] T016 [P] [US2] Author Divya Desam entries for the Nadu Nadu (Thondai Nadu) region group, `region_group: nadu-nadu`
- [x] T017 [P] [US2] Author Divya Desam entries for the Vada Nadu (North India + Nepal) region group, `region_group: vada-nadu`; set `country: nepal` for the Salagramam/Muktinath entry (FR-004b) and `country: india` for the rest
- [x] T018 [US2] Author the 2 celestial Divya Desam entries (Thiruparkadal, Paramapadam/Vaikuntam) under `content/divya-desam/`: `physical: false`, `region_group: celestial`, a `celestial_note` explaining their non-physical nature, and no `temple_ref`/`country` (divya-desam.schema.json forbids these when `physical: false`); assign final `seq` numbers after T013–T017 (depends on T013, T014, T015, T016, T017)
- [x] T019 [US2] Run `python3 scripts/validate_content.py --divya-desam-report` and fix entries until it reports exactly 108/108 with no `seq` gaps/duplicates and 0 unresolved `temple_ref` (depends on T018)

**Checkpoint**: US1 and US2 both independently functional.

---

## Phase 5: User Story 3 - Research a temple for a podcast episode (Priority: P2)

**Goal**: Existing temple entries carry sourced history/legend content sufficient for podcast preparation.

**Independent Test**: For the Divya Desam entries, each linked Temple file has a non-empty `history` body, `sources` with a named `text` when `type: scripture`, and `associated_saints` populated where applicable (FR-008).

### Implementation for User Story 3

- [ ] T020 [P] [US3] Enrich the Chola Nadu and Pandya Nadu Divya Desam temple entries (from T013–T014) with full `history` narrative bodies, `associated_saints` (Alvars) where applicable, and `sources` citing specific texts (e.g., Divya Prabandham hymns, relevant Puranas) per FR-008
- [ ] T021 [P] [US3] Enrich the Malai Nadu, Nadu Nadu, and Vada Nadu Divya Desam temple entries (from T015–T017) with the same history/saints/sources depth as T020
- [ ] T022 [US3] Set each enriched entry's `documented_vs_legend` field (`documented` | `legend` | `mixed`, per FR-017) based on whether its `history` content is attested history or oral tradition (depends on T020, T021)
- [ ] T023 [US3] Run `python3 scripts/validate_content.py` to confirm all enriched entries still pass schema validation, i.e., still carry ≥1 `sources` item (FR-020) (depends on T022)

**Checkpoint**: US1, US2, US3 all independently functional.

---

## Phase 6: User Story 4 - Find a temple outside India (Priority: P2)

**Goal**: Diaspora and heritage Sanatana temples outside India, spanning all six inhabited continents.

**Independent Test**: `python3 scripts/validate_content.py --coverage-report` shows temples in ≥15 non-India countries across all 6 continents; every non-India entry has `worship_status` set.

### Implementation for User Story 4

- [ ] T024 [P] [US4] Author actively-worshipped diaspora temple entries for ≥8 countries (e.g., USA, UK, Canada, Malaysia, Singapore, Mauritius, Trinidad and Tobago, South Africa) under `content/temples/<continent>/<country>/na/<slug>.md`, setting `worship_status: active` and omitting `region` (only required when `country="India"` per temple.schema.json)
- [ ] T025 [P] [US4] Author heritage/monument temple entries for ≥4 countries (e.g., Cambodia — Angkor Wat, Indonesia — Prambanan, Vietnam — My Son) under the same path convention, setting `worship_status: heritage`, omitting `darshan_hours` (not required when `worship_status: heritage`), and using `how_to_reach` for visitor/tourism access info instead of darshan logistics
- [ ] T026 [US4] Run `python3 scripts/validate_content.py --coverage-report` and author additional entries under any missing continent's `content/temples/<continent>/` until ≥15 non-India countries and all 6 continents are represented (SC-003, SC-010) (depends on T024, T025)

**Checkpoint**: US1–US4 all independently functional.

---

## Phase 7: User Story 5 - Explore the traditional cosmology beyond Earth (Priority: P2)

**Goal**: The "Beyond Earth" section of lokas and spiritual-world abodes, each scripturally sourced.

**Independent Test**: `python3 scripts/validate_content.py` confirms every `content/beyond-earth/*.md` file has ≥1 `tradition_accounts` entry with sources, and none carry `address`/`coordinates`/`darshan_hours`/`how_to_reach` (rejected by realm.schema.json).

### Implementation for User Story 5

- [ ] T027 [P] [US5] Author Realm entries for the material-cosmos lokas (`category: loka`) — the traditional fourteen-loka system — under `content/beyond-earth/<slug>.md`, each with ≥1 `tradition_accounts` item citing a named Purana/Upanishad per realm.schema.json
- [ ] T028 [P] [US5] Author Realm entries for the spiritual-world abodes (`category: spiritual-world`) — Vaikuntha, Goloka Vrindavana, Kailasa, Devi Loka/Manidvipa — under `content/beyond-earth/<slug>.md`
- [ ] T029 [US5] For any abode where traditions disagree (e.g., the "supreme eternal abode" differs across Vaishnava/Shaiva/Shakta accounts), add one `tradition_accounts` entry per tradition to the same file rather than merging into a single narrative, per FR-021 (depends on T027, T028)
- [ ] T030 [US5] Run `python3 scripts/validate_content.py` and confirm zero Beyond-Earth entries are rejected for a forbidden visit field (FR-022) and all cite ≥1 source (FR-020) (depends on T029)

**Checkpoint**: US1–US5 all independently functional.

---

## Phase 8: User Story 6 - Contribute or correct a temple listing (Priority: P3)

**Goal**: A working, enforced contribution workflow.

**Independent Test**: A sample PR adding/editing a Temple file is reviewable against `CONTRIBUTING.md`'s checklist; the schema gate blocks an invalid submission; a submission touching a `locked: true` Divya Desam field is caught by `--check-locked`.

### Implementation for User Story 6

- [ ] T031 [P] [US6] Add a GitHub PR template at `.github/PULL_REQUEST_TEMPLATE.md` requiring: which entity file(s) changed, source citations for new claims, and confirmation that `python3 scripts/validate_content.py` passes locally
- [ ] T032 [US6] Add a `--check-locked <base-ref>` flag to `scripts/validate_content.py`: diff changed `content/divya-desam/*.md` files against `base-ref` and fail if `seq`, `region_group`, or `physical` changed, per FR-014
- [ ] T033 [US6] Document the review workflow (pending → approved, duplicate handling) in `CONTRIBUTING.md`, referencing `scripts/validate_content.py`'s duplicate-candidate warnings from T007 per FR-015 (depends on T032)

**Checkpoint**: All user stories independently functional.

---

## Phase 9: Polish & Cross-Cutting Concerns

- [ ] T034 [P] Run `python3 scripts/validate_content.py` (full run, no flags) and fix any remaining violations across all entries authored in Phases 3–7
- [ ] T035 [P] Update `specs/001-temples-directory/quickstart.md` if any command/flag names changed from what T005/T006/T032 actually implemented
- [ ] T036 Walk through `quickstart.md` end-to-end (add one of each entity type, run all three validator flags) and confirm the documented steps match actual script behavior (depends on T034, T035)

---

## Dependencies & Execution Order

### Phase Dependencies

- **Setup (Phase 1)**: No dependencies — start immediately.
- **Foundational (Phase 2)**: Depends on Setup — BLOCKS all user stories.
- **User Stories (Phase 3–8)**: All depend on Foundational completion.
  - US1 and US2 (both P1) have no dependency on each other and can run in parallel.
  - US3 depends on US2's Divya Desam temple files existing (it enriches them) — run after US2.
  - US4 and US5 depend only on Foundational and can run in parallel with US1–US3.
  - US6 depends only on Foundational (it builds tooling/docs, not content) and can run any time after Phase 2.
- **Polish (Phase 9)**: Depends on all desired user stories being complete.

### Parallel Opportunities

- T002, T003 in parallel.
- T005, T006, T007 in parallel (different flags/functions in the same file — coordinate if working in parallel, or serialize within one contributor).
- T009, T010 in parallel (different files).
- T013–T017 in parallel (different region groups, different files).
- T020, T021 in parallel (different files).
- T024, T025 in parallel (different files).
- T027, T028 in parallel (different files).
- Once Foundational (Phase 2) completes: US1, US2, US4, US5, US6 can all start in parallel; US3 waits on US2.

---

## Parallel Example: Phase 4 (User Story 2)

```bash
Task: "Author Chola Nadu Divya Desam entries in content/divya-desam/ + content/temples/asia/india/tamil-nadu/"
Task: "Author Pandya Nadu Divya Desam entries in content/divya-desam/ + content/temples/asia/india/tamil-nadu/"
Task: "Author Malai Nadu Divya Desam entries in content/divya-desam/ + content/temples/asia/india/kerala/"
Task: "Author Nadu Nadu Divya Desam entries in content/divya-desam/ + content/temples/asia/india/tamil-nadu/"
Task: "Author Vada Nadu Divya Desam entries in content/divya-desam/ + content/temples/asia/india/<state>/ and content/temples/asia/nepal/"
```

---

## Implementation Strategy

### MVP First

Both US1 and US2 are P1. Recommended MVP order, since US2 is the fixed, explicitly-named deliverable ("Use 108 Divyadesam") and demonstrates the full pipeline (schema + cross-linking + celestial handling) end-to-end fastest:

1. Complete Phase 1: Setup
2. Complete Phase 2: Foundational (blocks everything)
3. Complete Phase 4: User Story 2 (108 Divya Desam) — a complete, closed, high-value deliverable
4. Complete Phase 3: User Story 1 (general catalog) in parallel or immediately after
5. **STOP and VALIDATE**: `--divya-desam-report` shows 108/108; `--coverage-report` shows growing India coverage

### Incremental Delivery

1. Setup + Foundational → tooling ready
2. US2 (108 Divya Desam) → validate → this alone is a complete, shareable artifact
3. US1 (general catalog) → validate → directory now useful beyond the fixed list
4. US3 (podcast depth) → validate → entries now support content creation
5. US4 (global) → validate → directory now spans continents
6. US5 (Beyond Earth) → validate → full cosmological scope from spec.md delivered
7. US6 (contribution workflow) → validate → directory can grow via community PRs
8. Polish

---

## Notes

- [P] tasks touch different files with no dependencies.
- [Story] labels map every content-authoring task to its spec.md user story for traceability.
- Every content-authoring task must leave `python3 scripts/validate_content.py` passing before being considered done — schema conformance is this phase's test suite.
- Commit after each task or logical group (e.g., one region group's worth of Divya Desam entries).
- Avoid: hand-editing `locked: true` fields on existing Divya Desam entries outside the T013–T018 authoring step; creating a Temple file without at least one `sources` entry; adding physical-visit fields to a Beyond-Earth entry.
