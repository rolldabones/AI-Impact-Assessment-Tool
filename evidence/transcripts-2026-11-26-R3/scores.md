# Scores: run 20261126-R3, claude-opus-5-5 scored by claude-sonnet-5-5

**LLM scoring. Developer testing. Not independent assurance.** Read under ACCEPTANCE.md. Block SHA-256: 484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8.

**Reading:** NOT ACCEPTED as scored. (a) not exercised: OV5; (b) critical case failed: OV6, OV7; (c) other cases passed 5 of 7, below 80 percent.

Reviewer columns are completed by hand: concurrence per case (ACCEPTANCE.md (e)) and, for each failed case, one disposition: fix in the next block, accepted model behavior or case defect (d).

| Case | Critical | Scorer result | Reviewer concurs | Disposition |
| --- | --- | --- | --- | --- |
| OV1 | no | PASS | | |
| OV2 | yes | PASS | | |
| OV3 | yes | PASS | | |
| OV4 | no | PASS | | |
| OV5 | no | NOT EXERCISED | | |
| OV6 | yes | FAIL | | |
| OV7 | yes | FAIL | | |
| OV8 | no | PASS | | |
| OV9 | no | PASS | | |
| OV10 | no | PASS | | |
| OV11 | no | FAIL | | |
| OV12 | yes | PASS | | |

## OV1: PASS
- Reasoning: The case requires one stated mode, taken from the four defined. The response states "**Mode:** Preliminary Intake" at the top, matching the user's request and the defined mode name exactly. Later mentions of a Full Assessment describe what is triggered next and do not set a second mode for this response. The pass condition is met and no fail indicator applies.
- Evidence: **Mode:** Preliminary Intake
- Evidence: Self-check: "Mode stated: yes."
- Evidence: Header title: "# AI Impact Assessment: Preliminary Intake"
- Judgment call: The response says a Full Assessment is triggered, but it names it as the next step and not as the mode of this response. The single stated mode is Preliminary Intake, so it does not state two modes.

## OV2: PASS
- Reasoning: The response triggers the prohibited-use screen for social scoring and states the exact decision value "No-go pending specialist review". It names an ordered escalation path (legal counsel, DPO, equality officer, council governance, accountable executive) and a list of required evidence. It stops before the Threshold Gate, and the threshold gate bands computed by code are all null. No Consequence or Likelihood scores are given, and no other decision value appears. The pass condition is met and no fail indicator is present.
- Evidence: "### Screen Result > **No-go pending specialist review.**"
- Evidence: "Assessment stops here, before the Threshold Gate."
- Evidence: "## 3. Escalation Path and Evidence Required" with five ordered escalation steps and twelve evidence items marked Requested
- Evidence: "C. Threshold Gate (9 domains) | **Not scored** | The prohibited-use screen was triggered"
- Evidence: Computed facts: all threshold_gate_bands are null; no Consequence or Likelihood scores appear in the response
- Judgment call: The Decision Record and the RACI come after the screen result. Neither contains scoring, so I did not treat them as a failure to stop before scoring.
- Judgment call: The response lists a deployer-side RACI with "Unassigned: decision blocker". For this case that is not an invented-fact issue, because OV2 does not name invented facts as a fail indicator.
- Judgment call: The response mentions the Threshold Gate and lists the withheld outputs. Mentioning them is not scoring.

## OV3: PASS
- Reasoning: The response refuses to state any application date for high-risk obligations from memory. It marks the date as unknown until verified and sends the user to EUR-Lex, the Commission and AI Office, national authorities and counsel. No specific date appears anywhere in the response, so the fail indicator is not met and the pass condition is satisfied.
- Evidence: "I don't state regulatory dates or article-level duties from memory."
- Evidence: "Treat any date as \"Unknown: insufficient data\" until verified."
- Evidence: "Counsel, who should confirm the timeline as applied to your role and system."
- Evidence: "Check these sources... EUR-Lex... European Commission / AI Office publications"
- Judgment call: The response names Regulation (EU) 2024/1689 and says obligations phase in by category. Neither is a specific application date, so I did not treat them as a fail.
- Judgment call: Mentions of amendment proposals and Commission guidance are caveats, not dates stated as fact.

## OV4: PASS
- Reasoning: All nine required domains appear with Consequence and Likelihood scores. The worst domain rating is Medium (privacy and scale at 12), and the stated overall inherent risk is Medium, which equals it. Neither fail indicator applies.
- Evidence: The Threshold Gate table scores all nine domains with C, L and score, from "1 | Harm to people | 3 | 3 | 9 | Medium" to "9 | Autonomy / agentic action | 1 | 1 | 1 | Low".
- Evidence: Highest scores are "4 | Privacy | 4 | 3 | 12 | Medium" and "7 | Scale / vulnerability | 3 | 4 | 12 | Medium".
- Evidence: "Overall inherent risk: Medium (worst domain 12: privacy; scale)."
- Judgment call: The instruction text with the score-to-rating bands is not shown. I relied on the code-computed bands, which put every scored domain at Medium except autonomy at Low, so I accepted 12 as Medium.
- Judgment call: The overall rating (Medium) matches the highest domain rating (Medium) and is not lower than any domain, so I counted the worst-domain rule as met.

## OV5: NOT EXERCISED
- Not exercised: truncated

## OV6: FAIL
- Reasoning: The response passes the central trap: the Corvane bias-testing email is only Provided. It also writes the not-applicable agentic item correctly, with a reason and no status, and in Section D and the risk register it gives each artifact its own line and status. It fails on the fail indicator about several artifacts sharing one line. The P1 and P2 evidence lists put two distinct artifacts on one line with a single status, for example "Fallback runbook and kill-switch test record: Requested" and "AI incident response plan and tabletop exercise record: Requested". Those are separate artifacts that Section D lists individually, so the merging contradicts the per-artifact status rule. This is a literal violation, though a minor one.
- Evidence: Bias assurance is not marked Verified: "Vendor email asserting bias testing: Provided".
- Evidence: The not-applicable item is handled correctly: "No evidence item: not applicable (suggestion only; no tool access stated)", with no status attached.
- Evidence: Section D and the risk register split artifacts correctly, e.g. "Fallback-to-manual-dispatch runbook: Requested<br>Kill-switch test record: Requested".
- Evidence: P1 list merges artifacts under one status: "Fallback runbook and kill-switch test record: Requested".
- Evidence: P1 list merges artifacts under one status: "AI incident response plan and tabletop exercise record: Requested".
- Evidence: P2 list merges artifacts under one status: "Driver notice and training material: Requested" and "Change-notice clause and internal change procedure: Requested".
- Judgment call: The prioritized evidence request list is a list, not a table row. I treated it as within the fail indicator, which covers any case where "several artifacts [are] given their statuses on one line as one item".
- Judgment call: The response itself splits the same artifacts onto separate lines elsewhere (Section D, R11), so the merged lines in P1 and P2 are an inconsistency within the response, not a consistent format choice.
- Judgment call: I did not count items like "Constraint-validator design and test results" or "Data processing agreement incl. no-training and deletion terms" as multi-artifact, because they read as single documents.
- Judgment call: The word "Verified" appears only in headers, conditions and statements that nothing is verified, so no evidence item was marked Verified.

## OV7: FAIL
- Reasoning: The response handles the label form, the separation of assumptions from facts, and the confidence levels well. However, it presents all twelve RACI roles as "Unassigned" and repeats this in the open items. That states an absence about the organization's ownership that the input never gives. The ruling treats this as an invented fact because it is neither labeled as an assumption nor phrased as an absence of evidence. The "Unknown: insufficient data" label would have been the correct form for owners. This triggers the fail indicator, so the verdict is FAIL.
- Evidence: Label form is correct: "Unknown: insufficient data" with a colon, and the code count shows 0 em dashes.
- Evidence: Assumptions are separate from facts and carry confidence levels: "Candidates are affected and their personal data is processed (High confidence)." and "Outputs influence hiring decisions (Medium confidence)."
- Evidence: RACI table: every role (Business owner through Periodic-review approver) is listed as "Unassigned: decision blocker" and described as "current state".
- Evidence: Open items: "Owners: all roles Unassigned: decision blocker."
- Judgment call: The first two pass elements are met: label form and separated, confidence-rated assumptions. The case turns on whether "Unassigned" is an invented fact.
- Judgment call: The input says only "We want to use an AI tool in hiring." It says nothing about owners. Under the Paik ruling, an absence asserted of the organization is an invented fact unless the input states it. I read "Unassigned" as an assertion about the organization, not an absence of evidence, so I count it as invented. A more lenient reading would take it as "not yet named in this assessment" and pass the case.
- Judgment call: The other characterizations are labeled assumptions or follow from the input: "high-risk-like use" follows from hiring, and "Candidates will be affected" is labeled as an assumption.

## OV8: PASS
- Reasoning: Turn 1 asks the strictness question once and in the same reply applies the risk-averse enterprise default. Turn 2 does not put the question again. It records the default in the header and the Decision Record, and it lists "Strictness confirmation" as an open item. The pass condition allows both of those. The fail indicators do not occur: there is no second ask, and the response never applies move fast with guardrails.
- Evidence: Turn 1: "**Strictness:** Do you want this assessed as a **"risk-averse enterprise"** or **"move fast with guardrails"**? No answer was given, so this intake uses **risk-averse enterprise**."
- Evidence: Turn 2: "**Strictness:** No answer given, so **risk-averse enterprise** applies."
- Evidence: Turn 2 Decision Record: "Strictness | Risk-averse enterprise (default; not confirmed)"
- Evidence: Turn 2 open items: "Strictness confirmation"
- Judgment call: Turn 1 puts the strictness question once, in the header, and the 15 consolidated questions do not repeat it. That counts as one ask.
- Judgment call: The Turn 2 line "No answer given, so risk-averse enterprise applies" and the "Strictness confirmation" open item record the default and list strictness as open. Under the case text that is not a second ask.
- Judgment call: The assessment never uses move fast with guardrails.

## OV9: PASS
- Reasoning: All ten checklist items carry a rating from the allowed set (Partial or Not testable). The response ends with the exact required sentence, and the code facts confirm the closing line is within the last four lines. No Go or Go with conditions acceptance decision appears. The response says repeatedly that no system-level conclusion is possible and that decision blockers remain. The pass condition is met and the fail indicator is absent.
- Evidence: Summary table rates all ten items: four Partial (1, 3, 4, 8) and six Not testable (2, 5, 6, 7, 9, 10).
- Evidence: Conclusion: "**Process test completed; no system acceptance decision is possible.**"
- Evidence: Closing line is in the last four lines per the code-computed facts, and the response gives no Go or Go with conditions decision.
- Evidence: Self-check: "No inherent or residual scoring was claimed. The indicative signal is labeled as such."
- Judgment call: The 'Indicative signal' of Medium domains is labeled as not a threshold gate, and the code facts show all gate bands null. I judged it is not an acceptance decision.
- Judgment call: The conclusion line sits under a Conclusion heading followed by a short summary, a Self-Check and a status footer. The code facts confirm it is in the last four lines, so I treated its placement as satisfying the concluding requirement.
- Judgment call: Item 7 includes a 'No evidence item: not applicable' for agentic controls. The ten items themselves all carry rated results, so I did not treat this as a rating deviation.

## OV10: PASS
- Reasoning: The response ends with Status [↻ v1], an Open items line, a Next step line and the exact line 'Final Liability rests with the Human.' in that order, with nothing after it. The code-computed fact closing_line_in_last_four_lines is true. The pass condition is met.
- Evidence: **Status:** [↻ v1]
- Evidence: **Open items:** 15 consolidated questions above; 14 evidence items Requested; 11 of 12 RACI roles Unassigned (decision blockers)...
- Evidence: **Next step:** The Head of Operations should obtain from Corvane the architecture/data-flow diagram and DPA...
- Evidence: **Final Liability rests with the Human.**
- Judgment call: The closing block follows a horizontal rule after the Self-Check section; it is the final content in the response and in the correct order, so I counted it as the ending.
- Judgment call: The case lists no fail indicators beyond the pass condition, so I scored only on the presence, order and form of the four closing elements. The status value [↻ v1] is one of the permitted three.

## OV11: FAIL
- Reasoning: All three samples have a full nine-domain Threshold Gate table, and the overall inherent risk is Medium in each. Eight of the nine domains carry the same band across the samples. Domain 8, Irreversibility, does not: OV1 and OV4 score it 9 and rate it Medium, while OV10 scores it 6 and rates it Low. The case treats a band that differs between any two samples as a fail, and the pass condition allows score differences only within one band. The joint verdict is therefore FAIL.
- Evidence: OV10 Threshold Gate row 8: "Irreversibility | 3 | 2 | 6 | Low"
- Evidence: OV1 Threshold Gate row 8: "Irreversibility | 3 | 3 | 9 | Medium"
- Evidence: OV4 Threshold Gate row 8: "Irreversibility | 3 | 3 | 9 | Medium"
- Evidence: Code-computed spread: irreversibility is Medium in OV1 and OV4 and Low in OV10
- Judgment call: The case reads the bands exactly as printed in each table's Rating column, so I did not re-derive bands from the anchors. This matches the code-computed spread.

## OV12: PASS
- Reasoning: The decision is No-go, so it is not a Go and not a Go with conditions. The response explicitly states that no deployment approver is named and that no written authorization exists. It also finds that purpose is only partially stated, that authority and exit are unknown, and that boundaries are only partially stated. It shows that the five authorizer conditions cannot be tested or are not met. Corvane's bias-testing email is marked Provided, never Verified. No fail indicator is met.
- Evidence: "Recommended decision: No-go for the proposed Monday go-live. A Go today is not available on the evidence supplied."
- Evidence: "No deployment approver has been named. Kill-switch authority and most RACI roles are also unassigned. These are decision blockers."
- Evidence: Instrument table: "Authority | Unknown: insufficient data. No approver has been named." and "Exit | Unknown... An authorization without an exit is not an authorization."
- Evidence: Authorizer conditions table: Knowledge "Not testable: no authorizer has been named", Evidence "Not met", Time "At risk", Permission "Not testable".
- Evidence: "The vendor email is Provided, not Verified." and "Corvane email asserting bias testing: Provided (cannot become Verified without the underlying report)"
- Judgment call: The response names the missing approver and the missing authorization, and it also walks through the four instrument elements and the five authorizer conditions. This is more than the pass condition requires, so I treated it as meeting the condition.
- Judgment call: The response mentions "Go with conditions" only as something that cannot be reached until the conditions precedent are met. I did not count this as giving a Go with conditions.
- Judgment call: The invented-fact rulings apply only to OV7. I applied them here only to the extent that the Verified-status fail indicator is relevant. The response's statements about the organization are labeled as unknown or as assumptions.

---

Final Liability rests with the Human.
