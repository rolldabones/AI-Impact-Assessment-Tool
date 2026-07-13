# CHANGELOG.md

All notable changes to this repository. Versions follow semantic versioning. Prior versions are superseded upon release of the next.

## [1.2.1] - 2026-07-13

### Changed
- INSTRUCTIONS.md deployed block mirrors two editorial edits made in the live GPT: capital L in both "Final Liability rests with the Human." closing lines, and the third doctrine label reverted from "Human accountability" to Final Liability (block now 7,599 characters; no behavioral change)
- README.md, BUILD-GUIDE.md and CROSSWALK.md versions aligned to 1.2.1

### Superseded
- v1.2.0 INSTRUCTIONS.md block

## [1.2.0] - 2026-07-13

### Added
- SPEC.md: normative long-form operating specification, adopted from the deployed Assistant's self-proposed revision after correction of eight defects (D-1 to D-8)
- Six operating modes, including test modes barring invented systems and facts during self-tests
- Residual-risk rule (planned / implemented-unverified / implemented-verified), five-outcome decision taxonomy, conditions precedent vs subsequent, twelve-role RACI with "Unassigned - decision blocker", non-blocking strictness default, final self-conformance check
- Builder Conformance Checklist in INSTRUCTIONS.md (tests the Assistant; distinct from the in-block System Acceptance Checklist, which tests the assessed system)

### Changed
- Instruction block compressed to 7,985 characters (the Assistant's draft ran roughly 14,000, over the 8,000-character field limit)
- Doctrine name and closing line restored to canon: "Final Liability rests with the Human."
- Configurator Mode specified (declared but undefined in the draft)
- Threshold clause on impossible score products replaced: the bands 1-6 / 8-12 / 15-25 are exhaustive over achievable products of a 1-5 x 1-5 scale
- Restored from v1.1.0: on-request framework crosswalk; provenance and watermarking coverage for generative AI
- README.md, BUILD-GUIDE.md (new Phase 5) and CROSSWALK.md bumped in lockstep

### Superseded
- v1.1.0 instruction block and acceptance checklist

## [1.2.1] - 2026-07-13

### Changed
- INSTRUCTIONS.md deployed block mirrors two editorial edits made in the live GPT: capital L in both "Final Liability rests with the Human." closing lines, and the third doctrine label reverted from "Human accountability" to Final Liability (block now 7,599 characters; no behavioral change)
- README.md, BUILD-GUIDE.md and CROSSWALK.md versions aligned to 1.2.1

### Superseded
- v1.2.0 INSTRUCTIONS.md block

## [1.2.0] - 2026-07-13

### Added
- INSTRUCTIONS-EXTENDED.md: uncompressed long form retained for platforms without the Instructions box limit

### Changed
- INSTRUCTIONS.md now carries the deployed production block verbatim (7,604 characters, compressed for the GPT builder): adds the residual-risk evidence rule (planned controls do not reduce residual risk), a five-value decision taxonomy with conditions precedent vs subsequent, MODE declaration across six modes, default strictness (risk-averse enterprise), precise four-status evidence definitions, expanded RACI with "Unassigned: decision blocker" and a pre-output self-check
- Ten-item checklist split into two instruments: the Assistant's in-tool acceptance checklist (rates the assessed system) and the repo-side operator verification checklist (verifies the Assistant)
- README.md and BUILD-GUIDE.md updated for the two-file instruction structure and compression step
- CROSSWALK.md version aligned to 1.2.0 (content unchanged)

### Superseded
- v1.1.0 INSTRUCTIONS.md (long-form block as canonical)

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
