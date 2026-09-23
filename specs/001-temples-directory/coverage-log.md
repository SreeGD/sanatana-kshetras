# Coverage Baseline Snapshot

Recorded after the first general-catalog authoring pass (T009-T012), on top of the completed 108 Divya Desam collection.

```
Temples by continent:
  asia: 124

Countries outside India (1):
  Nepal: 1
```

## Notes

- 106 of the 124 temples above are the physical Divya Desam collection (see `content/divya-desam/`); 18 are the general-catalog additions from T009/T010, spanning Uttar Pradesh, Uttarakhand, Tamil Nadu, Karnataka, Andhra Pradesh, Kerala, Odisha, Assam, West Bengal, Gujarat, Madhya Pradesh, and Jammu & Kashmir.
- General-catalog entries deliberately diversify tradition coverage beyond the Divya Desams' exclusively Vaishnava scope: Shaiva (Kashi Vishwanath, Kedarnath, Brihadeeswarar, Ramanathaswamy, Srisailam, Vadakkunnathan, Ekambareswarar, Lingaraj, Somnath, Mahakaleshwar), Shakta (Kollur Mookambika, Srisailam Bhramaramba, Kamakshi Amman, Kamakhya, Dakshineswar, Vaishno Devi), and Smarta (Sringeri Sharada Peetham).
- Not yet started: non-India (diaspora/heritage) temples (US4), Beyond-Earth cosmology (US5), and the contribution workflow (US6).

## Global (non-India) coverage — after US4 (T024-T026)

16 countries outside India, all 6 inhabited continents represented (SC-003, SC-010 both satisfied):

- **Active-worship diaspora/living tradition (12)**: Singapore, Malaysia, Nepal (Pashupatinath), Indonesia (Pura Besakih, Bali — living Balinese Hindu tradition), Fiji, Australia, USA, Trinidad and Tobago, United Kingdom, South Africa, Mauritius, Guyana, Sri Lanka.
- **Heritage/monument sites (4)**: Cambodia (Angkor Wat), Vietnam (My Son Sanctuary), Indonesia (Prambanan), Pakistan (Katas Raj Temples) — each flagged with its current worship status (no longer active, or only occasional/limited pilgrimage) per FR-007.

## ISKCON (Gaudiya Vaishnava) coverage

7 ISKCON/Hare Krishna temples added, all `status: verified` from the outset (cross-checked against dedicated Wikipedia articles before authoring, not after): 4 in India (Mayapur — ISKCON's world headquarters, Vrindavan's Krishna Balaram Mandir, Bangalore, Delhi) and 3 international (New Vrindaban WV USA, Bhaktivedanta Manor UK, and the founding site in New York City, 1966). Represents ISKCON's global footprint (~100+ countries) with a curated, high-confidence starting set rather than exhaustive coverage — a natural area to expand later given how well-documented the movement is.

## Additions sourced from templesofindia.org's public listing

templesofindia.org describes itself as "a growing devotee-led temple directory with 6L+ temples" (600,000+ crowdsourced entries) - far beyond any scope this project can or should bulk-import (both infeasible at that scale and a real ToS/copyright concern around wholesale-copying another platform's compiled crowdsourced database). Instead, its public homepage (Trending/Featured sections, ~18 named temples) was used only as a set of *leads* - names and locations - each independently verified against Wikipedia and written as original content here, not copied from that site.

Of 18 names: 3 were already in this directory (Jagannath Puri, Mahakaleshwar Ujjain, Lingaraj Bhubaneswar). Of the rest, 6 had dedicated, verifiable sources and were added: Kailasa Temple (Ellora, UNESCO monolithic rock-cut temple), Shree Siddhivinayak Ganapati Mandir (Mumbai), Sankat Mochan Hanuman Mandir (Varanasi), Shri Vishwanath Mandir/BHU (Varanasi - distinct from the main Kashi Vishwanath), Shri Bhadra Maruti Temple (Khuldabad, reclining-Hanuman iconography), and Sri Panchamuga Vishwaroopa Anjaneyar Temple (Karaikkudi - five-faced Hanuman; only the general iconographic tradition could be confirmed, not this specific temple's own history, so it stays `status: pending`). The remaining names (a generically-named "Hanuman Temple" in Kendujhargarh, two Mumbai temples that appear to be branch/replica sites of originals already covered elsewhere, and two more with no dedicated source found) were not added rather than written unsourced.

## ISKCON coverage, batch 2

6 more ISKCON entries: London (1968, Europe's first ISKCON temple, verified), Chennai (existence confirmed, details pending), and 4 compiled-from-general-knowledge entries explicitly marked `status: pending` since a live source couldn't be reached this session for these regions — South Africa (Durban), Brazil (Nova Gokula), Belgium (Radhadesh), Australia (Sydney). This intentionally trades some rigor for continent coverage (Africa, South America, Oceania now all have an ISKCON presence recorded) per explicit user direction; each carries a clear review_flag recommending independent confirmation.

## India catalog expansion via Wikipedia state-list articles

Explored Wikipedia's "List of Hindu temples in <state>"-style articles to find candidates beyond the initial curated set, verified each individually before writing (same standard as elsewhere). Added 6 entries across 3 states with no prior coverage:

- **Telangana**: Ramappa Temple (Palampet — UNESCO World Heritage, 13th-century Kakatiya "floating brick" engineering), Sri Lakshmi Narasimha Swamy Temple (Yadagirigutta — ~1,800 crore, 2016-2022 renovation).
- **Bihar**: Vishnupad Temple (Gaya — India's principal ancestral-rites/shraddha pilgrimage site), Mundeshwari Temple (Kaimur — among the oldest surviving Hindu temple structures in India, with a genuinely disputed dating between 108 CE and the 6th-7th century), Mahavir Mandir (Patna — one of the most-visited Hanuman temples in India).
- **Goa**: Shanta Durga Temple (Kavalem — Goa's most important Hindu temple, relocated inland after Portuguese destruction of the original site in 1566).

State list articles also surfaced many more candidates (Bhadrachalam and Birla Mandir in Telangana; several more in Bihar and Goa) not yet added — a natural next expansion.

## Full state-by-state pass (India)

Dispatched 3 parallel research passes to systematically cover every Indian state/UT still missing from the directory. Result: **33 of India's 36 states/UTs now have at least one entry** (up from 17), all cross-checked against Wikipedia before writing, with honest `review_flags`/`status: pending` wherever a specific detail (founding date, dynasty, Shakti Peetha status, etc.) wasn't confirmable from available sources — several entries deliberately correct or withhold a popular claim the source didn't support (e.g. not asserting Mansa Devi Panchkula as a Shakti Peetha, reclassifying Amritsar's Ram Tirath as its officially renamed Valmiki-tradition site).

**Newly covered (16 states/UTs)**: Rajasthan (4), Haryana (3), Punjab (3), Himachal Pradesh (4), Jharkhand (2), Chhattisgarh (2), Puducherry (2), Chandigarh (2, both flagged as physically in neighboring Panchkula/Haryana since no verifiable temple exists administratively inside the UT itself), Manipur (1), Tripura (1), Sikkim (1), Arunachal Pradesh (1), Meghalaya (1), Nagaland (1), Andaman & Nicobar Islands (1), Dadra & Nagar Haveli and Daman & Diu (1).

**Genuinely no verifiable Hindu temple found** (not a gap — an honest research finding, consistent with regional demographics): Mizoram (Christian-majority; only an unverifiable aggregate mention of "13 temples" via one committee, no individual temple confirmable), Ladakh (Buddhist-majority; no Hindu temple article/category exists), Lakshadweep (Muslim-majority; same).

India state/UT coverage: 33/36.

## District-level deepening within covered states

Dispatched 5 parallel research passes (4 landed so far) to add temples in districts/cities not previously represented within already-covered states, same WebFetch-verification rigor throughout. Added 47 new temple entries across Andhra Pradesh, Karnataka, Kerala, Telangana, Uttar Pradesh, Madhya Pradesh, Uttarakhand, Rajasthan, Gujarat, Maharashtra, Goa, Punjab, Haryana, West Bengal, Odisha, Bihar, Assam, Jharkhand, and Chhattisgarh — including several major sites previously missing entirely (Khajuraho, Omkareshwar, Trimbakeshwar, Pandharpur's Vithoba Temple, Hampi's Virupaksha Temple, Sabarimala, Guruvayur, Konark Sun Temple, Modhera Sun Temple).

Notable judgment calls made honestly rather than glossed over: Modhera, Konark, and Sirpur's Lakshmana Temple were set to `worship_status: heritage` after confirming no active daily worship; Kolhapur's Mahalakshmi Temple got a `review_flags` entry for a genuine scholarly dispute over whether it was originally a Jain temple; Achaleshwar Mahadev (Mount Abu) got a flag for an internal date conflict in its own sourcing (a cited 1412 construction date predates the Rana Kumbha reign it's also attributed to) rather than a fabricated resolution.

A 5th pass (Himachal Pradesh, J&K, Delhi, Puducherry, and the remaining single-temple states/UTs) is still in progress as of this commit.

## District deepening, final pass (5th group)

8 more temples: Himachal Pradesh (Naina Devi, Bilaspur — distinct from Uttarakhand's Naina Devi, Nainital), Jammu and Kashmir (Raghunath Temple, Jammu), Delhi (Kalkaji Mandir; Laxminarayan/Birla Mandir, Mandir Marg — distinct from Hyderabad's Birla Mandir), Puducherry (Thirunallar Dharbaranyeswarar, Karaikal district — a Navagraha/Shani temple), Manipur (Vishnu Temple, Lamangdong), Arunachal Pradesh (Malinithan, a 13th-14th c. archaeological site — worship_status: heritage), and Sikkim (Siddhesvara Dham, Namchi — a modern Char Dham/Jyotirlinga-replica complex, distinct district from the existing Legship entry).

Genuinely came up empty after real research attempts (not forced): a second temple for Meghalaya, Nagaland, Andaman & Nicobar Islands, and Dadra & Nagar Haveli and Daman & Diu; and a second temple for Tripura specifically (Agartala candidates lacked confirmable founding/dynastic attribution).

This completes the district-deepening pass: 55 temples added in total across all 5 groups.

## Asia continent expansion (outside India)

Dispatched 2 parallel research passes to expand Asia-outside-India coverage, same WebFetch-verification rigor throughout.

**New countries** (5): Bangladesh (Dhakeshwari Temple — "National Temple of Bangladesh"; Chandranath Temple; Ramna Kali Mandir, rebuilt after the 1971 massacre), Thailand (Devasathan — Bangkok's royal Brahmin temple; Sri Maha Mariamman Temple; Erawan Shrine — deliberately flagged as not a conventional Hindu temple per its own Wikipedia sourcing, included for its Brahma iconographic origin), United Arab Emirates (BAPS Hindu Mandir Abu Dhabi, opened 2024; the historic Bur Dubai temple, honestly flagged for its 2022-2024 split across two sites), Myanmar (Shri Kali Temple, Yangon, 1871), and China (Quanzhou's medieval Tamil-merchant Hindu temple carvings, 1281-83 CE — worship_status: heritage; the agent caught and corrected a source conflation about the Buddhist Kaiyuan Temple).

**Deepened existing countries** (8 new entries across 6 countries): Nepal (Janaki Mandir, Janakpur — Sita's traditional birthplace; Changu Narayan, oldest dated Hindu temple in Nepal), Sri Lanka (Kataragama — set worship_status: partially_active given its genuinely multi-religious character; Munneswaram), Pakistan (Hinglaj Mata Temple/"Nani Mandir," Balochistan — a major Shakti Peetha with ~300,000 annual pilgrims), Malaysia (Sri Rajakaliamman Glass Temple, Johor Bahru), Singapore (Sri Srinivasa Perumal Temple), and Indonesia (Pura Tanah Lot, Bali — a suspicious $480M restoration-cost figure was deliberately omitted rather than repeated unverified).

Asia (outside India) now spans 14 countries.

## Europe continent expansion + ISKCON gap-fill (Asia and Europe)

Dispatched 4 parallel research passes: 2 for general Europe expansion (Germany, Netherlands, France, Switzerland, Italy, Portugal, Austria, Ireland, a 2nd UK city), and 2 specifically to fill an ISKCON coverage gap the user flagged — the recent Asia and Europe expansion passes had focused on general diaspora/Tamil-community temples without specifically checking for ISKCON presence.

**Europe: 11 new temples, 8 new countries** — Germany (Sri Kamadchi Ampal Temple, Hamm; Pura Tri Hita Karana, Berlin — a Balinese temple in a public park; ISKCON Simhachalam, Jandelsbrunn — uniquely dedicated to Narasimha), Netherlands (Shri Ram Mandir, The Hague; ISKCON Amsterdam, heavily hedged), France (Sri Manicka Vinayakar Alayam, Paris; ISKCON New Mayapur, Luçay-le-Mâle), Switzerland (2 Tamil-community temples, Adliswil and Glattbrugg), Italy (Matha Gitananda Ashram — Saiva Siddhanta/Srividya, national HQ of the Italian Hindu Union; ISKCON Villa Vrindavana, Tuscany), Portugal (Radha Krishna Mandir, Lisbon — community descended from Daman/Diu Hindus via Mozambique), Ireland (a thin but real entry, Dublin), Spain (ISKCON New Vraja Mandala, corrected from a wrong initial lead). UK deepened with ISKCON Leicester. Austria yielded nothing verifiable and was correctly left out.

**Asia ISKCON gap-fill: 5 new entries** — Bangladesh (Swami Bagh Temple/ISKCON Dhaka, with the 2021 Noakhali violence correctly identified as a *different* location, not conflated), Indonesia (ISKCON Jakarta), Thailand (ISKCON Bangkok's multi-center presence, no single flagship address found), Malaysia (thin sourcing, honestly flagged), Singapore (a genuinely unusual case: ISKCON was legally banned by name in the 1970s; the community still worships today under other registered names — documented as such rather than glossed over). Nepal and Sri Lanka yielded no verifiable ISKCON temple after extensive search and were correctly left out.

Europe now spans 11 countries; Asia (outside India) 14 countries, several with a dedicated ISKCON presence now recorded alongside their general temples.

## Full continent sweep: Africa, North America, South America, Oceania

Dispatched 5 parallel research passes to bring the remaining thin continents up to a comparable standard: 2 for Africa, 1 each for North America, South America, and Oceania.

**Africa: 19 temples, 8 countries** (was 2 countries, 3 temples) — Kenya (incl. ISKCON Nairobi/Devasadan, active since 1969), Tanzania (incl. ISKCON Dar es Salaam), Uganda (Shree Sanatan Dharma Mandal, Kampala, 1954-64 — no ISKCON presence found, reported honestly), Réunion (Temple du Colosse and Temple du Gol, both centuries-old), South Africa deepened to 4 (Johannesburg/Lenasia), Mauritius deepened to 3 (Triolet's Maheswarnath Mandir, Sagar Shiv Mandir), plus new entries in Zimbabwe and Zambia. Nigeria and Madagascar yielded nothing verifiable.

**North America: 14 temples, 3 countries** (was 2 countries, 4 temples) — Canada added entirely (BAPS Toronto, ISKCON Toronto, Vishnu Mandir Richmond Hill), USA deepened to 9 (Malibu, BAPS Atlanta, BAPS Houston, Sri Siva Vishnu Maryland, Sri Meenakshi Pearland, ISKCON Spanish Fork Utah), Trinidad and Tobago deepened to 2.

**South America: 9 temples, 4 countries** (was 2 countries, 2 temples) — Suriname added entirely (Arya Diwaker Mandir 1929, Surya Mandir, ISKCON Nieuw Nickerie), Brazil and Guyana deepened, plus a genuine find in Chile: Punta Arenas Hindu Temple, described as the southernmost Hindu temple in the world.

**Oceania: 8 temples, 3 countries** (was 2 countries, 3 temples) — New Zealand added entirely (Bharatiya Mandir Auckland, 1986/1993 - NZ's oldest purpose-built Hindu temple; Shri Swaminarayan Mandir Auckland), Australia deepened with Perth (2 temples), Fiji deepened with a historically significant 1905 temple destroyed in 2008 communal arson (documented as heritage status given unconfirmed rebuild).

**Countries outside India: 41** (up from 18 before this session's Asia/Europe/Africa/Americas/Oceania passes began).

Consistent pattern throughout: WebSearch unavailable all session, so every claim is WebFetch-verified against Wikipedia (occasionally non-English Wikipedia or official temple sites); every genuinely unconfirmable detail is hedged in prose or flagged, never asserted; several countries (Nigeria, Madagascar, Argentina, Venezuela, and specific cities within covered countries) were honestly reported as yielding nothing verifiable rather than forced.

## Deepening the newly-added countries (10 countries from the continent sweep)

Dispatched 3 parallel passes to add temples in additional cities within Canada, Suriname, New Zealand, Kenya, Tanzania, Uganda, Réunion, Zimbabwe, Zambia, and Chile. 21 new temples added, 1 existing entry enriched with better sourcing rather than padded with a weak duplicate (Zambia).

**Canada**: 3 new provinces beyond Ontario — Aulds Cove Hindu Temple, Nova Scotia (1972, one of North America's oldest Hindu temples), ISKCON Montreal (1967, the third Krishna temple in the world outside India per its own history), ISKCON Calgary.
**Suriname**: 1 more Paramaribo-area temple (Blauwgrond), independently sourced.
**New Zealand**: 3 new cities — BAPS Christchurch, Sri Balaji Hamilton, Sri Venkateswara Swamy Wellington.
**Kenya**: BAPS Nairobi, Shivalaay Shiva Temple Mombasa.
**Tanzania**: ISKCON Arusha (the "second center" flagged but unwritten in the earlier pass), Shri Sanatan Dharma Mandir Mwanza.
**Uganda**: Vishwakarma Temple, Jinja (thinnest entry of this round, honestly flagged).
**Réunion**: Temple des Casernes, Saint-Pierre (sourced via France's official Mérimée heritage database) and Temple Kalikambal, Saint-Denis.
**Chile**: Hindu Temple of Santiago, sourced via two independent Wikipedia biographical articles about a Chilean diplomat who attends it.
**Zambia**: existing Lusaka entry enriched with a second independent source rather than a new weak entry.
**Zimbabwe**: genuinely nothing additional verifiable found — reported honestly.

This round again relied entirely on WebFetch (Wikipedia in multiple languages, official temple sites, and one national heritage database) since WebSearch remained unavailable throughout.

## Major spiritual tourist destination gap-check (user-requested audit)

User asked to specifically verify coverage of Ayodhya, Vrindavan, Srirangam, Haridwar, Madurai, and Guruvayur, and to search for other major spiritual tourist destinations. All 6 named places were already covered (Ayodhya and Srirangam via Divya Desam, Madurai via Meenakshi Amman + Koodal Azhagar Divya Desam, Guruvayur, Haridwar via Mansa Devi Temple, Vrindavan via ISKCON Krishna Balaram Mandir).

The broader search found 8 genuine gaps among India's most-visited spiritual/tourist sites, all now added:
- **Banke Bihari Temple**, Vrindavan — arguably Vrindavan's single most-visited temple, distinct from ISKCON's Krishna Balaram Mandir
- **Prem Mandir**, Vrindavan — a major modern pilgrimage/tourist site (2012, ~150 crore)
- **Swaminarayan Akshardham**, Delhi — Guinness World Record holder for world's largest comprehensive Hindu temple
- **Shree Samadhi Mandir, Shirdi** — one of India's most-visited pilgrimage sites (~25,000 daily pilgrims); included with an explicit review_flag noting Sai Baba's own teaching and practice were syncretic (Hindu-Muslim), not straightforwardly Sanatana Dharma, per this project's stated scope for historically shared/syncretic sites
- **Gangotri** and **Yamunotri** — completing the Char Dham circuit (Badrinath and Kedarnath were already covered)
- **Har Ki Pauri**, Haridwar — the actual sacred ghat and site of the daily Ganga Aarti, distinct from the previously-covered Mansa Devi Temple
- **Amarnath Cave Shrine** — the ice-lingam pilgrimage site drawing hundreds of thousands annually; its documented history of security incidents (2000, 2001, 2002, 2017) is noted factually as pilgrimage-planning context, not sensationalized

This audit is a useful reminder that "comprehensive" coverage benefits from periodic top-down checks against known-major sites, not just bottom-up state/district/country sweeps.

## Completing three canonical Shaiva/Murugan lists

Following the Jyotirlinga/Panch Bhoota Sthalam/Arupadaiveedu gap audit, dispatched 2 parallel passes to complete all three well-defined lists (this directory already had 9/12 Jyotirlingas and 1/5 Panch Bhoota Sthalams; 0/6 of Murugan's Arupadaiveedu existed).

**Jyotirlingas — now 12/12**: added Bhimashankar (Maharashtra), Nageshwar (Gujarat, honestly flagged for a genuine three-way location dispute with rival claimant sites in Uttarakhand and Maharashtra), and Grishneshwar (Maharashtra — confirmed distinct from the already-covered Kailasa Temple, Ellora, ~1.5 km away; caught and flagged an internal inconsistency in Wikipedia's own article over who funded its 1729 rebuild).

**Panch Bhoota Sthalams — now 5/5**: added Thillai Nataraja Temple, Chidambaram (akasha/ether — confirmed clearly distinct from the existing Divya Desam Govindaraja Perumal Vishnu-shrine entry at the same complex), Arunachaleswarar Temple, Tiruvannamalai (agni/fire, with Ramana Maharshi's associated ashram noted briefly), Srikalahasti (vayu/air), and Jambukeswarar Temple, Thiruvanaikaval (jala/water) — the latter two both had their popular founding-date claims flagged as unconfirmed rather than repeated as fact.

**Arupadaiveedu (Murugan's six abodes) — now 6/6**: Palani, Tiruchendur, Swamimalai, Tiruttani, Pazhamudircholai, and Thiruparankundram, each tagged with its traditional mythological episode (renunciation, Soorasamharam, teaching Om to Shiva, the Valli courtship, etc.).

Also added: **Bhagavathy Amman Temple, Kanyakumari** — India's southernmost major Devi temple, with the secular Vivekananda Rock Memorial nearby correctly excluded as not a temple.

This closes out the canonical-list-completion approach for Shaiva/Murugan traditions, mirroring how the 108 Divya Desam collection was completed earlier for Vaishnava tradition.
