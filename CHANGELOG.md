# CHANGELOG.md

All notable changes to this repository. Versions follow semantic versioning. Prior versions are superseded upon release of the next.

## [1.1.0] - 2026-07-13

### Added
- INSTRUCTIONS.md: instruction block v1.1.0 with a ten-item acceptance checklist
- CROSSWALK.md: mapping to EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005, with a dated regulatory-currency note reflecting the 2026 Digital Omnibus on AI
- BUILD-GUIDE.md: the build log, split out of the README, corrected and updated
- CHANGELOG.md and LICENSE.md (CC BY-NC-SA 4.0)
- Ecosystem section linking the profile repository's canonical ECOSYSTEM.md and nearest-neighbor repositories

### Changed
- README.md rewritten: overview, audience, outputs, quickstart, file map, standards note, disclaimer, license
- Instruction block: added ISO/IEC 42005 alignment; added rule against reciting regulatory dates from memory; moved prohibited-use screen ahead of all scoring and added the NCII/CSAM prohibition; made the Threshold Gate deterministic (Consequence x Likelihood, worst domain governs); consolidated the v1 improvement round (evidence tags, system boundary, threat model, vendor controls, SLI/SLO monitoring, Decision Record, strictness modes) into the block itself; named the three doctrines and bound the DECISION step to Informed Intent; corrected NIST AI RMF function order to GOVERN, MAP, MEASURE, MANAGE
- Repository description made platform-agnostic (model choice noted as the reference implementation's, not a requirement)

### Fixed
- Grammatical and typographical errors in the build narrative ("The satisfaction condition should be whether", "You will likely be asked", "a GPT", "It finally completed")

### Superseded
- v1.0.0 README.md (single-file build log with embedded v1.0.0 prompt)

## [1.0.0] - initial release

- Single README.md containing the build narrative and the v1.0.0 instruction prompt

Final Liability rests with the Human.
