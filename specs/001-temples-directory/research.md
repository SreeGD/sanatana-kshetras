# Phase 0 Research: Global Sanatana Temple Directory (Data Phase)

**Scope of this research**: Only the data-authoring phase (per user direction: "data first, then site"). Website/application technology choices are explicitly deferred to a follow-up plan once the dataset exists — see "Deferred decisions" at the end.

## Decision: Content format — per-entry Markdown files with YAML front matter

**Decision**: Each temple, Divya Desam entry, and Beyond-Earth realm is one Markdown file: structured fields (deity, location, tradition, citations, etc.) in a YAML front-matter block, with long-form narrative (history/legend) as the Markdown body.

**Rationale**:
- Matches FR-005–FR-023's mix of structured fields (for filtering/search) and long narrative text (history, legend, podcast research content) — no single flat format (CSV/JSON) handles both well.
- Git-friendly: one file per temple means clean diffs, easy per-entry review/approval (maps directly to FR-013's pending-review workflow via PRs), and no merge conflicts between unrelated temples.
- Format-agnostic for the future: virtually every static-site generator and web framework (Astro, Hugo, Next.js content collections, 11ty, etc.) can ingest Markdown+front-matter directly, so today's data phase isn't thrown away when the site is built.
- Human-editable by non-technical contributors (monks, devotees) with minimal syntax, unlike raw JSON.

**Alternatives considered**:
- Single JSON/YAML file for all temples: rejected — becomes an unreviewable, merge-conflict-prone monolith at hundreds/thousands of entries; poor fit for long narrative text.
- CSV/spreadsheet: rejected — cannot cleanly hold multi-paragraph history/legend text, multi-value fields (multiple deities, multiple tradition tags, multiple citations), or nested structures (festival lists).
- A real database (SQLite/Postgres) from day one: rejected for the data-authoring phase — adds tooling overhead before there's an application to serve it; files-in-git is the simpler starting point and can be imported into a DB later without data loss.

## Decision: Directory layout and identity scheme

**Decision**:
```
content/
├── temples/<continent>/<country>/<state-or-region-or-na>/<slug>.md
├── divya-desam/<seq-3-digit>-<slug>.md
└── beyond-earth/<slug>.md
```
- `<continent>` ∈ {asia, europe, africa, north-america, south-america, oceania} (the six inhabited continents; matches SC-010).
- `<slug>` is a lowercase kebab-case ASCII identifier derived from the primary name plus, when needed, a disambiguating city (e.g., `sri-venkateswara-swamy-temple-tirupati`).
- Each Divya Desam file's front matter carries a `temple_ref` pointing to the corresponding file under `content/temples/...` when physical, or omits it and sets `physical: false` for the two celestial entries.

**Rationale**: Mirrors FR-001/FR-002's continent > country organization directly in the filesystem, making "browse by continent/country" a free consequence of directory structure rather than something that must be computed. Keeps the fixed 108-entry Divya Desam collection physically separate from the open-ended general directory, matching FR-003/FR-014's "editorially locked" requirement — nothing outside `content/divya-desam/` can accidentally shadow it.

**Alternatives considered**: A single flat `content/temples/` directory with country as a front-matter field only — rejected because it makes continent/country coverage (SC-003, SC-010) harder to audit at a glance and loses free deduplication-by-path benefits.

## Decision: Schema validation tooling

**Decision**: A single dependency-light Python script (`scripts/validate_content.py`, stdlib + PyYAML only) that walks `content/`, parses front matter, and checks each entry against the JSON Schemas in `contracts/`. Run via `python3 scripts/validate_content.py` with no other setup.

**Rationale**: Operationalizes FR-020 (citation required), FR-022 (no visit-fields on Beyond-Earth entries), and the enum constraints (tradition, worship_status, continent) as an automated, repeatable gate — addressing the "verify for accuracy" and "ground in tradition" directive structurally (a missing citation or an invalid enum value fails validation) rather than relying on manual review alone. Python + PyYAML is the lowest-friction choice: no build step, runs anywhere, and is a safe default that doesn't lock in the eventual site's stack.

**Alternatives considered**: A Node.js/JSON-Schema-based validator — rejected only because it would require choosing/pinning a JS toolchain before the site's own stack is decided; Python's stdlib + one small dependency avoids that lock-in while doing the same job.

## Decision: Source-citation convention

**Decision**: Every entry's front matter includes a `sources` list; each item has `type` (`scripture` | `oral_tradition` | `historical_record`) and, when `type: scripture`, a `text` name (e.g., "Divya Prabandham", "Srimad Bhagavatam", "Skanda Purana") plus an optional `reference` (chapter/verse/canto). Cosmology entries with more than one tradition's account use a `tradition_accounts` list, each tagged with its own `tradition` and `sources`, rather than one merged narrative.

**Rationale**: Directly implements FR-020 and FR-021 as a checkable data shape: validation can mechanically reject an entry with zero `sources` entries, and reject a cosmology entry that states a claim outside a `tradition_accounts` block without attribution.

**Alternatives considered**: Freeform citation text in the Markdown body only — rejected because it can't be validated mechanically, so "100% of entries cite a named source" (SC-008) would be unverifiable without manual audit of every file.

## Decision: Underscore-prefixed files are non-content coordination artifacts

**Decision**: Any file under `content/**` whose name starts with `_` (e.g., `content/divya-desam/_manifest-<region-group>.md`) is skipped by `scripts/validate_content.py` and is not a real entry.

**Rationale**: Parallel content-authoring work (e.g., multiple contributors/agents each covering one Divya Desam region group) needs a place to hand off a list of authored temples for centralized sequence-number assignment without colliding with another contributor's numbering, and without that handoff file being mistaken for — or validated as — a real Temple/Divya-Desam/Realm entry. A leading underscore is a widely recognized "not real content" convention and needed no new schema or directory.

**Alternatives considered**: Requiring every contributor to self-assign `seq` — rejected, since two contributors working in parallel on different region groups have no way to avoid colliding sequence numbers without a coordination step; a per-region draft file outside `content/` entirely — rejected only for convenience, since keeping the manifest next to the entries it describes makes the handoff easier to find and clean up.

## Decision: The 108 Divya Desam identity/region/coordinate/Alvar data is generated from the `108divyadesam` project's dataset, not from independent web research

**Decision**: All 106 physical Divya Desam entries' `id`, `name`, `place`/`city`, `region_group`, `seq`, `coordinates`, and `associated_saints` are generated programmatically from `/Users/sree/Projects/108divyadesam/data/dataset/{temples,regions,alwars,alwar_temple_map}.json` — a dataset extracted from a published Tamil temple-guide Android app (`com.coderays.divyadesam`) covering all 108 temples, 12 Alvars, and 204 Alvar↔temple mangalasasanam links. The generator script lives at the project root's `scripts/` only in spirit — the one-off generation was run from the scratchpad and its output is the committed content; the script itself is not part of this repo since it depends on a sibling project's data files.

**Rationale**: Six parallel web-research passes (one per region group) initially populated this collection, but cross-checking against this authoritative dataset surfaced real errors: two agents conflated the distinct "Nadu Nadu" (a separate 2-temple group) and "Thondai Nadu" (22 temples) groups into one; several temples were misattributed to the wrong physical site because many Divya Desams share near-identical names (e.g., three unrelated temples all called "Bhaktavatsala Perumal Temple"; four different places ending in "...Vinnagaram"); and a couple of true duplicate entries were written by two agents independently. Rebuilding identity/region/coordinate/Alvar data from one authoritative, structurally-verified source eliminates this whole class of error, which free-text web research is prone to given how many Divya Desams share deity epithets and place-name patterns.

**Consequence — narrative depth was traded for identity accuracy**: the source dataset explicitly does not include Sthala Puranam (origin legend) prose, festival calendars, or darshan timings (a documented gap in its own README). Rather than risk re-introducing misattribution by trying to automatically re-merge the web-researched narrative prose from the six original agents (which would require re-solving the same name-collision matching problem), every regenerated entry currently carries only a short, honestly-scoped history paragraph grounded in verified facts (place, deity, Alvar attribution, region), a generic-but-labeled darshan-hours/best-time-to-visit placeholder, and a `review_flags` entry stating the fuller legend is pending. This is a deliberate accuracy-over-richness tradeoff, reversible by enriching individual entries later (a natural task for `/speckit-implement` or manual follow-up), now that every entry's *identity* is on solid ground.

**Alternatives considered**: Manually auditing and correcting all ~105 web-researched files in place — rejected as this session's chosen path initially, but abandoned after estimating the manual verification cost across the many name-collision clusters exceeded the cost of a clean regeneration from authoritative data.

**Provenance/licensing note**: The `108divyadesam` project's own README flags that "images and any server-sourced prose are the original publisher's — confirm redistribution rights before publishing." This project draws only from `data/dataset/{temples,regions,alwars,alwar_temple_map}.json` (structured factual data — names, coordinates, region groupings, Alvar attributions — extracted from the app, not the publisher's prose) and `data/cache/{temple-history,temple-extras}.json` (independently AI-generated narrative text, marked `review: "auto"` in its own source, explicitly *not* the publisher's server-sourced prose per the README). No images and no publisher-authored prose were used. Still, confirm this reasoning before any public launch, since it wasn't independently legally reviewed here.

## Deferred decisions (explicitly out of scope for this plan)

- Website/application framework, hosting, and runtime (Story-4-era decision) — to be made in a follow-up `/speckit-plan` once enough of the dataset exists to know real query/filter/scale needs.
- Search indexing/full-text search technology — deferred with the above.
- Community contribution *tooling* (FR-012/013 workflow UI) — for the data phase, "contribution" is a pull request against this repository, reviewed per FR-013/FR-023; a dedicated submission UI is deferred to the website plan.
- Image hosting/storage for FR-016 — deferred; front matter reserves an `images` field (list of paths/URLs) so it's ready when storage is chosen.
