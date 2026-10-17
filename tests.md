# tests.md

**AI Impact Assessment Tool · tests · v1.3.0 · 18 October 2026 (KST)**

The tests for the instruction block in [INSTRUCTIONS.md](INSTRUCTIONS.md). This file holds the case list pointer, the known defects and the record of logged runs. It does not repeat the cases.

## Cases

The cases are the ten items of the [Operator verification checklist](INSTRUCTIONS.md#operator-verification-checklist) in INSTRUCTIONS.md. Run them in a fresh conversation with the block as the system prompt, custom instructions or project instructions. All ten must pass. The checklist verifies the Assistant itself; the Assistant's own ten-item acceptance checklist, inside the block, rates an assessed system and is case 9's subject, not a separate suite.

## Known defects

Recorded, not fixed. Each is a change to the block and needs a logged run before it is accepted.

1. **Two modes have no specified output.** MODE lists six modes; REQUIRED OUTPUTS specifies four. Reassessment/Change Review and Configurator Mode have no output structure, so their behavior is whatever the model supplies.
2. **One rule depends on an external file.** The Informed Intent line points to DOCTRINE.md for the elements and conditions of prior authorization. An assistant that cannot open the link applies the gate without them unless the operator supplies that section.
3. **README summary narrower than the block.** README's "What the Assistant produces", item 8, names three decision values; the block uses five.
4. **House style inside the block.** Three output labels carry em dashes ("Unknown—insufficient data", "Unassigned—decision blocker", "No decision possible—insufficient evidence") and nine lists carry serial commas (registered in CHANGELOG 1.2.7). Checklist item 7 tests the first label verbatim, so the labels and the checklist would change together.

## Results log

| Run | Date (KST) | Model string | Configuration | Cases passed | Evidence | Run by |
|---|---|---|---|---|---|---|
| None yet | | | | | | |

Record each run as one row: the exact model string, the surface (API system prompt, custom instructions or project instructions), the block version, the result of each of the ten cases and a link to the transcript.

## Last run

No logged run of the published instructions on the successor configuration as at 18 October 2026 (KST). Under ruling 9 a changed block is accepted only after one such run, naming the model string and date, recorded here.

History: no run of the operator verification checklist against the custom GPT is recorded in this repository. [BUILD-GUIDE.md](BUILD-GUIDE.md) steps 9, 13 and 15 describe self-tests and the v1.1.0 acceptance testing done in the GPT, with no results kept. [example.md](example.md) is an illustrative run, not a logged run.

---

Final Liability rests with the Human.
