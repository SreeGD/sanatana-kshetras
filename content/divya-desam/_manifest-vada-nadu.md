---
region_group: vada-nadu
entries:
  - temple_id: sri-venkateswara-temple-tirumala
    name: Sri Venkateswara Temple, Tirumala (Thiruvenkatam)
    country: india
  - temple_id: sri-nava-narasimha-temple-ahobilam
    name: Sri Nava Narasimha Swamy Temples, Ahobilam (Thiru Singavelkundram)
    country: india
  - temple_id: sri-ramar-temple-ayodhya
    name: Sri Ramar Temple, Ayodhya (Thiru Ayodhi)
    country: india
  - temple_id: sri-devaraja-perumal-temple-naimisharanyam
    name: Sri Devaraja Perumal Temple, Naimisharanyam
    country: india
  - temple_id: sri-moorthy-perumal-temple-muktinath
    name: Sri Moorthy Perumal Temple, Muktinath (Thiru Salagramam)
    country: nepal
  - temple_id: sri-badrinarayan-temple-badrinath
    name: Sri Badrinarayan Temple, Badrinath (Thiru Vadariashramam)
    country: india
  - temple_id: sri-neelamega-perumal-temple-devaprayag
    name: Sri Neelamega Perumal Temple, Devaprayag (Thiru Kandamennum Kadinagar)
    country: india
  - temple_id: sri-narasimha-temple-joshimath
    name: Sri Narasimha Temple, Joshimath (Thiruppirithi)
    country: india
  - temple_id: sri-govardhana-nesa-perumal-temple-mathura
    name: Sri Govardhana Nesa Perumal Temple, Mathura (Thiru Vadamathurai)
    country: india
  - temple_id: sri-navamohana-krishna-temple-gokul
    name: Sri Navamohana Krishna Perumal Temple, Gokul (Thiruvaipadi)
    country: india
  - temple_id: sri-dwarkadhish-temple-dwaraka
    name: Sri Dwarkadhish Temple, Dwaraka (Thiru Dwarakai)
    country: india
---

Coordination manifest for the Vada Nadu region group of the 108 Divya
Desams (the North Indian cluster, outside the Tamil Nadu/Kerala heartland).
Final `seq` numbers (1-108), `locked: true`, and individual
`content/divya-desam/*.md` files are assigned centrally by the reviewer
merging all region-group manifests; this file is not itself a Divya Desam
entry and does not conform to `divya-desam.schema.json`.

All 11 entries above were cross-checked against at least two independent
sources (108divyadesams.in, veludharan.blogspot.com's Vada Nadu list, and
uveda.org's Divya Desam index, sequence numbers 96-106 there) before
inclusion. Notes:

- `sri-moorthy-perumal-temple-muktinath` (Thiru Salagramam) is the only
  physical Divya Desam located outside India, in present-day Nepal
  (Mustang district, near Muktinath) -- confirmed by multiple independent
  sources, per FR-004b. It is filed under
  `content/temples/asia/nepal/na/` with no `region` field, per schema.
- `sri-venkateswara-temple-tirumala` (Thiruvenkatam/Tirupati) is included
  here because the majority of consulted sources place it within Vada
  Nadu, though a minority of sources treat it as its own category given
  that it is glorified by nearly all twelve Alvars; see that temple file's
  `review_flags`.
- Several entries (Ayodhya, Mathura, Gokul) carry `review_flags` noting
  uncertainty about whether the present-day temple structure is
  continuous with the ancient Divya Desam shrine, given later
  reconstruction/relocation at those sites.
- The two celestial (non-physical) Divya Desam entries, Thiruparkadal and
  Paramapadam, are NOT part of this region group and are handled
  separately (see `content/divya-desam/107-thiruparkadal.md` and
  `108-paramapadam.md`).
