# Phase 1 Data Model: Global Sanatana Temple Directory

Concrete field-level shape of the entities defined in `spec.md`. Each entity below is authored as YAML front matter on a Markdown file (see `research.md` for the format decision and `contracts/` for the enforceable JSON Schemas).

## Temple

Represents a single place of worship or heritage site (spec: **Temple**).

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string (slug) | yes | Stable identifier; matches filename. |
| `name` | string | yes | Primary name, English. |
| `alt_names` | list<{ script/language, value }> | no | Alternate names/transliterations (FR-005). Resolves the "same temple, many names" edge case via a canonical `id` plus this list. |
| `deities` | list<string> (Deity id) | yes, ≥1 | Supports multi-shrine sites (FR-018). |
| `traditions` | list<enum: vaishnava, shaiva, shakta, smarta, folk/regional, other> | yes, ≥1 | Multi-value (FR-018). |
| `continent` | enum: asia, europe, africa, north-america, south-america, oceania | yes | FR-001/002/010. |
| `country` | string (ISO country name) | yes | FR-001/002/010. |
| `region` | string | no | State/union territory/province; required when `country == India` (FR-001). |
| `city` | string | yes | |
| `coordinates` | {lat, lng} | no | Best-effort per Assumptions. |
| `address` | string | no | Descriptive location when coordinates unavailable. |
| `worship_status` | enum: active, heritage, partially_active | yes | FR-007. |
| `darshan_hours` | string | required if `worship_status != heritage` | FR-006; omitted/N-A note for heritage sites. |
| `best_time_to_visit` | string | yes | FR-006. |
| `festivals` | list<{name, approx_date}> | no | FR-006. |
| `how_to_reach` | string | yes | FR-006. |
| `access_notes` | string | no | Dress code / restricted access (edge case). |
| `history` | markdown body | yes | Origin/legend narrative (FR-008). |
| `associated_saints` | list<string> | no | E.g., Alvars/Nayanars (FR-008). |
| `sources` | list<SourceCitation> | yes, ≥1 | FR-020. |
| `documented_vs_legend` | enum: documented, legend, mixed | yes | FR-017. |
| `images` | list<string (path/URL)> | no | FR-016; absence must render as "no image," never broken. |
| `divya_desam_ref` | string (Divya Desam id) | no | Set when this temple is also one of the 108. |
| `status` | enum: verified, pending | yes | FR-013. |
| `duplicate_of` | string (Temple id) | no | Set by reviewers when FR-015 flags a duplicate; entry is retired in favor of the canonical one. |
| `review_flags` | list<string>, ≥1 if present | no | Notes on specific facts the author could not fully verify (e.g., conflicting sources on a date or a claim found only in one secondary source) — signals which parts of an otherwise `status: pending` entry need the most scrutiny before verification. |

## Divya Desam Entry

Fixed collection of 108 (spec: **Divya Desam Entry**).

| Field | Type | Required | Notes |
|---|---|---|---|
| `seq` | integer 1–108 | yes | Canonical sequence number; unique. |
| `id` | string (slug) | yes | |
| `name` | string | yes | |
| `region_group` | enum: chola-nadu, nadu-nadu, thondai-nadu, malai-nadu, pandya-nadu, vada-nadu, celestial | yes | FR-003. Seven traditional groups, not six: Nadu Nadu (a distinct 2-temple "central region" group) and Thondai Nadu (22 temples, the Kanchipuram/Chennai cluster) are separate groups, not synonyms. |
| `physical` | boolean | yes | `false` only for the 2 celestial entries. |
| `temple_ref` | string (Temple id) | required if `physical == true` | Links to the full Temple record. |
| `country` | enum: india, nepal | required if `physical == true` | FR-004(a)/(b). |
| `celestial_note` | markdown | required if `physical == false` | Explains the non-physical nature (FR-004(c)); no location/visiting fields permitted. |
| `locked` | boolean | yes, always `true` | Enforces FR-014: `seq`, `region_group`, and `physical` cannot change via unreviewed contribution. |
| `sources` | list<SourceCitation> | required if `physical == false` | A physical entry's sourcing lives on its linked Temple record; a celestial entry has no Temple to inherit from, so it MUST carry its own `sources` directly to satisfy FR-020. |
| `review_flags` | list<string>, ≥1 if present | no | Same purpose as Temple.review_flags — e.g., uncertainty about which region group a temple traditionally belongs to. |

Validation invariant: exactly 108 entries, `seq` values are the set {1..108} with no gaps/dupes (SC-002).

## Realm (Loka) — "Beyond Earth"

Non-earthly plane or abode (spec: **Realm (Loka)**).

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string (slug) | yes | |
| `name` | string | yes | E.g., "Vaikuntha", "Goloka Vrindavana", "Kailasa", "Manidvipa", one of the fourteen lokas. |
| `category` | enum: loka (material-cosmos plane), spiritual-world (beyond material creation) | yes | FR-019. |
| `governing_deity` | string (Deity id) | no | |
| `tradition_accounts` | list<{tradition, description (markdown), sources: list<SourceCitation>}> | yes, ≥1 | Required whenever more than one tradition describes this realm differently (FR-021); a single-tradition realm has exactly one entry in this list. |
| `position_in_cosmology` | string | no | E.g., "5th of the seven upper lokas". |

Validation invariant: **no** `address`, `coordinates`, `darshan_hours`, or `how_to_reach` fields permitted on this entity (FR-022) — enforced by JSON Schema `additionalProperties: false`.

## Deity

| Field | Type | Required | Notes |
|---|---|---|---|
| `id` | string (slug) | yes | |
| `name` | string | yes | |
| `traditions` | list<enum, see Temple.traditions> | yes | |
| `iconography_notes` | string | no | |

## Tradition/Sect

Enumerated, not a separate content file: `vaishnava | shaiva | shakta | smarta | folk_regional | other` — used as a controlled vocabulary by Temple, Deity, and Realm.

## Region

Not a content file; derived from `continent` + `country` (+ `region` for India) fields present on Temple entries. Used for filesystem layout (`research.md`) and for browse/filter (FR-010).

## Source Citation (shared shape)

| Field | Type | Required | Notes |
|---|---|---|---|
| `type` | enum: scripture, oral_tradition, historical_record | yes | FR-020. |
| `text` | string | required if `type == scripture` | E.g., "Divya Prabandham", "Skanda Purana", "Brahma Samhita". |
| `reference` | string | no | Chapter/verse/canto. |
| `note` | string | required if `type == oral_tradition` | Brief description of the tradition/lineage it comes from. |

## Contribution/Submission

Represented as a pull request against this repository during the data phase (see `research.md` deferred decisions), not a separate content file. Its "fields" are: proposed file diff, submitter (PR author), and review status (open/approved-merged/rejected-closed) — GitHub's own PR state substitutes for a bespoke status field per FR-013.

## Curated Collection

Not a content file; a computed grouping (Featured, Trending, New, 108 Divya Desam = all files under `content/divya-desam/`, Beyond Earth = all files under `content/beyond-earth/`) for FR-011.

## Relationships

```
Temple 1───0..1 Divya Desam Entry   (via divya_desam_ref / temple_ref, mutually consistent)
Temple *───* Deity                  (via deities)
Temple *───* Tradition              (via traditions, enum)
Realm  *───* Deity                  (via governing_deity, optional)
Realm  1───* Tradition Account      (embedded list, ≥1)
```
