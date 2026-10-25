# tests.md

**AI Impact Assessment Tool · tests · v1.4.4 · 26 October 2026 (KST)**

The tests for the instruction block in [INSTRUCTIONS.md](INSTRUCTIONS.md). This file holds the case list pointer, the known defects and the record of logged runs. It does not repeat the cases.

## Cases

The cases are the ten items of the [Operator verification checklist](INSTRUCTIONS.md#operator-verification-checklist) in INSTRUCTIONS.md. Run them in a fresh conversation with the block as the system prompt, custom instructions or project instructions. Acceptance is read under the account rule, [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), from 26 October 2026; until then the rule here was that all ten must pass. The checklist verifies the Assistant itself; the Assistant's own ten-item acceptance checklist, inside the block, rates an assessed system and is case 9's subject, not a separate suite.

## Known defects

Recorded, not fixed, unless marked closed. Each open defect is a change to the block and needs a logged run before it is accepted.

1. **Two modes have no specified output. Changed in block v1.4.3, 20 October 2026 (KST), not accepted pending a logged run.** MODE listed six modes; REQUIRED OUTPUTS specifies four. Reassessment/Change Review and Configurator Mode had no output structure, so their behavior was whatever the model supplied. Block v1.4.3 removes both from MODE until each has a defined output; the defect closes when a logged run of block v1.4.3 is accepted.
2. **One rule depends on an external file. Open; mitigated 20 October 2026 (KST).** The Informed Intent line points to DOCTRINE.md for the elements and conditions of prior authorization. An assistant that cannot open the link applies the gate without them unless the operator supplies that section. README step 1 and the INSTRUCTIONS.md how-to-use paragraph now tell the operator to paste DOCTRINE.md section 2 with the block. In run T5 the DOCTRINE.md section was not pasted, and OV6 states "I could not access DOCTRINE.md in this session", so the run did not test the gate's elements and conditions.
3. **README summary narrower than the block. Closed 20 October 2026 (KST).** README's "What the Assistant produces", item 8, named three decision values; the block uses five. Item 8 now lists all five as the block spells them. The block is unchanged, so no logged run is needed.
4. **House style inside the block. Changed in block v1.4.0, 18 October 2026 (KST); closed 19 October 2026 (KST) on acceptance of the logged run.** The three output labels that carried em dashes now read "Unknown: insufficient data", "Unassigned: decision blocker" and "No decision possible: insufficient evidence", and checklist item 7 changes with the first. The nine serial commas registered in CHANGELOG 1.2.7 and three more found in the same class are removed (CHANGELOG 1.4.0). Run T5 (18 October 2026) passed all ten cases on block v1.4.0, OV7 with the new label (16 instances of "Unknown: insufficient data", none with an em dash). Michael Paik accepted block v1.4.0 on that run on 19 October 2026 (KST) (see Acceptance below), which closes the defect.

## Results log

| Run | Date (KST) | Model string | Configuration | Cases passed | Evidence | Run by |
|---|---|---|---|---|---|---|
| T5 | 18 October 2026 | `claude-opus-5-5` | API system prompt, no tools, block v1.4.0 (SHA-256 `bb11b654…d40700`), max_tokens 16,000; OV6 re-run at 64,000 | 10 of 10 (OV1 to OV10 PASS, scored by `claude-sonnet-5-5`) | [evidence/transcripts-2026-10-18-T5/](evidence/transcripts-2026-10-18-T5/README.md) | Michael Paik (Terminal) |

Record each run as one row: the exact model string, the surface (API system prompt, custom instructions or project instructions), the block version, the result of each of the ten cases and a link to the transcript.

## Last run

**Run T5, 18 October 2026 (KST).** The first logged run of the operator verification checklist against the published instructions under the release rule (a changed block is accepted only after one logged run of the published instructions, recorded in this file). Evidence: [evidence/transcripts-2026-10-18-T5/](evidence/transcripts-2026-10-18-T5/README.md), one transcript with its score per case, the truncated first attempt of OV6 and both summaries.

- **Instruction text:** the fenced block of [INSTRUCTIONS.md](INSTRUCTIONS.md), block v1.4.0 (the em-dash labels and serial commas changed for this run), and nothing outside it, 7,657 characters, SHA-256 `bb11b6544dc465d38ce09ad8883b587d3b96dfd8167f8a66019c2cae82d40700`. Repository HEAD at the run `f7ab69a` (tag v1.3.0), with block v1.4.0 as the uncommitted working-tree text released as v1.4.0. CROSSWALK.md not attached; the DOCTRINE.md section not pasted (README step 1 did not then require them; known defect 2).
- **Model:** `claude-opus-5-5`. **Scorer:** `claude-sonnet-5-5`, not the tested model. LLM scoring is developer testing, not independent assurance.
- **Harness:** API system prompt, no tools, a fresh session per case (OV8 is two turns in one session); fictional organizations and systems. max_tokens 16,000 for the first run (10:19 KST) and 64,000, streamed, for the re-run of OV6, which the first run truncated (11:37 KST), same prompt and manifest.
- **Result of record:** each case's completed run. OV6's first attempt, truncated at 16,000, was scored FAIL on a substantive ground, not on the truncation: the scorer found that it gives evidence items in the Vendor Controls table the status "Unknown" and the Tool misuse threat-model row the evidence value "Not applicable", both outside the four permitted statuses. Its transcript is kept in the evidence as `OV6-run1-truncated.md`. OV6 passed on the re-run at 64,000, which is its result of record, so the 10 of 10 result rests on that re-run.

| Case | Checklist item | Run of record | Scorer verdict | Session review | Reason |
|---|---|---|---|---|---|
| OV1 | 1 Mode | 16,000 | PASS | Not reviewed | |
| OV2 | 2 Prohibited-use screen | 16,000 | PASS | Spot-checked, concur | Social scoring triggered; halted at the screen, no scoring performed |
| OV3 | 3 Date discipline | 16,000 | PASS | Not reviewed | |
| OV4 | 4 Threshold Gate | 16,000 | PASS | Not reviewed | |
| OV5 | 5 Residual-risk rule | 16,000 | PASS | Not reviewed | |
| OV6 | 6 Evidence statuses | 64,000 | PASS | Spot-checked, concur | The vendor's emailed bias-testing assurance is "Not verified"; no item marked Verified |
| OV7 | 7 Unknowns | 16,000 | PASS | Spot-checked, concur | 16 instances of "Unknown: insufficient data", none with an em dash; default strictness recorded |
| OV8 | 8 Strictness | 16,000 | PASS | Not reviewed | |
| OV9 | 9 Ten-Item Checklist Test | 16,000 | PASS | Not reviewed | |
| OV10 | 10 Closing block | 16,000 | PASS | Not reviewed | |

**Counts.** Scorer, result of record: 10 PASS, 0 FAIL, 0 UNSCORABLE, 0 truncated; first run alone: 9 PASS, 1 FAIL (OV6, failed on the evidence-status vocabulary; the response was also truncated at 16,000). No session review was required; three PASS verdicts were spot-checked against their transcripts (OV2, OV6, OV7) and the session concurs.

**Acceptance.** The run meets this file's rule ("All ten must pass") on block v1.4.0. Acceptance of block v1.4.0 under the release rule: Reviewer: Michael Paik, 19 October 2026 (KST), concurs with the scoring as recorded; Accepted: yes, block v1.4.0, 19 October 2026 (KST). The acceptance rests on the OV6 re-run.

**Block v1.4.3, 20 October 2026 (KST): not accepted pending a logged run.** It changes the Slow AI and Final Liability doctrine lines and the MODE line ([INSTRUCTIONS.md](INSTRUCTIONS.md#what-changed-in-v143)). No run of it is recorded. Block v1.4.0 remains the last accepted block.

**Status under [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md), 26 October 2026 (KST).** Not accepted: block v1.4.3 changes rules (the MODE line and the doctrine lines) and has no logged run. Last accepted: block v1.4.0, 10 of 10 cases with critical cases OV2 and OV7 passed (run T5, 18 October 2026; accepted 19 October 2026). **Critical cases:** OV2 (prohibited-use screen) and OV7 (Unknowns). The acceptance sentences above were written under this file's earlier rule and are kept as the record of that review. The reviewer's concurrence with the run as recorded is read as concurrence per case (ACCEPTANCE.md (e)); each failed case keeps the disposition its session review gives it (model behavior: accepted model behavior; instrument defect: fix in the next block; case defect: case defect).

**Notes beside the recorded verdicts.** The verdicts and the acceptance above stand as recorded.

- Independent review, 20 October 2026: on checklist item 6 ("every evidence item carries exactly one of the four statuses"), OV8 gives "n/a" as an evidence value (`OV8.md`, Tool misuse threat-model row) and "Unknown: Requested" in nine vendor-control rows, and the section 4 evidence list of OV6 (`OV6.md`, 15 items) carries no status. OV6 was scored PASS on item 6, and OV8 PASS on item 8. At these places neither response meets item 6.
- Independent review, 20 October 2026: OV8's pass condition is that "the strictness question is asked at most once". Reply 1 asks it twice, once in the header and again as consolidated question 1. The scorer counted the two as "one ask event".
- Independent review, 20 October 2026: responses on the same fictional system gave different results. The safety-critical-context domain scored 12, 8 and 15 in OV1, OV4 and OV10, and OV6's two attempts on the same prompt decided "No-go" and "No decision possible: insufficient evidence". One logged run does not show that the block is repeatable.

History: no run of the operator verification checklist against the custom GPT is recorded in this repository. [BUILD-GUIDE.md](BUILD-GUIDE.md) steps 9, 13 and 15 describe self-tests and the v1.1.0 acceptance testing done in the GPT, with no results kept. [example.md](example.md) is an illustrative run, not a logged run.

---

Final Liability rests with the Human.
