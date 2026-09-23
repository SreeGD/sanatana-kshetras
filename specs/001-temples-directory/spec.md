# Feature Specification: Global Sanatana Temple Directory

**Feature Branch**: `001-temples-directory`

**Created**: 2026-09-23

**Status**: Draft

**Input**: User description: "Create a full list of hindu,sanatana temples, india, across globe follow the format https://templesofindia.org/. Use 108 Divadesam. Make it as comprehensive list as possible. The goal for people to visit, monks to do a podcast"

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Plan a pilgrimage visit (Priority: P1)

A devotee wants to visit a Hindu/Sanatana temple, either in their home region or while traveling, and needs enough information to plan the trip: where it is, when it's open, what deity is enshrined, and what makes it significant.

**Why this priority**: This is the core value proposition ("the goal for people to visit"). Without reliable, complete visit-planning information, the directory has no purpose.

**Independent Test**: Can be fully tested by searching for a specific temple (by name, city, or state/country) and confirming the result page contains location, deity, tradition, visiting hours, best time to visit, and how to reach it — enough to plan a visit without another source.

**Acceptance Scenarios**:

1. **Given** a devotee knows a temple's name or city, **When** they search the directory, **Then** they see a result with the temple's exact location, presiding deity, and visiting information.
2. **Given** a devotee wants to plan a trip to a region, **When** they browse by country and state/region, **Then** they see all listed temples in that area with enough summary detail to choose which to visit.
3. **Given** a devotee is comparing two temples in the same city, **When** they view both detail pages, **Then** each page independently shows complete darshan hours, festival dates, and directions.

---

### User Story 2 - Follow the 108 Divya Desam pilgrimage circuit (Priority: P1)

A devotee or Vaishnava pilgrim wants to see the complete, traditional list of the 108 Divya Desams (temples glorified by the Alvars), understand which region each belongs to, and track which ones are physically visitable versus celestial/non-physical.

**Why this priority**: Explicitly named by the requester as a required, canonical dataset. It's a well-defined, closed list (unlike the open-ended general directory), so it can be delivered completely and serves as a flagship, high-trust collection that anchors the site's credibility.

**Independent Test**: Can be fully tested by opening the "108 Divya Desam" collection and confirming all 108 entries are present, each tagged with its traditional region (e.g., Chola Nadu, Pandya Nadu, Malai Nadu, Vada Nadu), and that the 2 celestial entries (Thiruparkadal and Paramapadam/Vaikuntam) are clearly marked as non-physical rather than showing broken travel information.

**Acceptance Scenarios**:

1. **Given** a user opens the Divya Desam collection, **When** the list loads, **Then** all 108 entries are present and none are placeholders.
2. **Given** a Divya Desam temple is a real, physical location, **When** the user views it, **Then** it shows full location and visiting details like any other temple, plus its Divya Desam region grouping.
3. **Given** a Divya Desam entry is celestial (no earthly location), **When** the user views it, **Then** the page explains its non-physical nature instead of showing empty/broken address or visiting-hours fields.
4. **Given** a Divya Desam temple lies outside India (e.g., Salagramam/Muktinath in Nepal), **When** the user views the collection filtered to "outside India," **Then** it appears correctly under its country.

---

### User Story 3 - Research a temple for a podcast episode (Priority: P2)

A monk, teacher, or content creator preparing an episode about a specific temple wants its history, associated legends, scriptural references (Puranas, Divya Prabandham, Thevaram, etc.), associated saints, and architectural/cultural significance in one place, with clear indication of source/tradition, so the content can be spoken about accurately and with proper attribution.

**Why this priority**: Explicitly named as a goal ("monks to do a podcast"). It's P2 rather than P1 because it depends on the same core temple record used by Story 1 — it primarily requires additional depth fields, not a new browsing capability.

**Independent Test**: Can be fully tested by opening any Featured or Divya Desam temple's detail page and confirming it contains a history/legend narrative, at least one cited scriptural or textual source, and any associated saints — sufficient to script a short episode without leaving the page.

**Acceptance Scenarios**:

1. **Given** a content creator opens a temple's detail page, **When** they scroll to the history section, **Then** they find a narrative account of the temple's origin/legend with its source tradition or text named.
2. **Given** a temple is associated with a specific saint or sage (e.g., an Alvar or Nayanar), **When** viewing the temple page, **Then** the saint's name and their connection to the temple are shown.
3. **Given** two temples share a legend or deity story, **When** each is viewed independently, **Then** each page states the connection rather than requiring cross-referencing external sources.

---

### User Story 4 - Find a temple outside India (Priority: P2)

A member of the global Hindu diaspora, or a traveler abroad, wants to find Sanatana temples outside India — whether an actively-worshipped community temple (e.g., in the US, UK, Malaysia, Mauritius, Trinidad) or a historic heritage site (e.g., Angkor Wat, Prambanan) — and understand whether it's a living place of worship or primarily a heritage/monument site.

**Why this priority**: Explicitly named ("across globe"). P2 because it extends the same core browsing/detail experience from Story 1 to a second geographic scope rather than introducing new mechanics.

**Independent Test**: Can be fully tested by filtering the directory to a non-India country and confirming temples appear with a clear "worship status" (active place of worship vs. heritage/monument vs. partially active) alongside standard location and deity fields.

**Acceptance Scenarios**:

1. **Given** a user filters by a non-India country, **When** results load, **Then** every result shows its worship status alongside location and deity.
2. **Given** a heritage-site temple has no regular darshan schedule, **When** viewed, **Then** the page shows visitor/tourism information instead of an empty or misleading "darshan hours" field.

---

### User Story 5 - Explore the traditional cosmology beyond Earth (Priority: P2)

A devotee, monk, or spiritually curious user wants to understand the traditional Sanatana cosmology that sits beyond the physical, visitable directory: the other planets/planes (lokas) described in the Puranas and Vedas, and the spiritual world beyond material creation (e.g., Vaikuntha, Goloka Vrindavana, Kailasa, Devi Loka/Manidvipa) — each grounded in a named scripture, not presented as a physical travel destination.

**Why this priority**: Explicitly requested as part of the full scope ("other planets, Spiritual world") and directly supports the monk/podcast research goal (Story 3) with doctrinally-grounded cosmological content. P2 because it enriches and completes the directory's traditional worldview but isn't required for the core visit-planning MVP (Stories 1–2), since these realms cannot be visited.

**Independent Test**: Can be fully tested by opening the "Beyond Earth" section and confirming every entry names a specific scriptural source (e.g., a named Purana, Upanishad, or the Brahma Samhita), is clearly separated from the physical temple directory (no address, no darshan hours, no "how to reach" field), and — where traditions disagree on the supreme abode — presents each tradition's own account rather than declaring one universally authoritative.

**Acceptance Scenarios**:

1. **Given** a user opens the "Beyond Earth" section, **When** they browse it, **Then** they see it clearly separated from the physical, visitable temple directory.
2. **Given** a user views an "other planet"/loka entry (e.g., one of the fourteen traditional lokas), **When** the page loads, **Then** it names a specific scriptural source and does not present address, darshan-hours, or travel fields.
3. **Given** a user views a "spiritual world" entry describing a deity's supreme abode (e.g., Vaikuntha, Goloka, Kailasa, Manidvipa), **When** more than one tradition describes a different supreme abode, **Then** the page presents each tradition's account attributed to its own scripture rather than asserting a single universal answer.
4. **Given** a monk is researching this content for a podcast, **When** they read an entry, **Then** they can identify which specific text/verse grounds each claim.

---

### User Story 6 - Contribute or correct a temple listing (Priority: P3)

A knowledgeable community member (devotee, local resident, temple administrator) wants to submit a new temple that's missing from the directory, or correct/enrich an existing listing, so the directory keeps growing toward full comprehensiveness.

**Why this priority**: Supports the "as comprehensive as possible" goal over time, but the directory delivers real value (Stories 1–4) before any contribution workflow exists, using an initial curated dataset.

**Independent Test**: Can be fully tested by submitting a new temple entry or an edit to an existing one and confirming it enters a pending/review state rather than immediately overwriting or polluting verified public data.

**Acceptance Scenarios**:

1. **Given** a contributor submits a new temple, **When** the submission is saved, **Then** it is marked pending review and is not yet shown as verified public content.
2. **Given** a contributor edits an existing verified temple's details, **When** the edit is submitted, **Then** the original verified version remains visible until the edit is reviewed.
3. **Given** a reviewer approves a submission, **When** approval is recorded, **Then** the entry (or edit) becomes part of the public, verified directory.

---

### Edge Cases

- What happens when a temple is known by multiple names or spellings across languages (Sanskrit, Tamil, Hindi, regional, and English transliterations)? The directory must resolve these to one canonical entry rather than creating duplicates.
- How does the directory handle a Divya Desam entry that is celestial/non-physical (Thiruparkadal, Paramapadam)? It must omit or clearly suppress location and visiting-hours fields rather than leaving them blank or broken.
- How does the directory handle a temple that is currently closed, under renovation, destroyed, or rebuilt? Status must be visible so a pilgrim doesn't travel to a closed site.
- How does the directory handle a temple complex containing multiple shrines/deities under one physical site? It must represent the complex and its constituent shrines without forcing an artificial single-deity classification.
- How does the directory handle access restrictions (e.g., dress codes, non-Hindu visitor restrictions, restricted inner-sanctum access) so visitors aren't surprised on arrival?
- How does the directory handle two independent contributors submitting the same temple under different names? The review workflow must detect likely duplicates before publishing.
- How does the directory handle a temple with sparse, unverified, or disputed historical information? The page must distinguish documented history from oral tradition/legend rather than presenting both as equally certain.
- How does the directory handle a temple that is significant to more than one tradition (e.g., shared Shaiva-Shakta or Vaishnava-Shaiva significance)? Classification must allow more than one tradition tag rather than forcing a single choice.
- How does the directory handle traditions that disagree on cosmology (e.g., Vaishnava, Shaiva, and Shakta traditions each naming a different supreme/eternal abode)? Each tradition's account must be presented on its own terms, attributed to its own scripture, rather than the directory asserting one as the single correct answer.
- How does the directory handle a claim that has no traceable scriptural source, only popular or sectarian belief? It must be labeled as tradition/belief rather than presented with the same authority as a cited scripture.
- What happens when a user tries to apply visit-planning fields (address, darshan hours, how to reach) to a non-physical realm? The interface must not surface those fields for entries classified as non-physical.

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The directory MUST include temples located within India, organized by continent (Asia) > country (India) > state/union territory > city.
- **FR-002**: The directory MUST include Sanatana/Hindu temples located outside India, organized by continent > country > city, covering both actively-worshipped diaspora community temples and historic heritage/monument temples, across all continents where such temples exist (Asia outside India, Europe, Africa, North America, South America, Oceania).
- **FR-003**: The directory MUST include a complete, dedicated collection of all 108 Divya Desams, distinct from the general listing, each tagged with its traditional pilgrimage region — one of seven groups: Chola Nadu (40), Nadu Nadu (2), Thondai Nadu (22), Malai Nadu (13), Pandya Nadu (18), Vada Nadu (11), or the celestial group (2) — or its celestial classification.
- **FR-004**: Each Divya Desam entry MUST indicate whether it is (a) a physical site in India, (b) a physical site outside India, or (c) celestial/non-physical; celestial entries MUST NOT display location, darshan-hours, or travel fields.
- **FR-005**: Each temple entry MUST record: primary name, known alternate names/transliterations, presiding deity or deities, tradition/sect classification (Vaishnava, Shaiva, Shakta, Smarta, or other/folk), and precise location (address or descriptive location, city, state/region, country, and coordinates where available).
- **FR-006**: Each temple entry MUST record visit-planning information: visiting/darshan hours (or a note that none apply), best time of year to visit, major festivals with approximate dates, and how to reach the site.
- **FR-007**: Each temple entry MUST record a "worship status" of active place of worship, heritage/monument site, or partially active, so users know what kind of visit to expect.
- **FR-008**: Each temple entry MUST record research-oriented content usable for podcast/teaching preparation: an origin/legend narrative, at least one named source or tradition it draws from (e.g., a specific Purana, the Divya Prabandham, Thevaram, local tradition/oral history), and any associated saints or sages.
- **FR-009**: Users MUST be able to search temples by name, including matches on alternate names/transliterations.
- **FR-010**: Users MUST be able to filter or browse temples by continent, country, state/region, deity, tradition, and Divya-Desam membership.
- **FR-011**: The directory MUST support curated groupings similar to the reference site's model (e.g., Featured, Trending/Popular, Newly Added), independent of the fixed 108 Divya Desam collection.
- **FR-012**: The directory MUST allow community members to submit new temple entries or propose corrections to existing entries.
- **FR-013**: Community-submitted entries and edits MUST enter a pending-review state and MUST NOT replace or appear as verified public content until reviewed and approved.
- **FR-014**: The 108 Divya Desam collection's core facts (identity, region grouping, celestial vs. physical status) MUST be treated as editorially verified and MUST NOT be alterable through unreviewed community submissions.
- **FR-015**: The directory MUST flag likely duplicate submissions (e.g., matching location plus a similar name) for reviewer attention before publishing.
- **FR-016**: Each temple entry SHOULD include one or more representative images when available, and MUST clearly indicate when no image is available rather than showing a broken element.
- **FR-017**: Each temple entry's historical/legendary content MUST visually or textually distinguish documented/attested history from oral tradition or legend.
- **FR-018**: A temple entry MUST support more than one tradition/sect tag and more than one enshrined deity, to represent shared or multi-shrine sites.
- **FR-019**: The directory MUST include a "Beyond Earth" section, separate from the physical temple directory, covering the traditional Puranic/Vedic cosmology: the other planets/planes (lokas) of the fourteen-loka system, and the spiritual world beyond material creation (e.g., Vaikuntha, Goloka Vrindavana, Kailasa, Devi Loka/Manidvipa), organized by tradition.
- **FR-020**: Every entry in the directory — physical temple, loka/planet, or spiritual-world abode — MUST cite at least one named source (a specific scripture/text, or explicitly "oral tradition/local legend" when no scriptural source exists), and the citation type MUST be visibly distinguishable from unattributed claims.
- **FR-021**: Where traditions give differing or conflicting cosmological accounts (e.g., a different supreme/eternal abode per Vaishnava, Shaiva, or Shakta tradition), the directory MUST present each account attributed to its own tradition and scripture, and MUST NOT assert a single account as universally authoritative.
- **FR-022**: Entries in the "Beyond Earth" section MUST NOT display physical-visit fields (address, coordinates, darshan hours, how to reach), since they describe non-physical realms.
- **FR-023**: Content for the "Beyond Earth" section and any content citing scripture MUST pass a review step by a contributor/reviewer versed in the relevant tradition before publishing, given its doctrinal sensitivity, in addition to the standard duplicate/accuracy review applied to physical temple submissions.

### Key Entities

- **Temple**: A single place of worship or heritage site. Attributes include primary name, alternate names, deity/deities, tradition/sect tag(s), location (address, city, state/region, country, coordinates), worship status, visiting/darshan info, festival calendar, history/legend narrative with sourcing, associated saints, images, verification status (verified vs. pending), and Divya-Desam membership flag.
- **Divya Desam Entry**: One of the fixed 108 records glorified by the Alvars. Links to a Temple when physical, or stands alone with a celestial classification when not. Carries its traditional region grouping (e.g., Chola Nadu, Malai Nadu, Vada Nadu).
- **Deity**: A named form of the divine enshrined at one or more temples (e.g., Venkateswara, Meenakshi, Jagannath), with associated tradition.
- **Tradition/Sect**: A classification such as Vaishnava, Shaiva, Shakta, Smarta, or regional/folk tradition, usable as a filter and applicable to a temple in more than one instance.
- **Region**: A geographic grouping — continent, country, and within India, state/union territory — used for browsing and filtering.
- **Realm (Loka)**: A non-earthly plane or abode described in scripture rather than a physical location — e.g., one of the fourteen traditional lokas, or a deity's spiritual-world abode (Vaikuntha, Goloka, Kailasa, Manidvipa). Attributes include name, governing deity, tradition, position in cosmology, and its scriptural citation(s). Never carries physical-visit fields.
- **Source Citation**: A reference attached to a factual or cosmological claim — either a named scripture/text (with chapter/verse where available) or an explicit "oral tradition/local legend" label — used to ground content in tradition and distinguish attested scripture from popular belief.
- **Contribution/Submission**: A community-proposed new temple, loka/spiritual-world entry, or edit to an existing one, with submitter reference, proposed data, and a review status (pending, approved, rejected).
- **Curated Collection**: A named grouping of temples (Featured, Trending, New, 108 Divya Desam, Beyond Earth) used to surface subsets of the directory.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: A user can locate a specific temple's complete visit-planning details (location, hours or equivalent note, best time to visit, how to reach) within 3 steps from the homepage.
- **SC-002**: The directory includes 100% of the 108 Divya Desams at launch, each with a complete region tag and correct physical/celestial classification.
- **SC-003**: The directory includes actively-worshipped or heritage Sanatana temples spanning at least 15 countries outside India at launch, reflecting the major global Hindu diaspora and historic heritage regions.
- **SC-004**: For at least 80% of temples in the Featured and Divya Desam collections, a content creator can find a history/legend narrative with a named source and any associated saints without consulting an external reference.
- **SC-005**: At least 90% of users surveyed after visiting a temple's detail page agree it gave them enough information to plan a visit without checking another source.
- **SC-006**: Community-submitted entries reach a review decision (approved or rejected) within a defined turnaround window, keeping the pending queue from silently stalling growth of the directory.
- **SC-007**: No published Divya Desam entry is ever altered to contradict its editorially verified region/classification through an unreviewed submission.
- **SC-008**: 100% of published entries in the "Beyond Earth" section cite a named scriptural source, and 0% display physical-visit fields (address, coordinates, darshan hours, how to reach).
- **SC-009**: Where more than one tradition describes a differing cosmological account, 100% of the affected entries present each tradition's account with its own attribution, rather than a single unattributed answer.
- **SC-010**: The physical directory spans temples across all six inhabited continents where Sanatana temples exist (Asia, Europe, Africa, North America, South America, Oceania) at launch.

## Assumptions

- "Comprehensive" is interpreted as: complete coverage of the closed, canonical 108 Divya Desam list, plus as broad a curated set of other historically, religiously, or culturally significant Sanatana temples (in India and globally) as can be verified — expanding over time through community contribution, rather than an exhaustive census of every small local shrine from day one.
- "Podcast" support is interpreted as providing sufficiently rich, sourced reference material (history, legends, scriptural citations, associated saints) for a monk or creator to prepare spoken content — not as a feature to record, host, or publish audio episodes within the directory itself. Audio/podcast production tooling is out of scope for this feature.
- Historic/archaeological Hindu temple sites with little or no active daily worship (e.g., Angkor Wat, Prambanan) are in scope, since they are visited by pilgrims and travelers and are relevant to podcast-style cultural/historical content, but are distinguished from active places of worship via the "worship status" field so visitor expectations are set correctly.
- The scope is Hindu/Sanatana Dharma temples across all its major traditions (Vaishnava, Shaiva, Shakta, Smarta, and regional/folk deity traditions). Jain, Buddhist, and Sikh sites are out of scope unless a site is historically shared/syncretic and independently notable as a Sanatana worship site.
- Data quality follows a hybrid model, matching the reference site's crowdsourced approach: open community contribution drives breadth and growth, while a review step and an explicit verified/pending distinction protect accuracy — with the 108 Divya Desam collection held to the highest, editorially-locked standard given its religious and cultural significance.
- Coordinates/addresses are best-effort; some remote or historic sites may only have descriptive location rather than precise coordinates at launch.
- Language of record is English with native-script alternate names captured per temple; full multi-language localization of the interface is out of scope for this feature.
- "Other planets" refers to the traditional Puranic/Vedic cosmological planes (the fourteen lokas and related realms described in scripture), not modern astronomical exoplanets or space exploration; this section is explicitly doctrinal/devotional content, not a science feature.
- "Ground the information in tradition" means every factual, historical, or cosmological claim is traceable to a named scripture, text, or explicitly-labeled oral tradition, verified by someone knowledgeable in that specific tradition — applied uniformly across physical temples, the 108 Divya Desams, and the Beyond Earth section, with the strictest scrutiny reserved for cosmological/doctrinal claims given their sensitivity across differing sampradayas (lineages).
