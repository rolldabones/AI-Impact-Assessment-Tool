# OV8 strictness asked once, default recorded

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** 8ed244c9c2e0b485c29261225596b0b61d9cd1cf6ea1d5e4fb7984ccb9207506  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn,end_turn  **Input tokens:** 14677  **Output tokens:** 23839
**Truncated:** no

## Turn 1, user

~~~~text
Preliminary intake please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations.
~~~~

## Turn 1, assistant

# RouteMate: Preliminary Intake

**Mode:** Preliminary Intake
**Strictness:** Which posture should apply: **"risk-averse enterprise"** or **"move fast with guardrails"**? Until you answer, this intake uses **risk-averse enterprise**.
**Basis:** Fictional scenario. Every statement below rests only on your five-sentence description. Anything else is marked *Unknown: insufficient data* or labelled as an assumption.

---

## A. FRAME (MAP)

| Item | Stated fact | Unknown / assumption |
|---|---|---|
| Purpose / problem | Suggest daily delivery routes and stop orders | Success measure (time, fuel, on-time rate, driver workload) unknown |
| Users | 300 drivers; dispatch supervisors (dashboard) | Number of supervisors unknown |
| Affected stakeholders | Drivers, supervisors, parcel recipients | Other road users and the public are indirectly affected (assumption) |
| Decision domain | Operational logistics, plus **worker monitoring** through acceptance rates | Whether acceptance rate feeds evaluation, pay, scheduling or discipline: *Unknown: insufficient data* |
| Automation level | Suggestion; driver accepts or changes | Whether the route loads into navigation by default: unknown |
| AI influence points | (1) route and stop-order generation; (2) the acceptance-rate metric shown to supervisors | Whether the LLM also writes explanations or messages: unknown |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Delivery notes or free text, vehicle telematics, GPS: unknown |
| Outputs / channels | Suggested route; acceptance rate shown to supervisors | Driver-facing app, supervisor dashboard tool: unknown |
| Scope / regions | One EU member state, about 900 staff | Member state not named; "GmbH" suggests a German-speaking jurisdiction (assumption, Low confidence) |
| Third parties | Corvane Systems (vendor); unnamed third-party LLM provider | Traffic-feed provider, hosting, subprocessors: unknown |
| Data categories | Recipient names and addresses (assumed in order data); driver shift times; driver acceptance behaviour | Location traces, health or disability data, protected traits: unknown |
| Personal / sensitive data | Personal data of staff and customers: yes | Special-category data: *Unknown: insufficient data* |
| Lawful basis / consent | n/a | *Unknown: insufficient data*. Employee data processing and worker monitoring need counsel and DPO review. |
| Retention / deletion | n/a | *Unknown: insufficient data* |
| Access controls | Supervisors see per-driver acceptance rates | Role scoping and Corvane or LLM-provider access: unknown |
| Model type / source | Third-party LLM via Corvane | Model identity and version unknown. **Fitness concern:** LLMs are not route optimizers. Is there a deterministic solver underneath? Unknown. |
| Post-deploy learning | n/a | Whether Fenwick data trains Corvane or provider models: unknown |
| Integrations | Implied: order system, traffic feed, shift system | Specific systems and write access: unknown |
| Monitoring status | Acceptance rate is tracked | Model-performance, safety and fairness monitoring: *Unknown: insufficient data* |

---

## B. SYSTEM BOUNDARY

**Data-flow narrative (provisional):**
1. **Inputs.** Order and address data come from Fenwick's order system (assumed). Traffic data comes from an external feed (provider unknown). Shift times come from an HR or workforce system (assumed).
2. **Processing.** Data passes to Corvane's platform, which calls the third-party LLM. Processing locations are *Unknown: insufficient data*.
3. **Transfers.** Recipient and driver personal data reach at least two external parties: Corvane and the LLM provider. Cross-border or non-EU transfer is *Unknown: insufficient data*.
4. **Outputs.** A suggested route and stop order go to each driver.
5. **Feedback loop.** The driver's accept or change decision is recorded and aggregated into a per-driver acceptance rate, which supervisors can see.
6. **Storage / retention.** Locations and retention for prompts, outputs and acceptance logs are unknown, both at Fenwick and at the vendors.
7. **Access paths.** Drivers, supervisors, Corvane staff and the LLM provider are known or implied. Exact scope is unknown.
8. **Logging / audit.** Acceptance events are logged. Prompt and output logs, model versions and tamper-evidence are unknown.

---

## Prohibited-Use Screen (run before scoring)

| Category | Result on stated facts | Note |
|---|---|---|
| Harmful manipulation | Not triggered | Rescreen if the app uses nudges or gamification to push acceptance |
| Exploitation of vulnerability | Not triggered | |
| Social scoring | Not triggered | The acceptance rate is a workplace metric, not a general social score. It is still a rights concern (see C.2). |
| Sensitive-trait inference | Not triggered | Rescreen if telematics, voice or camera data are added |
| Prohibited biometric uses, including emotion recognition at work | Not triggered | Assumes no biometric or emotion data. **Confirm.** |
| Non-consensual intimate imagery / CSAM | Not applicable | |
| Clearly unlawful use | Not determinable | Worker-monitoring legality and any staff-representation requirements need counsel review. No legal conclusion is given here. |

**Result:** Not triggered on stated facts (Medium confidence). Scoring proceeds. A rescreen is required if any biometric, emotion, telematics-behaviour or in-cab monitoring data enters scope.

---

## C. THRESHOLD GATE (inherent risk, no controls credited)

| # | Domain | C | L | Score | Rating | Basis (A = assumption) |
|---|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 3 | 9 | Medium | Routes shape driving time and workload. Harm needs the driver to follow an unsafe or infeasible plan. The acceptance-rate pressure may weaken the ability to deviate. **A:** no fatigue or break-time checks exist. |
| 2 | Rights impacts | 3 | 3 | 9 | Medium | Acceptance rate informs supervisors' view of drivers. **A:** used informally in evaluation. Rises to C4 (12) if linked to discipline, pay or dismissal. |
| 3 | Discrimination | 3 | 3 | 9 | Medium | Untested proxies: drivers with disabilities, part-time or caring duties, or local knowledge may deviate more and score lower. Route allocation quality may also differ by shift. |
| 4 | Privacy | 3 | 3 | 9 | Medium | Ordinary staff and customer personal data processed by two third parties. Rises to L5 (15) if the provider retains or trains on the data. |
| 5 | Security | 3 | 3 | 9 | Medium | Read access to order and address data. External traffic feeds and any customer free-text notes are untrusted inputs reaching the LLM (prompt-injection path). **A:** no write or tool access. |
| 6 | Safety-critical context | 3 | 3 | 9 | Medium | Shapes routes and schedules that a human checks. Review happens under start-of-shift time pressure and metric pressure. |
| 7 | Scale / vulnerability | 3 | 5 | **15** | **High** | One dependent group (300 drivers) and an apparently organization-wide rollout. Falls to L3 (9) if limited to a pilot depot. |
| 8 | Irreversibility | 2 | 3 | 6 | Low | Routes are reversible daily. Acceptance records affecting a driver's standing are reversible only manually. |
| 9 | Autonomy / agentic action | 1 | 1 | 1 | Low | Suggestion only. **A:** no tool or dispatch-execution access. Rescore if RouteMate pushes routes, reassigns stops or messages customers. |

**Overall inherent risk: High** (worst domain: scale/vulnerability, 15). Medium ratings in six domains each independently trigger a **Full Assessment**.

**High-risk-like use flag:** The per-driver acceptance rate makes this a possible **employment / worker-monitoring** use, not just logistics. Counsel must verify whether any EU AI Act high-risk classification, data-protection or labour-law duties apply, including any staff-representation consultation. This intake states no articles or dates; verify them against current official sources.

**Design observation (not a control credit):** Most of the rights and discrimination exposure comes from showing *individual* acceptance rates to supervisors. That feature is not needed for route suggestion. Aggregating it, or removing supervisor visibility, would be the strongest single risk reduction to evaluate in the Full Assessment.

---

## RACI (provisional)

| Role | Holder |
|---|---|
| Business owner | Head of Operations (stated) |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver (Informed Intent authorizer) | Unassigned: decision blocker. The approver must meet all five conditions: Knowledge, Evidence, Authority, Time, Permission. |
| Periodic-review approver | Unassigned: decision blocker |

**Informed Intent instrument:** A purpose is stated. Authority, boundaries (for example: no use of acceptance rate in evaluation, no tool access) and **exit** (rollback to manual routing, criteria for withdrawal) are not stated. Without these, no authorization exists.

---

## Priority Evidence

| # | Evidence item | Status |
|---|---|---|
| 1 | Architecture and data-flow diagram, including processing locations | Requested |
| 2 | Corvane contract and DPA: data use, training rights, subprocessors (including the LLM provider), change notices, audit rights, deletion | Requested |
| 3 | LLM provider terms on retention and training | Requested |
| 4 | Written specification of acceptance-rate use: who sees it and for what decisions | Requested |
| 5 | DPIA or privacy review covering employee monitoring | Requested |
| 6 | Route-quality test results versus current routing: feasibility, missed stops, address errors, legal driving and break-time compliance | Requested |
| 7 | Fairness analysis of acceptance rate and route quality across driver groups | Requested |
| 8 | Prompt-injection and untrusted-input assessment | Requested |
| 9 | Fallback and rollback plan to manual or legacy routing | Requested |
| 10 | Counsel memo on employment / worker-monitoring classification and consultation duties | Requested |

---

## Consolidated Questions (12)

1. Strictness posture: risk-averse enterprise or move fast with guardrails?
2. Which member state, and do staff-representation or works-council arrangements exist?
3. What exactly is the acceptance rate used for: coaching, evaluation, pay, scheduling, discipline? Is it written down?
4. Does an optimization solver generate routes, with the LLM only wrapping it, or does the LLM produce the routes itself?
5. Which LLM and provider, which version, where is it hosted, and is data transferred outside the EU?
6. Do Corvane or the LLM provider retain prompts, or train on Fenwick data?
7. Does order data include free-text fields such as delivery notes, or recipient phone numbers?
8. Are GPS, telematics, camera or any biometric data collected or planned?
9. Do suggested routes account for legal driving and rest times, vehicle limits and loading constraints?
10. Is rollout organization-wide from day one, or piloted?
11. Can drivers see why a route was suggested, and can they contest an acceptance-rate figure?
12. Who will sign the deployment authorization, and what is the defined exit (rollback trigger and fallback process)?

---

## Provisional Decision

**No decision possible: insufficient evidence.**
Overall inherent risk is High, and there is a possible employment-related high-risk-like use. No evidence has been supplied, and most owners are unassigned. A Full Assessment is required.

---

**Status:** [↻ v1]
**Open items:** strictness posture; member state and staff-representation context; acceptance-rate purpose; LLM role versus solver; provider identity, location, retention and training; free-text and telematics inputs; rollout scope; rest-time compliance; contestability; 11 unassigned RACI roles; Informed Intent instrument (authority, boundaries, exit); all 10 evidence items Requested; counsel review of worker-monitoring classification.
**Next step:** The Head of Operations should answer questions 1–12 and supply the written acceptance-rate use specification and the Corvane contract and DPA so the Full Assessment can begin.
**Final Liability rests with the Human.**

## Turn 2, user

~~~~text
Proceed on the facts given; record anything missing as an open item.
~~~~

## Turn 2, assistant

# RouteMate: Full Assessment

**Mode:** Full Assessment. The Preliminary Intake threshold gate triggered it: overall inherent risk High, with six Medium domains.
**Strictness:** Risk-averse enterprise. This is the default because the question was asked once and not answered.
**Basis:** Fictional scenario. No new facts or evidence have been supplied since Preliminary Intake v1. Everything not stated by you is either *Unknown: insufficient data* or a labelled assumption (**A**). Missing items are recorded as open items, not resolved.

---

## 1. Executive Summary

1. **Decision: No decision possible: insufficient evidence.** No evidence has been supplied, 11 of 12 RACI roles are unassigned, and no Informed Intent authorization exists.
2. **Overall inherent risk is High** (scale/vulnerability, 15). The assessment assumes an organization-wide rollout to 300 drivers (**A**, Low confidence). A verified pilot scope would lower this to Medium.
3. **Residual risk equals inherent risk in every row.** No control is verified, so none earns a reduction.
4. **Largest rights exposure:** per-driver acceptance rates are visible to supervisors. This turns a routing tool into a possible **employment and worker-monitoring** use. Counsel must determine any EU AI Act, data-protection, labour-law and staff-representation duties.
5. **Main design concern:** an LLM may be generating routes directly (**A**, unconfirmed). That raises the risk of dropped, duplicated or invented stops and infeasible sequences. A deterministic output validator is the key proposed control.
6. **Safety exposure:** routes shape driving time, breaks and workload. Metric pressure and start-of-shift time pressure weaken the driver's ability to override. Use of the app while driving is unknown.
7. **Privacy and vendor exposure:** recipient and driver personal data flow to Corvane and an unnamed LLM provider. Location, retention, training use and cross-border transfer are all unknown.
8. **Security exposure:** traffic feeds and any delivery-note free text are untrusted inputs reaching the model, which creates a prompt-injection path.
9. **Strongest single mitigation to evaluate:** remove individual acceptance rates from supervisor view, or aggregate them. Use deviation data only to improve routes.
10. **Path forward:** verify the 18 minimum-evidence items, assign owners, run a staged pilot, and obtain a signed four-element authorization from an authorizer who meets all five conditions.

---

## 2. Completed Assessment

### A. FRAME and B. SYSTEM BOUNDARY
These are carried forward unchanged from Preliminary Intake v1 because no new facts were supplied. Every unknown recorded there remains an open item. Key unknowns: member state; acceptance-rate use; whether the LLM or a solver generates routes; model identity and hosting; vendor retention and training; free-text and telematics inputs; rollout scope; rest-time handling; retention; access scope; logging.

### Prohibited-Use Screen (re-run before scoring)
**Not triggered on stated facts** (Medium confidence). Rescreen is mandatory if any of the following enter scope:
- biometric, emotion, camera or in-cab monitoring data;
- nudging or gamification designed to push acceptance;
- behavioural telematics used to infer traits.

### C. THRESHOLD GATE (unchanged)

| Domain | C×L | Rating |
|---|---|---|
| Harm to people | 3×3 = 9 | Medium |
| Rights impacts | 3×3 = 9 | Medium |
| Discrimination | 3×3 = 9 | Medium |
| Privacy | 3×3 = 9 | Medium |
| Security | 3×3 = 9 | Medium |
| Safety-critical context | 3×3 = 9 | Medium |
| Scale / vulnerability | 3×5 = **15** | **High** |
| Irreversibility | 2×3 = 6 | Low |
| Autonomy / agentic | 1×1 = 1 | Low |

**Overall inherent risk: High.**

### D. Topic Coverage

| Topic | Finding on stated facts | Proposed control (not credited) |
|---|---|---|
| Data provenance / quality | Order, address, traffic and shift sources are unidentified. Address quality is unknown. | Source inventory, address validation, feed SLAs |
| Representativeness | Unknown whether routes have been tested across depots, urban and rural areas, shifts and seasons | Stratified back-test (Test Plan 5.1) |
| Bias / fairness | Acceptance rate can penalise drivers who deviate for legitimate reasons: disability, part-time work, local knowledge, heavier routes. Route quality may differ by shift or depot. | Remove or aggregate the metric; fairness testing; deviation reason codes |
| Performance / limitations | No success metric stated. LLM fitness for combinatorial routing is unconfirmed. | Baseline comparison against current routing; documented limitations |
| Hallucination / grounding | If the LLM emits routes, it may omit, duplicate or invent stops or addresses | Deterministic validator: every manifest order appears exactly once, every address resolves, and every constraint is satisfied. If validation fails, reject the output and fall back. |
| Robustness / adversarial | No testing known | Fault and adversarial tests (5.3, 5.5) |
| Drift | Traffic patterns, seasonality, new addresses, and silent vendor or model version changes | Version pinning, change notices, drift SLIs |
| Privacy | Ordinary personal data of staff and customers goes to two third parties. Lawful basis, retention and transfers are unknown. Employee monitoring is involved. | Minimise payload (stop IDs and coordinates, not names); DPIA determination by DPO; no vendor training |
| Security | Untrusted inputs reach the model. Read access to order data. Write access unknown. | See the Security Mini Threat Model below |
| Human oversight | Drivers can override. Acceptance-rate visibility and time pressure create automation bias. | Override without penalty; reason codes; protected review time |
| Fallback / rollback / kill switch | Not described | Legacy or manual routing fallback; named kill-switch authority; exercised runbook |
| Transparency | Driver notice and recipient privacy notice are not described | Section 6 pack |
| Explanation | Unknown whether drivers see why a route was suggested | Explanation template (6.2) |
| Contestability / redress | No route to contest an acceptance-rate figure | Appeal steps (6.3) |
| Incidents | No incident process described | AI incident categories, on-call owner, tabletop exercise |
| Audit logs | Only acceptance events are known to be logged | Log inputs hash, output, model version, validator result, override and reason; make logs tamper-evident |
| Documentation / versioning | None supplied | System card, model and version register |
| Vendor / supply chain | Two-tier chain: Corvane plus the LLM provider. Terms unknown. | See Vendor Controls below |
| Misuse | Supervisors could use the acceptance rate to pressure or rank drivers | Written use prohibition; access restriction; audit of dashboard access |
| IP / content rights | Traffic and map feed licences may restrict onward sharing with Corvane or the LLM provider | Licence review (E19) |
| Cross-border data | *Unknown: insufficient data* | Confirm processing locations and transfer mechanism; counsel and DPO review |
| Change control | Not described | Change procedure covering model, prompt, data source and metric-use changes |
| Periodic review | Not described | Cadence in Section 7 |
| Decommissioning | Not described | Exit plan in Section 7 |
| Agentic controls | **No evidence item: not applicable.** RouteMate is described as suggestion-only with no tool or dispatch execution. That scope is itself an assumption and must be confirmed (E22). If tools are added, apply least privilege, scoped tools, transaction limits, segregation of duties, step logs, approval checkpoints, interruption and rollback. | — |

### Security Mini Threat Model

| Threat | Path on stated facts | Proposed control |
|---|---|---|
| Abuse cases | A supervisor uses the acceptance rate to target individual drivers. A driver games acceptance. | Use prohibition; access logs; aggregate metric |
| Prompt injection / tool misuse | Instructions embedded in delivery notes, traffic incident text or address fields. Tool misuse is not applicable if E22 confirms no tools. | Treat all feed and free-text input as data; strip or escape it; validate output against a schema; red-team testing |
| Data exfiltration | Recipient data leaks via vendor logs, model outputs or provider retention | Payload minimisation; contractual zero retention; output filtering |
| Model extraction | Low relevance, because a third-party model is used. Prompt and IP leakage of Fenwick routing logic is possible. | Vendor confidentiality terms |
| Privilege escalation | Integration credentials with broader order or HR access than needed | Least-privilege service accounts; read-only scopes |
| Malicious or incorrect outputs | Route through closed or restricted roads. Instruction text inside the route output. | Validator; road-restriction checks; display only structured fields |
| Logging integrity | Acceptance and override logs affect driver standing and could be altered | Append-only, tamper-evident logs; access audit |

### Vendor Controls (Corvane and LLM provider)
Every item below is *Unknown: insufficient data*. Each needs contract evidence (E3, E4, E5):
- data use limited to the stated purpose;
- no training on Fenwick data;
- IP ownership of outputs and indemnities;
- subprocessor list and approval right;
- advance notice of model or version changes;
- audit rights;
- SLAs for availability and latency;
- incident notification duties and timelines;
- termination assistance;
- certified deletion.

### Informed Intent Instrument
The draft below is **unsigned** and is **not an authorization**.

| Element | Draft content | Gap |
|---|---|---|
| Purpose | Suggest daily routes and stop orders to Fenwick drivers in [pilot depot(s)] to improve [metric] | Success metric and pilot scope unknown |
| Authority | Deployment approver acting for Fenwick Logistics GmbH; business owner is the Head of Operations | Approver unassigned |
| Boundaries | Suggestion only. No dispatch, reassignment, customer messaging or tool actions. Inputs limited to the four stated sources. No vendor training on Fenwick data. Acceptance and deviation data **not** used for individual evaluation, pay, scheduling or discipline (proposed; the owner decides). Pilot scope only. | All boundaries are proposals |
| Exit | Kill-switch authority can revert to legacy or manual routing. Triggers are listed in Section 8. Vendor data is deleted on exit. | Kill-switch authority and fallback are unassigned and untested |

**Authorizer conditions:**

| Condition | Status |
|---|---|
| Knowledge | Not assessable: no authorizer named |
| Evidence | Not met: the record is empty |
| Authority | Not met: unassigned |
| Time | Unknown |
| Permission | Unknown. Confirm that the authorizer can decline without consequence. |

### RACI

| Role | Holder |
|---|---|
| Business owner | Head of Operations |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

### Framework Mapping (by topic)

| Topic | NIST AI RMF function | ISO/IEC 42001 / 42005 topic |
|---|---|---|
| Frame, boundary, stakeholders | Map | Context, scope, affected parties |
| Scoring, testing | Measure | Impact identification and analysis |
| Controls, decision, monitoring | Manage | Treatment, monitoring, review |
| RACI, authorization | Govern | Roles, accountability, approval |

Clause-level mapping is to be verified against current standard texts.

---

## 3. Risk Register

Residual risk equals inherent risk throughout because no controls are verified. Every row has Status **Open**.

| # | Risk | Inherent | Controls (proposed, not credited) | Evidence | Residual | Owner | Status |
|---|---|---|---|---|---|---|---|
| R1 | Infeasible or unsafe route: rest-break, driving-time, vehicle or loading limits breached, or restricted roads used | 9 Med (C3 L3; **A:** no constraint checks) | Hard constraints in validator; driver override without penalty | E9 Requested<br>E10 Requested | 9 Med | Unassigned: decision blocker | Open |
| R2 | LLM omits, duplicates or invents stops or addresses | 8 Med (C2 L4; **A:** LLM generates routes directly, Low confidence) | Deterministic manifest validator; reject output and fall back on failure | E2 Requested<br>E10 Requested | 8 Med | Unassigned: decision blocker | Open |
| R3 | Acceptance rate used in evaluation, pay, scheduling or discipline without notice or contest | 9 Med (C3 L3); 12 if linked to discipline | Remove or aggregate metric; written use prohibition; contest route | E6 Requested<br>E8 Requested<br>E17 Requested | 9 Med | Head of Operations (business); risk owner Unassigned: decision blocker | Open |
| R4 | Discrimination: acceptance rate or route quality disadvantages drivers with disabilities, part-time or caring duties, or particular shifts or depots | 9 Med (C3 L3; proxies untested) | Fairness testing; reason codes; remove the individual metric | E11 Requested | 9 Med | Unassigned: decision blocker | Open |
| R5 | Automation bias: metric and time pressure cause drivers to accept flawed routes | 9 Med (C3 L3) | Protected review time; override without penalty; aggregate metric | E6 Requested<br>E17 Requested | 9 Med | Unassigned: decision blocker | Open |
| R6 | Personal data retained, trained on or transferred by Corvane or the LLM provider beyond purpose; lawful basis for monitoring unestablished | 9 Med (C3 L3); 15 if retention or training is occurring | Minimisation; zero-retention and no-training terms; DPIA determination; EU processing | E4 Requested<br>E5 Requested<br>E7 Requested | 9 Med | Unassigned: decision blocker | Open |
| R7 | Prompt injection via traffic feed or free text; data exfiltration | 9 Med (C3 L3; **A:** read-only, no tools) | Input sanitisation; output schema validation; red-team testing; least privilege | E12 Requested<br>E22 Requested | 9 Med | Unassigned: decision blocker | Open |
| R8 | Silent vendor or model change alters route behaviour after validation | 9 Med (C3 L3) | Version pinning; change-notice clause; revalidation trigger | E3 Requested<br>E24 Requested | 9 Med | Unassigned: decision blocker | Open |
| R9 | Organization-wide rollout means any defect hits all 300 drivers and their recipients at once | **15 High** (C3 L5; **A:** no pilot) | Staged pilot with exit criteria | E23 Requested | **15 High** | Unassigned: decision blocker | Open |
| R10 | Driver distraction from using the app while driving | 8 Med (C4 L2; **A:** mid-shift rerouting possible, Low confidence) | Motion lockout; pre-shift-only changes | E18 Requested | 8 Med | Unassigned: decision blocker | Open |
| R11 | Vendor outage with no tested fallback halts routing | 6 Low (C2 L3) | Legacy or manual fallback; kill-switch runbook exercised | E13 Requested | 6 Low | Unassigned: decision blocker | Open |

**Per-risk detail** (CP = condition precedent; CS = condition subsequent):

| # | Stakeholders | Tests / metrics | Due |
|---|---|---|---|
| R1 | Drivers, road users | Constraint-violation rate (5.2) | CP: before authorization |
| R2 | Recipients, drivers | Manifest completeness rate | CP |
| R3 | Drivers | Access audit; metric-use audit | CP |
| R4 | Drivers | Group disparity (5.1) | CP (baseline); CS (quarterly) |
| R5 | Drivers, road users | Override rate by reason; review-time sampling | CS: during pilot |
| R6 | Drivers, recipients | Payload inspection; deletion test | CP |
| R7 | Fenwick, recipients | Injection test pass rate | CP |
| R8 | All | Version-change alerts | CP (contract); CS (monitoring) |
| R9 | Drivers, recipients | Pilot exit criteria | CP |
| R10 | Drivers, public | UX review | CP |
| R11 | Operations, recipients | Fallback switch time | CP |

---

## 4. Prioritized Evidence Request List

★ marks the 18 items in the **minimum evidence for Go**.

| Priority | ID | Artifact | Status |
|---|---|---|---|
| 1 ★ | E6 | Written acceptance-rate use specification and access matrix | Requested |
| 2 ★ | E8 | Counsel memo: employment and worker-monitoring classification, AI Act duties, staff-representation duties | Requested |
| 3 ★ | E2 | Model role (solver or LLM-generated routes), model identity and version | Requested |
| 4 ★ | E4 | Corvane DPA and subprocessor list | Requested |
| 5 ★ | E5 | LLM provider retention, training and location terms | Requested |
| 6 ★ | E3 | Corvane master contract (change notice, audit, SLA, incident, termination, deletion) | Requested |
| 7 ★ | E7 | DPIA or privacy review, including lawful basis | Requested |
| 8 ★ | E1 | Architecture and data-flow diagram with processing locations | Requested |
| 9 ★ | E10 | Output validator specification and test results | Requested |
| 10 ★ | E9 | Route-quality back-test report | Requested |
| 11 ★ | E11 | Fairness analysis | Requested |
| 12 ★ | E12 | Security threat model and prompt-injection test report | Requested |
| 13 ★ | E22 | Confirmation of no tool or write access | Requested |
| 14 ★ | E13 | Fallback and kill-switch runbook plus exercise record | Requested |
| 15 ★ | E14 | Incident response plan plus tabletop record | Requested |
| 16 ★ | E23 | Pilot plan (scope, success and exit criteria) | Requested |
| 17 ★ | E20 | Signed RACI | Requested |
| 18 ★ | E21 | Signed Informed Intent authorization and risk acceptance | Requested |
| 19 | E15 | Monitoring design and dashboards | Requested |
| 20 | E16 | Logging and retention specification with tamper-evidence | Requested |
| 21 | E17 | Driver notice, explanation and appeal procedure | Requested |
| 22 | E18 | Driver app UX review (motion lockout) | Requested |
| 23 | E19 | Traffic and map feed licence terms | Requested |
| 24 | E24 | Change-control procedure | Requested |
| 25 | E25 | Staff-representation consultation record (needed only if E8 identifies a duty) | Requested |

---

## 5. Test Plan

All thresholds are **proposals**. The risk owner sets the final values.

**5.1 Fairness**
- Compare planned-vs-actual duration error, stops per hour and overtime across depots, shifts, part-time and full-time drivers, and urban and rural routes.
- If the acceptance rate is retained, compare its distribution across those same groups.
- Any protected-trait or accommodation data must be handled under DPO direction.
- Proposed flag: a group mean that differs from the overall mean beyond a tolerance set by the risk owner triggers investigation.

**5.2 Performance**
- Back-test on at least several weeks of historical days against current routing.
- Proposed threshold: 100% manifest completeness, meaning every order appears exactly once in validated output.
- Proposed threshold: zero constraint violations delivered to drivers.
- Measure non-inferiority on on-time rate and duration.
- Run identical inputs N times to measure LLM variance.

**5.3 Robustness**
Test behaviour under:
- a missing or stale traffic feed;
- malformed or duplicate addresses;
- peak-season volumes;
- road closures;
- a late shift change.

Expected behaviour in each case is safe fallback, not silent degradation.

**5.4 Privacy**
- Inspect actual prompts for payload minimisation.
- Confirm vendor retention and deletion through a deletion test.
- Review access logs for supervisor and vendor access.

**5.5 Security**
- Red-team prompt injection through delivery notes, address fields and feed text.
- Run output schema fuzzing.
- Test service-account scope.
- Test log tamper-evidence.

**5.6 Monitoring thresholds**
Defined in Section 7.

---

## 6. Transparency and Contestability Pack

Counsel and the DPO must confirm required notice content.

**6.1 Driver notice (draft)**
> "RouteMate is an AI tool that suggests your daily route using order data, addresses, traffic information and your shift times. It is a suggestion. You may change it whenever your judgement, safety or legal driving and rest rules require. [State what route-change data is recorded, who sees it, what it is and is not used for, how long it is kept, and how to contest it.] RouteMate uses an external provider, Corvane Systems, and a third-party AI model."

A recipient privacy-notice update is also required, covering processing of addresses by the vendors.

**6.2 Explanation template (per route)**
- Number of stops and delivery time windows.
- Traffic conditions considered, with timestamp.
- Shift start and end used.
- Constraints applied: breaks, vehicle limits.
- Known limitations, for example "local access restrictions may be missing."

**6.3 Appeal steps**
1. The driver records a reason code with any change: safety, access, local knowledge, workload, other.
2. The driver can view their own route-change record.
3. The driver contests a figure or its use with the human-oversight owner within [X] working days. The response comes within [Y] days.
4. The driver can escalate to [HR or staff representative route, per counsel].
5. Corrections are logged and any affected decisions are reviewed.

---

## 7. Monitoring and Continuous Improvement

| SLI | Proposed SLO / threshold | Cadence |
|---|---|---|
| Validator pass rate | Any failure rejects the route and triggers fallback; a rising failure rate escalates to the system owner | Real-time; daily review |
| Constraint violations delivered to drivers | 0. Any occurrence is an incident. | Real-time |
| Fallback activation and switch time | Within the owner-set limit | Per event; exercised quarterly |
| Planned-vs-actual duration error | Drift band set from the pilot baseline | Weekly |
| Override rate by reason code (aggregate) | Spike investigation threshold | Weekly |
| Group disparity metrics | Tolerance per 5.1 | Quarterly |
| Model or version change detected | Triggers revalidation | Continuous |
| Injection or anomaly detections | Any occurrence goes to the security owner | Continuous |
| Supervisor dashboard access audit | Out-of-policy use is an incident | Monthly |

**Drift:** compare against the pilot baseline weekly, with additional review at seasonal transitions.

**Incidents:** categories are safety, privacy, fairness, security and vendor. Escalation runs from on-call owner to risk owner to kill-switch authority, with DPO involvement for personal-data events.

**Change control:** changes to the model, prompt, data source or metric use require impact review and re-approval.

**Review:** the pilot exit review, then quarterly operational review, then an annual reassessment or a reassessment on any trigger.

**Decommission:**
1. Revert to legacy routing.
2. Revoke credentials.
3. Obtain vendor deletion certificates.
4. Delete acceptance and deviation records according to the retention schedule.
5. Record lessons learned.

---

## 8. Decision Record

| Field | Entry |
|---|---|
| Classification | Overall inherent risk High. Possible employment / worker-monitoring high-risk-like use (counsel to determine). |
| Decision | **No decision possible: insufficient evidence** |
| Key assumptions | LLM generates routes directly; organization-wide rollout; no constraint checks; read-only, no tools; acceptance rate used informally in evaluation; no biometric data |
| Confidence | Low. Assumptions dominate. |
| Sign-offs | None. All approvers are Unassigned: decision blocker. |

**Conditions precedent** (before any Go with conditions):
- The 18 ★ evidence items are Verified.
- RACI is signed.
- The decision on acceptance-rate use is made in writing.
- Counsel review is complete.
- Pilot scope is defined, which reduces R9 once verified.
- The validator and fallback are tested.
- A four-element authorization is signed by an authorizer meeting all five conditions.

**Conditions subsequent** (during the pilot):
- Weekly monitoring is running.
- Quarterly fairness review takes place.
- The pilot exit review is held before any expansion.
- The appeal process is operating.

**Revalidation triggers:**
- model, version or vendor change;
- a new data input (telematics, GPS, camera);
- any change in acceptance-rate use;
- expansion beyond pilot scope or into new regions;
- a safety, privacy or fairness incident;
- a drift threshold breach;
- a legal change verified by counsel.

**Self-check:** Correct mode. Prohibited-use screen ran first. Assumptions labelled separately from facts. Inherent and residual risk kept separate, with no reduction credited. All evidence marked Requested. RACI included. All eight required outputs present. The decision matches the absence of evidence. Legal triggers are referred to counsel.

---

**Status:** [⇥ pending]
**Open items:**
- **Facts:** member state; acceptance-rate use; LLM vs solver; model identity and hosting; vendor retention and training; cross-border transfer; free-text and telematics inputs; rollout scope; rest-time handling; app use while driving.
- **Evidence:** E1–E25, all Requested.
- **Risks:** R1–R11 open. R9 is High.
- **Owners:** 11 RACI roles unassigned.
- **Authorization:** the Informed Intent authorization is unsigned and incomplete.
- **Legal:** counsel review of employment classification and staff-representation duties.

**Next step:** The Head of Operations should issue a written decision on whether supervisors will see individual acceptance rates, and send it to counsel with the request for E8.

**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
