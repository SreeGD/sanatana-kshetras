## What changed

- [ ] Entity file(s) touched (list paths): 
- [ ] New temple / Divya Desam entry / Beyond-Earth entry / edit to an existing one

## Sourcing

- [ ] Every new or changed factual claim has at least one entry in `sources` (a named scripture/text, or an explicit `oral_tradition` note) — see `specs/001-temples-directory/data-model.md` § Source Citation
- [ ] Anything I couldn't independently verify is listed in `review_flags`, not asserted as fact

## Validation

- [ ] `python3 scripts/validate_content.py` passes locally
- [ ] `python3 scripts/validate_content.py --duplicates` doesn't flag this entry against an existing one
- [ ] If this PR touches `content/divya-desam/`: `python3 scripts/validate_content.py --check-locked <base-ref>` shows no changes to `seq`, `region_group`, or `physical` on any existing entry

## Notes for the reviewer

<!-- Anything that needs a second pair of eyes: disputed facts, a legend vs. documented-history judgment call, a region-group boundary case, etc. -->
