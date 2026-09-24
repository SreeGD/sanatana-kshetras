# Sanatana Kshetras

A comprehensive, git-based directory of Hindu / Sanatana Dharma temples across India and the globe — built as structured content, not a database, so every entry is reviewable, versioned, and sourced like code.

The goal: give pilgrims a reliable way to plan a visit, and give podcasters, monks, and researchers a well-sourced starting point for a story — without ever presenting oral tradition or AI-assisted drafting as settled fact.

## What's in here

| | |
|---|---|
| **Temples** | 860, across 6 continents and 67 countries outside India |
| **108 Divya Desam** | 106 physical + 2 celestial entries — the canonical Vaishnava collection, complete and locked |
| **Beyond Earth** | 11 cosmology entries (the six lokas, the seven patalas, and spiritual-world abodes like Vaikuntha and Kailasa) |
| **Deity categories** | 29 computed worship categories (Rama, Krishna, Narasimha, Shiva, Devi/Shakti, Ganesha, Murugan, Hanuman, and more) — see below |

Canonical lists tracked to completion: 108/108 Divya Desam, 12/12 Jyotirlinga, 9/9 Navagraha, 8/8 Ashtavinayak, 6/6 Arupadaiveedu, 5/5 Panch Bhoota Sthalam, plus partial coverage of larger lists (Paadal Petra Sthalam, Shakti Peetha) where sourcing quality, not effort, is the limiting factor.

## Structure

```
content/
  temples/<continent>/<country>/<state-or-na>/<slug>.md   # one file per temple
  divya-desam/<seq>-<slug>.md                              # the 108 Divya Desam entries
  beyond-earth/<slug>.md                                   # cosmological realms
  deities/<slug>.md                                        # worship-category definitions

specs/001-temples-directory/
  spec.md, data-model.md, contracts/*.schema.json          # what a valid entry looks like
  coverage-log.md                                          # append-only log of every addition batch and why

scripts/
  validate_content.py                                      # schema validation + coverage/duplicate/deity reports
```

Every temple entry is YAML front matter (deities, coordinates, sources, `status: verified | pending`, `documented_vs_legend`) plus a short prose history. Nothing is asserted without a citation — legend and documented history are explicitly distinguished, and genuinely unresolved facts stay flagged rather than smoothed over.

## Using the validator

```bash
python3 scripts/validate_content.py                 # schema-validate everything
python3 scripts/validate_content.py --coverage-report   # temples by continent/country
python3 scripts/validate_content.py --divya-desam-report # 108/108 completeness check
python3 scripts/validate_content.py --duplicates          # near-duplicate name detection
python3 scripts/validate_content.py --deity-report --export-json out.json  # temples grouped by deity
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). In short: every entry needs a source, the validator has to pass, and the 108 Divya Desam collection's core fields (`seq`, `region_group`, `physical`) are locked against routine edits.

## License

Licensed under the [GNU General Public License v3.0](LICENSE).
