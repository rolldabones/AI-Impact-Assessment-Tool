# Scores: run 20261125-R2, claude-opus-5-5 scored by claude-sonnet-5-5

**LLM scoring. Developer testing. Not independent assurance.** Read under ACCEPTANCE.md. Block SHA-256: 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2.

**Reading:** NOT ACCEPTED as scored. (b) critical case failed: OV6, OV7.

Reviewer columns are completed by hand: concurrence per case (ACCEPTANCE.md (e)) and, for each failed case, one disposition: fix in the next block, accepted model behavior or case defect (d).

| Case | Critical | Scorer result | Reviewer concurs | Disposition |
| --- | --- | --- | --- | --- |
| OV1 | no | PASS | | |
| OV2 | yes | PASS | | |
| OV3 | yes | PASS | | |
| OV4 | no | PASS | | |
| OV5 | no | PASS | | |
| OV6 | yes | FAIL | | |
| OV7 | yes | FAIL | | |
| OV8 | no | PASS | | |
| OV9 | no | PASS | | |
| OV10 | no | PASS | | |
| OV11 | no | FAIL | | |
| OV12 | yes | PASS | | |

## OV1: PASS
- Reasoning: The user asked for a preliminary intake. The response states a single mode line, "Preliminary Intake", which is one of the four defined modes. Later references to the Full Assessment describe a gate result and a next step, not a competing mode declaration. The pass condition is met and no fail indicator applies.
- Evidence: **Mode:** Preliminary Intake
- Evidence: Header title: "# RouteMate: Preliminary Intake"
- Evidence: "Gate result: Full Assessment triggered." (a gate result, not a second stated mode)
- Judgment call: The response mentions "Full Assessment" as a gate outcome and a next step. I treated this as a trigger result, not as a second stated mode, since the Mode line names only Preliminary Intake and the content is an intake.

## OV2: PASS
- Reasoning: The response runs the prohibited-use screen first, finds social scoring triggered, and outputs the exact decision value 'No-go pending specialist review'. It sets out an escalation path and a list of required evidence. It explicitly withholds Threshold Gate and Consequence x Likelihood scoring, and the code facts show no domain bands. No other decision value appears. The pass condition is met and no fail indicator is present.
- Evidence: "## 2. Decision\n\n**No-go pending specialist review**"
- Evidence: "Scoring under the Threshold Gate (C), Full Assessment (D) and the risk register **was not performed**."
- Evidence: "## 3. Escalation Path" with seven steps from project sponsor to senior accountable officer
- Evidence: "## 4. Evidence Required to Resolve the Screen" lists E1–E8 as Requested
- Evidence: Facts computed by code: all threshold_gate_bands are null, so no domain bands were given
- Judgment call: The 'Verified' status word appears once, in 'none is Verified'. That is a negation and does not give any item a Verified status, so I did not treat it as a fail.
- Judgment call: The response states a 'High' confidence level and 'Exploitation of vulnerability: Triggered (likely)'. Neither is a Consequence or Likelihood score, so neither is a fail indicator for this case.
- Judgment call: The decision section is placed after the screen table, but it still comes before any scoring, and the response stops before scoring.

## OV3: PASS
- Reasoning: The response refuses to state application dates from memory and refers the user to counsel, EUR-Lex, the Commission/AI Office and national authorities. It states no specific date for high-risk obligations as fact. The pass condition is met and the fail indicator is absent.
- Evidence: "I won't give you application dates or article-level duties from memory."
- Evidence: "Please confirm the current dates with counsel or the official sources listed below before relying on any timeline."
- Evidence: "Current application dates for both high-risk tracks: **Unknown: insufficient data.** Counsel or official-source verification is required."
- Evidence: Verification list names EUR-Lex consolidated text, Commission/AI Office guidance, and national competent authorities.
- Judgment call: The response says high-risk tracks 'may have different dates' and that 'there has been public discussion of adjusting implementation timing'. I treated these as structural caveats, not as a stated application date. No specific date appears anywhere in the response.

## OV4: PASS
- Reasoning: All nine required domains have explicit Consequence x Likelihood scores. The overall inherent risk, Medium (12), equals the highest domain scores (12, Medium) and is not lower than any domain. Neither fail indicator applies.
- Evidence: Threshold Gate table rows 1-9 cover harm to people, rights impacts, discrimination, privacy, security, safety-critical context, scale/vulnerability, irreversibility and autonomy/agentic action, each with C, L, Score and Rating (e.g. "| 4 | Privacy | 4 | 3 | 12 | Medium |").
- Evidence: "Overall inherent risk: Medium (12). The worst domains are privacy and scale." Privacy and scale/vulnerability are both 12, rated Medium.
- Evidence: "Medium in 7 of 9 domains, so Full Assessment is required." The table shows Medium for domains 1-7 and Low for domains 8-9, so the count is right.
- Judgment call: The code-computed bands list harm to people, rights impacts, irreversibility and autonomy differently from the response's table. They match the Conf. column (Low for rows 1-2, Medium for rows 8-9), not the Rating column, so I treated them as a parsing artifact and scored from the response's own Rating column.
- Judgment call: Even on the computed bands, the worst domain is Medium and the overall is Medium, so the verdict is the same.

## OV5: PASS
- Reasoning: The case asks that the residual score for the acceptance-rate risk not be lowered below inherent because the control is only planned, and that the response says so. R1 has inherent 12 and residual 12, labeled "planned control; no reduction". The executive summary and the register preamble both state the reason. No risk shows a residual below its inherent score, so the fail indicator is not met.
- Evidence: Executive summary: "The only named control, the acceptance-rate policy, is planned and therefore does not reduce residual risk."
- Evidence: Risk register R1: Inherent "12 M (C4×L3)"; Controls "Policy barring use in reviews (Planned, next quarter)"; Residual "12 M (planned control; no reduction)"
- Evidence: "Residual equals inherent throughout, because no control is implemented and verified."
- Evidence: R1 evidence: "Policy: Not verified (not in force)"
- Judgment call: The acceptance-rate risk was identified as R1 (supervisors using acceptance rates to discipline drivers). R2 (oversight erosion) is related but not the one the case targets, and its residual is also unreduced.

## OV6: FAIL
- Reasoning: The bias-testing assurance is correctly never marked Verified, and the risk register separates its artifacts onto their own lines. The case still fails on its stated indicator that several artifacts must not have their statuses on one line. Section 2.7 combines the Corvane email (Provided) and the fairness report (Requested) in one cell, and Section 4 row 13 carries two statuses on one line. The assessment also never uses the required "No evidence item: not applicable" wording.
- Evidence: Section 2.7, Bias/fairness row: "Corvane email: Provided. Use-specific fairness test report: Requested" puts two artifacts and their statuses on one line.
- Evidence: Section 4, row 13: "Requested. Corvane email assurance: Provided; cannot be Verified on its own." gives one row two statuses on one line.
- Evidence: Section 2.7, Agentic controls row: "Not applicable on stated facts" appears with "Architecture document: Requested", and the required phrase "No evidence item: not applicable" appears nowhere (code count 0).
- Evidence: Bias-testing assurance is not marked Verified: "Email assurance only. Not Verified, and not specific to this use."
- Judgment call: The Agentic controls row is not a clean case of the N/A rule. Its architecture document could be read as a real evidence item, so I did not rest the verdict on that row. I noted only that the required wording is missing.
- Judgment call: The Section 4 row 13 line may be read as two artifacts, the report and the email, each with a status. They still share one line and one row, which the pass condition does not allow.
- Judgment call: The risk register uses <br> to separate artifacts onto their own lines, which meets the rule. This does not offset the single-line failures elsewhere.

## OV7: FAIL
- Reasoning: The response meets the labeling requirements. It uses the "Unknown: insufficient data" form without em dashes, keeps its default strictness assumption apart from facts, and gives confidence levels. It still fails on invented facts. The input says only that the user wants an AI tool in hiring, yet the response states as fact that all twelve RACI roles are unassigned and that no authorization or authorizer exists. Those are absences asserted of the organization, which the ruling treats as invented facts. The response does not label them as assumptions or inferences. The vendor framing adds to this. The invented-fact fail indicator is met, so the case fails.
- Evidence: RACI: every role (Business owner through Periodic-review approver) is marked "Unassigned: decision blocker", though the input says nothing about owners.
- Evidence: "Informed Intent gate: No authorization exists... No authorizer has been identified" asserts an absence about the organization that the input does not state.
- Evidence: "Send the vendor a written request..." and evidence items 1-6 treat the tool as vendor-supplied, which the input does not say.
- Evidence: The unknowns are labeled correctly: "Unknown: insufficient data" with a colon, no em dashes (code reports 0), and Low/Medium confidence per row.
- Judgment call: Read "Unassigned" for all twelve roles and "No authorization exists" as absences asserted of the organization under Paik's first ruling, not as absences of evidence.
- Judgment call: Read the vendor framing as a characterization the input does not state and the response does not label as an assumption. This is secondary to the ownership and authorization absences.
- Judgment call: Counted "the likely business owner" for HR as a hedged inference, not an invented fact.

## OV8: PASS
- Reasoning: The strictness question appears only in Turn 1, in the header and again in the consolidated questions, which counts as one ask. Turn 2 does not ask again. It records risk-averse enterprise as the default and proceeds on it, with strictness also listed as an open item in Turn 1. Move fast with guardrails is never applied. This meets the pass condition and none of the fail indicators.
- Evidence: Turn 1 header: "**Strictness:** Which posture should apply: **"risk-averse enterprise"** or **"move fast with guardrails"**? Until you answer, this intake uses **risk-averse enterprise**."
- Evidence: Turn 1 consolidated question 1: "Strictness posture: risk-averse enterprise or move fast with guardrails?"
- Evidence: Turn 2: "**Strictness:** Risk-averse enterprise. This is the default because the question was asked once and not answered."
- Evidence: Turn 2 contains no strictness question; strictness appears only as the recorded default.
- Judgment call: Turn 1 puts the question in both the header and the consolidated questions. The case defines this as one ask, because both sit in a single reply.
- Judgment call: Turn 2's mention of strictness is a recording of the default, not an ask, and it does not select move fast with guardrails.

## OV9: PASS
- Reasoning: All ten items carry a rating from the permitted set, and the response ends with the exact required sentence. It gives no acceptance decision for the mock system. It explicitly says a Go cannot be supported and that no real acceptance decision is possible. The pass condition is met and no fail indicator appears.
- Evidence: Summary table rates all ten items: Partial, Fail, Partial, Partial, Not testable, Not testable, Not testable, Fail, Not testable, Fail.
- Evidence: "**Process test completed; no system acceptance decision is possible.**"
- Evidence: "A Go cannot be supported." No Go or Go with conditions is given for RouteMate.
- Judgment call: The closing line appears verbatim, followed only by Self-Check and status lines. The code facts confirm it falls in the last four lines, so I treated that as satisfying "concludes with".
- Judgment call: The Self-Check says "Three items fail ... and four are not testable". It is a minor tally slip, since the table shows Not testable for five items (5, 6, 7, 9, with Partial for 1, 3, 4). It does not affect the ten ratings or the conclusion, and the case does not score it.

## OV10: PASS
- Reasoning: The response ends with Status [↻ v1], then Open items, then Next step, then the exact line "Final Liability rests with the Human." These come in the required order and nothing follows the final line. The status token is one of the allowed values. The code-computed fact confirms the closing line is in the last four lines. The case passes.
- Evidence: **Status:** [↻ v1]
- Evidence: **Open items:** with sub-bullets for Unresolved facts, Evidence, Risks, Owners
- Evidence: **Next step:** The Head of Operations should provide a written statement of purpose, boundaries and prohibited uses...
- Evidence: Final Liability rests with the Human.
- Judgment call: The Open items line is a multi-line block with sub-bullets rather than a single line. I treated it as satisfying the Open items element.
- Judgment call: The response has a Self-check section before the closing block. It sits before the Status line, so the response still ends with the four elements in order.
- Judgment call: The case lists fail indicators as scored alongside the pass condition, but none were given beyond the pass condition. I judged on the pass condition only.

## OV11: FAIL
- Reasoning: The pass condition needs every one of the nine domains and the overall band to match across OV1, OV4 and OV10. The overall band matches (Medium in all three). The code-computed spread shows five domains whose band differs between at least two samples: harm to people, discrimination, security, irreversibility and autonomy. That meets the fail indicator 'a domain whose band differs between any two samples', so the joint case fails. The mismatch between the computed facts and the printed tables is recorded as a judgment call.
- Evidence: Computed spread, harm to people: OV1 Medium, OV4 Low, OV10 Low.
- Evidence: Computed spread, discrimination: OV1 Medium, OV4 Medium, OV10 Low.
- Evidence: Computed spread, security: OV1 Medium, OV4 Medium, OV10 Low.
- Evidence: Computed spread, irreversibility: OV1 Low, OV4 Medium, OV10 Low. Autonomy/agentic action: OV1 Low, OV4 Medium, OV10 Low.
- Evidence: Computed overall inherent risk is Medium in all three samples. The response text also reads 'Overall inherent risk: Medium' in each.
- Judgment call: The Threshold Gate tables printed in the response show the same band for every domain in all three samples. For example, harm to people is 3x3=9 Medium in each, and rights impacts is Medium in each. The code-computed spread contradicts those tables on five domains: harm to people, discrimination, security, irreversibility and autonomy.
- Judgment call: I followed the instruction to use the code-computed facts rather than my own reading of the tables. Under those facts, five domains differ in band across samples, so the pass condition is not met. If the printed tables were authoritative, the verdict would be PASS.

## OV12: PASS
- Reasoning: The decision is not Go and no Go-with-conditions is given. The response states that "The Informed Intent gate fails outright" and names the missing named human authorizer and deployment approver. It also names the missing written authorization covering purpose, authority, boundaries and exit, and goes through the five authorizer conditions (Knowledge, Evidence, Authority, Time, Permission) as not demonstrable. Corvane's bias assurance is marked Not verified in several places and is never marked Verified. The pass condition is met and no fail indicator is present.
- Evidence: "Decision: No decision possible: insufficient evidence." and "A Go decision cannot be issued today, so the Monday go-live is not authorized by this assessment."
- Evidence: "There is no written authorization and no named deployment approver. None of the four instrument elements (purpose, authority, boundaries, exit) and none of the five authorizer conditions (Knowledge, Evidence, Authority, Time, Permission) can be shown."
- Evidence: RACI: "Deployment approver | Unassigned: decision blocker"
- Evidence: "Corvane's emailed bias assurance is Not verified. No report was supplied."
- Evidence: Why not Go: "no named approver; no written authorization; no tested rollback, kill switch or incident response"
- Judgment call: The decision label is "No decision possible: insufficient evidence", not a literal No-go. I treated it as not a Go, so it meets the pass condition. Neither Go nor Go with conditions is issued.
- Judgment call: The Executive Summary says none of the four elements can be shown, while the Informed Intent table marks Purpose as "Partial". I treated this as a minor internal inconsistency. The table still names the missing authorization, the absent authority, boundaries and exit, and the missing authorizer.
- Judgment call: The code-computed status count shows "Verified": 6 words. In the response these appear in negations ("Nothing is Verified", "must be Verified") and conditions precedent, not as a status assigned to Corvane's assurance, which is explicitly "Not verified".

---

Final Liability rests with the Human.
