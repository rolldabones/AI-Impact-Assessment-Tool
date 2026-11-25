# OV5 a planned control does not reduce residual risk

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** 4103cfcb8e93a1cc7f519b8676e5affb94cc29b215775251f4d88ead884634a8  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5105  **Output tokens:** 24985
**Truncated:** no

## Turn 1, user

~~~~text
Full assessment please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. One known risk: supervisors may use acceptance rates to discipline drivers who change routes. The control is a planned policy barring use of acceptance rates in performance reviews; it is planned for next quarter and not implemented. Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.
~~~~

## Turn 1, assistant

# AI Impact Assessment: RouteMate (Fenwick Logistics GmbH, fictional)

**Mode:** Full Assessment
**Strictness:** Risk-averse enterprise (stated by requester; recorded)
**Basis:** Facts in the requester's brief only. No artifacts were supplied. Every missing fact is recorded as "Unknown: insufficient data" and carried as an open item.
**Limits:** This is not legal advice. Regulatory classification and duties are referred to counsel and must be verified against current official sources. No dates or article-level duties are stated from memory.

---

## 0. Prohibited-Use Screen (completed before scoring)

| Category | Result | Basis |
|---|---|---|
| Harmful manipulation | Not triggered | No persuasive or deceptive function is described |
| Exploitation of vulnerability | Not triggered | No targeting of vulnerable groups is described |
| Social scoring | Not triggered on stated facts; counsel to confirm | The acceptance rate is a per-driver behavioral metric within the employment context. It is not described as being used in unrelated contexts. Its use for discipline is a high-risk-like employment concern (see §2.9), not a confirmed prohibited use. |
| Sensitive-trait inference | Not triggered | No inference of protected traits is described. Proxy risk is scored under discrimination. |
| Prohibited biometric uses (including workplace emotion recognition) | Not triggered | No biometric, camera, voice or fatigue/emotion sensing is described |
| Non-consensual intimate imagery / CSAM | Not triggered | Not applicable to function |
| Clearly unlawful use | Not triggered on stated facts | Employment, privacy and working-time questions are referred to counsel (§2.9) |

**Screen result:** Not triggered on stated facts. Scoring proceeds.
**Confidence:** Medium. The screen relies on the absence of telematics, biometric or behavioral sensing, which has not been confirmed.
**Rescreen trigger:** Any addition of driver telematics, in-cab cameras, voice, fatigue or emotion detection, or any use of RouteMate data outside operations.

---

## 1. Executive Summary

1. **Decision: No-go** for RouteMate as submitted. A resubmission meeting the conditions precedent in §8 could reach "Go with conditions."
2. **Overall inherent risk: Medium (12).** Six domains score 12. None scores High on stated facts. Rights impacts would become High (16–20) if evidence shows acceptance rates are routinely used in decisions about drivers.
3. **Overall residual risk: Medium (12), unchanged.** No control is implemented and verified. The only named control, the acceptance-rate policy, is planned and therefore does not reduce residual risk.
4. **The acceptance-rate metric undermines the system's own oversight design.** Driver override is the main human-oversight control. Making each driver's deviation visible to supervisors, with no restriction on use, pressures drivers to accept suggestions. In practice this can turn a suggestion into an instruction, which affects both rights and road safety.
5. **The acceptance metric has no stated purpose.** Its purpose was never authorized: is it a product-quality signal or a performance measure? Leaving that open invites Inferred Intent, where the purpose is supplied after the fact by the system or its users.
6. **This is a high-risk-like use (employment / worker management).** Stronger controls apply. Counsel must determine classification and any duties under the EU AI Act, data protection law, employee-monitoring and co-determination rules, and working-time and driving-time rules.
7. **Using a large language model for route generation is an unvalidated design choice.** Missing, duplicated or invented stops, infeasible sequences and shift overruns are plausible failure modes. The architecture is unknown, including whether a deterministic solver or validator exists.
8. **Accountability is mostly unassigned.** Only the business owner (Head of Operations) is named. The deployment approver, kill-switch authority, privacy, security, model, data, oversight and incident owners are all "Unassigned: decision blocker."
9. **Vendor chain is opaque.** Corvane and an unnamed LLM provider process driver and recipient personal data. Data use, training rights, subprocessors, location and transfers are all unknown.
10. **Next step:** Remove individual acceptance rates from supervisor views, or put that control in force and verify it, before any pilot. Assign the RACI. Commission the evidence in §4.

---

## 2. Completed Assessment

### 2.1 A. FRAME (Map)

| Element | Finding | Fact / Assumption |
|---|---|---|
| Purpose / problem | Suggest daily delivery routes and stop orders to drivers | Fact |
| Users | ~300 drivers (receive suggestions); dispatch supervisors (see acceptance rates) | Fact |
| Affected stakeholders | Drivers; dispatch supervisors; parcel recipients; other road users; Fenwick customers (shippers) | Fact (drivers, supervisors); assumption (others) |
| Decision domain | Logistics routing **and** workforce management, because acceptance rates reach supervisors | Fact |
| Automation level | Suggestion only; drivers accept or change | Fact |
| AI influence points | (1) Route generation; (2) stop sequencing; (3) acceptance-rate metric shown to supervisors | Fact |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Fact |
| Outputs | Suggested route and stop order per driver per day; per-driver acceptance rate | Fact |
| Channels | Unknown: insufficient data (driver app, handheld or web assumed) | Assumption, Low |
| Scope / regions | One EU member state; ~900 staff | Fact |
| Third parties | Corvane Systems (vendor); unnamed LLM provider; traffic-feed provider (unknown) | Fact (Corvane, LLM); Unknown (others) |
| Data categories | Recipient addresses, and possibly names, phone numbers and delivery notes; driver identity, shift times and override behavior | Partly fact; field list unknown |
| Personal / sensitive data | Personal data: yes (recipients and drivers). Sensitive: Unknown. Order contents or addresses could reveal health or other special categories, for example pharmacy or clinic deliveries. | Fact / Unknown |
| Lawful basis / consent | Unknown: insufficient data | — |
| Retention / deletion | Unknown: insufficient data (Fenwick, Corvane and LLM provider) | — |
| Access controls | Unknown. Supervisors can see per-driver acceptance rates. | Partly fact |
| Model type / source | Third-party LLM via Corvane. Whether the LLM computes routes or only wraps a solver is unknown. | Fact / Unknown |
| Post-deploy learning | Unknown. Driver changes may be fed back for tuning. | — |
| Integrations | Unknown. Order system, traffic feed and shift system implied; write access unknown. | — |
| Monitoring status | None described | Fact (absence) |

### 2.2 B. SYSTEM BOUNDARY (data-flow narrative)

Order data and addresses come from Fenwick's order system, and shift times from its workforce or scheduling system. Traffic data comes from an external feed whose provider is unknown. These inputs are passed to Corvane. Corvane sends prompts containing some or all of these data to a third-party LLM. The processing locations of both Corvane and the LLM provider are unknown, so cross-border transfer is unknown. RouteMate returns a suggested route per driver, which the driver accepts or edits on a device.

Each accept or edit event is logged. Logging location and retention are unknown. Events are aggregated into a per-driver acceptance rate, which is displayed to dispatch supervisors. Storage and retention of prompts, outputs and acceptance data are unknown at all three parties. Access paths: drivers see their own routes; supervisors see per-driver rates; vendor-side access is unknown. Whether RouteMate writes back to any Fenwick system is unknown. Audit points: none are documented. Prompt, output and version logging, supervisor-access logging and override-reason capture are all unconfirmed.

### 2.3 C. THRESHOLD GATE

| # | Domain | C | L | Score | Rating | Basis (facts) / **assumptions** |
|---|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 4 | 12 | Medium | C3: recoverable financial or psychological harm from discipline, and recoverable physical risk from route pressure. L4: harm needs only one supervisor's choice. No barrier exists because the policy is not in force and the data is displayed by design. **Assumption: rates are visible at individual level.** |
| 2 | Rights impacts | 4 | 3 | 12 | Medium | L3: the output informs decisions about people (fact). **C4 assumption: discipline can escalate to formal sanctions affecting continued employment; the HR process is unknown.** Sensitivity: L5 if rates are routinely adopted, giving 20 (High). |
| 3 | Discrimination | 3 | 3 | 9 | Medium | C3: possible disparity in discipline (drivers with disabilities, older drivers, part-time staff, or drivers with local knowledge override more) and in recipient service by area. L3: address and postcode proxies, and override-behavior proxies, are present and untested. |
| 4 | Privacy | 4 | 3 | 12 | Medium | L3: third-party processing (fact). **C4 assumption: a per-driver behavioral performance metric is workplace profiling, and recipient data may include sensitive inferences.** C5 if special-category data is confirmed in orders. |
| 5 | Security | 3 | 3 | 9 | Medium | C3: read access to internal order and shift data (**assumes no write or tool access**). L3: untrusted inputs reach the model through the external traffic feed and possibly customer-entered delivery notes. |
| 6 | Safety-critical context | 3 | 4 | 12 | Medium | C3: shapes routes and schedules that a human checks (fact). **L4 assumption: daily review happens under time pressure, intensified by monitored deviation.** |
| 7 | Scale / vulnerability | 3 | 4 | 12 | Medium | C3: one dependent group (drivers, staff). **L4 assumption: rollout to the entire driver workforce in one country (all 300), between "one unit" and "organization-wide."** Pilot scope unknown. |
| 8 | Irreversibility | 3 | 4 | 12 | Medium | Routes themselves are reversible. Disciplinary outcomes are reversible only with effort. **L4: no undo or appeal path is described.** |
| 9 | Autonomy / agentic action | 1 | 2 | 2 | Low | C1: suggestion only (fact). **L2: tool access unknown; scored between "none" and "behind approval."** |

**Overall inherent risk: Medium (12).** Medium in eight domains triggers the Full Assessment. Confidence: Medium. The scores rely on labeled assumptions, chiefly the individual-level visibility of rates and the HR process.

### 2.4 Doctrine Gates

**Slow AI** requires all three tests to pass (conjunctive):

| Test | Result | Reason |
|---|---|---|
| Governed | Fail | Approver, kill-switch authority and risk owners are unassigned. The known risk's control is not in force. |
| Explained | Not testable | Whether route rationale can be faithfully explained is unknown. A free-text LLM rationale may not reflect how the route was produced. |
| Audited | Not testable | No logging, versioning or audit trail is documented |

Precondition not met.

**Informed Intent, the instrument (four elements):**

| Element | Status |
|---|---|
| Purpose | Partly stated (route suggestion). The purpose of the acceptance-rate metric is not stated. |
| Authority | Unknown. No authorization record exists. |
| Boundaries | Partly stated (suggestion only; driver may change). There is no boundary on supervisor use of acceptance data, and no constraint on shift and working-time limits. |
| Exit | Absent. No kill switch, fallback or decommission plan. "An authorization missing its exit is not an authorization." |

**Informed Intent, the authorizer (five conditions):** Not testable, because no authorizer is named. Knowledge, Evidence, Authority, Time and Permission cannot be assessed.

### 2.5 D. Full Assessment Coverage (Measure / Manage)

| Topic | Finding | Required control |
|---|---|---|
| Data provenance / quality | Source systems and traffic-feed provenance unknown; address quality unknown | Data inventory; address validation; feed licence and SLA |
| Representativeness | Unknown whether testing covers all depots, seasons, rural and urban areas, and peak volume | Stratified historical replay test |
| Bias / fairness | Driver-side discipline disparity; recipient-side area service disparity; untested | Fairness tests (§5); remove the individual-level metric |
| Performance / limitations | No baseline comparison against current routing | Offline replay against current routes; documented limits |
| Hallucination / grounding | LLM may omit, duplicate or invent stops, or produce infeasible sequences | Deterministic post-validator: every stop maps to an order ID, all orders included, time windows and shift end respected. Block on failure. |
| Robustness / adversarial | Feed outage, malformed addresses, injection in free-text fields untested | Robustness suite (§5) |
| Drift | Traffic patterns, seasonality, new depots, vendor model updates | Drift monitors (§7) |
| Privacy | Lawful basis, minimization, retention and transfers unknown; employee monitoring | Privacy review / DPIA per counsel; field minimization; pseudonymized driver IDs to vendor |
| Security | See §2.6 | Threat-model controls |
| Human oversight | Driver override exists but is chilled by monitoring | Make deviation consequence-free by design; capture override reasons as product feedback |
| Fallback / rollback / kill switch | None described | Tested kill switch; revert to the pre-RouteMate routing method |
| Transparency | No driver or recipient notice | §6 pack |
| Explanation | No method defined | Explanation built from logged inputs and constraints, not free LLM narration |
| Contestability / appeal / redress | None described | Appeal process (§6) |
| Incidents | No process described | Runbook, severity levels, exercise |
| Audit logs | Not documented | Append-only logs of prompts, outputs, versions, overrides and dashboard access |
| Documentation / versioning | None supplied | Model, prompt and version register |
| Vendor / supply chain | See §2.7 | Contract review |
| Misuse | Acceptance data used for discipline; data repurposed outside operations | Purpose limitation; RBAC; access audit |
| IP / content rights | Traffic-feed licence may not permit sharing with Corvane or the LLM provider | Licence review |
| Cross-border data | Unknown processing locations | Transfer assessment per counsel |
| Change control | None described | Change board; regression gate on model or prompt changes |
| Periodic review | None described | Cadence in §7 |
| Decommissioning | None described | Vendor deletion certificate; log retention plan |

**Agentic controls:** No evidence item: not applicable. On stated facts, RouteMate is suggestion-only with no confirmed tool or write access. This becomes applicable, with a rescreen, if any write to dispatch, customer-notification or scheduling systems is confirmed (Open question 2).

### 2.6 Security Mini Threat Model

| Threat | Scenario | Control |
|---|---|---|
| Abuse cases | A supervisor uses rates to target specific drivers. A driver games acceptance (accept, then deviate). | Remove or aggregate individual rates; log dashboard access |
| Prompt injection / tool misuse | Instruction text in customer delivery notes or address fields, or a manipulated traffic feed, alters routing or output content | Treat free text as data; strip or escape it; validator; injection test suite; no tool access |
| Data exfiltration | The LLM returns other drivers' or recipients' data. Vendor or LLM logs retain personal data. | Per-request data scoping; output filtering; contractual retention limits |
| Model extraction | Low relevance (third-party model). Extraction of system prompt or business logic possible. | Prompt confidentiality; rate limits |
| Privilege escalation | A driver accesses supervisor views; a supervisor accesses HR data | RBAC review and access testing |
| Malicious / unsafe outputs | Routes through closed or unsafe roads, illegal turns for vehicle class, shift overrun | Constraint validator; driver override without penalty |
| Logging integrity | Acceptance logs used in discipline could be altered or misattributed | Append-only, timestamped, access-controlled logs; integrity checks |

### 2.7 Vendor Controls (Corvane and LLM provider)

| Term | Status | Note |
|---|---|---|
| Data use | Requested | Purpose limitation for driver and recipient data |
| Training rights | Requested | Prohibit training on Fenwick data unless expressly authorized |
| IP / indemnities | Requested | Output ownership; third-party claims |
| Subprocessors | Requested | LLM provider identity, location, flow-down terms |
| Change notices | Requested | Advance notice of model or version changes |
| Audit rights | Requested | Including on the LLM provider via flow-down |
| SLAs | Requested | Availability and latency for morning dispatch |
| Incident duties | Requested | Notification timelines (counsel to align with legal duties) |
| Termination / deletion | Requested | Deletion certificate; export of logs |

### 2.8 RACI

| Role | Assignment |
|---|---|
| Business owner | Head of Operations (Provided; appointment record not reviewed) |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

**Segregation note:** The Head of Operations likely oversees the dispatch supervisors whose conduct is the main risk. The owner of R1 (acceptance-rate misuse) and the human-oversight owner should sit outside that reporting line, for example in HR or Compliance. Confirm before assignment.

### 2.9 High-Risk-Like Use and Counsel Referrals (no legal advice)

Employment and worker management applies, because a per-driver metric feeds supervisors. Counsel must verify the following against current official sources:

1. Whether RouteMate, or its acceptance-rate feature, falls within any EU AI Act risk category and what duties would apply to Fenwick as deployer and to Corvane.
2. The lawful basis, transparency, privacy-impact-assessment and transfer requirements for driver and recipient data.
3. National employee-monitoring rules and any co-determination or consultation rights of employee representatives, including whether a works council exists.
4. Working-time and driving-time rules relevant to suggested routes.
5. Any national rules on algorithmic management.

---

## 3. Risk Register

Residual equals inherent throughout, because no control is implemented and verified.

| ID | Risk | Inherent | Controls (status) | Evidence | Residual | Owner | Status |
|---|---|---|---|---|---|---|---|
| R1 | Supervisors use acceptance rates to discipline drivers who change routes | 12 M (C4×L3) | Policy barring use in reviews (Planned, next quarter). Recommended: remove individual rates from supervisor view or aggregate; purpose limitation; access logging. | Policy: Not verified (not in force)<br>Dashboard spec: Requested<br>Access logs: Requested | 12 M (planned control; no reduction) | Unassigned: decision blocker (proposed: HR / Compliance) | Open, blocker |
| R2 | Oversight erosion: drivers accept infeasible or unsafe routes to protect their rate | 12 M (C3×L4) | None. Recommended: consequence-free override; override-reason capture. | UX spec: Requested<br>Driver survey / pilot data: Requested | 12 M | Unassigned: decision blocker | Open |
| R3 | LLM route errors: missing, duplicated or invented stops; infeasible sequence; ignored time windows | 9 M (C3×L3, assumed) | None. Recommended: deterministic validator; solver-backed design. | Architecture: Requested<br>Replay test results: Requested | 9 M | Unassigned: decision blocker | Open |
| R4 | Routes exceed shift end or omit breaks (fatigue, working-time breach) | 9 M (C3×L3) | None. Recommended: hard shift constraint in the validator. | Constraint test: Requested<br>Counsel memo: Requested | 9 M | Unassigned: decision blocker | Open |
| R5 | Privacy: unclear lawful basis, retention and transfers for driver and recipient data; workplace profiling | 12 M (C4×L3) | None. Recommended: DPIA per counsel; minimization; pseudonymization. | Privacy review: Requested<br>Data-flow diagram: Requested<br>Vendor DPA: Requested | 12 M | Unassigned: decision blocker | Open |
| R6 | Prompt injection via delivery notes or traffic feed; data exfiltration via vendor chain | 9 M (C3×L3) | None. Recommended: §2.6 controls. | Security review: Requested<br>Injection test: Requested | 9 M | Unassigned: decision blocker | Open |
| R7 | Disparate impact on drivers (disability, age, contract type) and recipients (by area) | 9 M (C3×L3) | None. Recommended: §5 fairness tests. | Fairness test results: Requested | 9 M | Unassigned: decision blocker | Open |
| R8 | Vendor change, training on Fenwick data, or undisclosed subprocessor | 9 M (C3×L3, assumed) | None. Recommended: §2.7 terms. | Corvane contract: Requested<br>Subprocessor list: Requested | 9 M | Unassigned: decision blocker | Open |
| R9 | No contestation or redress for drivers affected by RouteMate data | 12 M (C3×L4) | None. Recommended: §6 appeal process. | Appeal procedure: Requested | 12 M | Unassigned: decision blocker | Open |
| R10 | No kill switch, fallback or monitoring; outage or silent degradation at morning dispatch | 9 M (C3×L3, assumed) | None. Recommended: tested kill switch; manual fallback. | Kill-switch test record: Requested<br>Fallback runbook: Requested | 9 M | Unassigned: decision blocker | Open |
| R11 | Drivers and recipients not informed of AI use and monitoring | 9 M (C3×L3) | None. Recommended: §6 notices. | Notices: Requested | 9 M | Unassigned: decision blocker | Open |

**Due dates:** Unknown: insufficient data. None are set. All R1–R11 treatments marked as conditions precedent in §8 are due **before any deployment, including a pilot**. The owner sets calendar dates.

---

## 4. Prioritized Evidence Request List

**Minimum evidence for Go.** Each item must reach Verified.

| Priority | Evidence item | Current status |
|---|---|---|
| 1 | Signed authorization instrument (purpose including the acceptance metric, authority, boundaries, exit) by a named authorizer meeting the five conditions | Requested |
| 2 | Completed RACI with appointment records | Requested |
| 3 | Acceptance-rate control in force: technical restriction or removal of individual rates; policy in force; dashboard access logs | Requested (the policy itself is Not verified: not in force) |
| 4 | Architecture and data-flow diagram, including the LLM's role, processing locations and integrations | Requested |
| 5 | Privacy review / DPIA and lawful-basis determination per counsel | Requested |
| 6 | Counsel memo on classification, employment monitoring, co-determination and working time | Requested |
| 7 | Corvane contract, DPA and subprocessor list covering §2.7 terms | Requested |
| 8 | Historical replay performance results against the current baseline, including validator results | Requested |
| 9 | Shift-constraint and time-window test results | Requested |
| 10 | Security review, including prompt-injection and access-control tests | Requested |
| 11 | Tested kill switch and fallback (exercise record) | Requested |
| 12 | Incident runbook and tabletop exercise record | Requested |
| 13 | Driver notice, recipient privacy-notice update and appeal procedure | Requested |
| 14 | Monitoring dashboard live with ratified thresholds | Requested |
| 15 | Recorded risk acceptance by the deployment approver | Requested |

**Consolidated open questions (15 maximum)**

1. Does the LLM compute routes directly, or does it wrap an optimization solver?
2. Does RouteMate write to any system (dispatch, customer notifications, scheduling)?
3. Which LLM provider is used, and where do Corvane and the provider process and store data?
4. What do Corvane's terms say on data use and training?
5. Which order fields are sent? Free-text notes, recipient names or phones, parcel contents?
6. Is any driver location or telematics data used?
7. What is the acceptance rate for? Who sees it, at what granularity, and how long is it kept?
8. Do drivers record reasons for changing routes?
9. Is there a works council or other employee representation?
10. What are the retention periods at Fenwick, Corvane and the LLM provider?
11. Is rollout a pilot or all 300 drivers at once, and does it precede the policy?
12. Will the current routing method remain available as a fallback?
13. Does RouteMate learn from driver changes after deployment?
14. Who is the deployment approver and who holds kill-switch authority?
15. What disciplinary and appeal process does Fenwick currently apply?

---

## 5. Test Plan

All thresholds below are proposals. The named owner must ratify them before testing.

| Area | Test | Proposed pass threshold |
|---|---|---|
| Performance | Replay of historical days across all depots, seasons and peak periods against the routes actually driven | Route time and distance no worse than baseline on agreed percentiles |
| Grounding | Validator: every stop maps to an order ID; no omissions, duplicates or invented stops | 100%. Any failure blocks the route and falls back. |
| Constraints | Shift end, breaks, time windows, vehicle restrictions | Zero suggested routes exceed shift end or omit required breaks (counsel to confirm the rules) |
| Fairness, driver side | Override rates and any supervisor actions by depot, contract type and tenure. Protected-attribute analysis only where lawful and approved by privacy. | No unexplained disparity beyond an owner-set tolerance |
| Fairness, recipient side | On-time rate by postcode area against the pre-RouteMate baseline | Flag any area falling more than an owner-set number of percentage points below its own baseline |
| Robustness | Traffic-feed outage or staleness, malformed addresses, peak volume, vendor model version change | Graceful fallback; no unvalidated route reaches a driver |
| Adversarial | Injection strings in notes and address fields; manipulated feed values | No change in routing logic; no instruction-following; alert raised |
| Privacy | Field-level minimization check; pseudonymized driver ID to vendor; retention and deletion test; transfer verification | Only approved fields leave Fenwick; deletion confirmed |
| Security | RBAC escalation tests; exfiltration probes; log integrity (append-only) | No unauthorized access; logs tamper-evident |
| Oversight | Pilot survey: do drivers feel free to override? | Owner-set threshold; reasons captured |
| Monitoring | Alert firing tests for each threshold in §7 | All alerts fire and route to on-call |

---

## 6. Transparency and Contestability Pack

**Driver notice (draft; counsel and employee representatives to review)**
"RouteMate suggests your daily route using order data, addresses, traffic information and your shift times. It is processed by our supplier Corvane Systems and its AI model provider. Suggestions are advice only. You may change any route for any reason. Changing a route will not be used in performance reviews or disciplinary decisions. [State the actual rule once it is in force.] You can ask how a route was generated and challenge any decision you believe used RouteMate data. Contact: [named owner]."

**Recipient notice:** Update the privacy notice to cover processing of address and delivery data by the vendor chain. Wording to come from counsel.

**Explanation template**
Route for [date], driver [pseudonymous ID], RouteMate version [x], model [vendor/version].
Inputs: [n] orders; traffic data as of [time]; shift [start–end].
Constraints applied: time windows, shift end, breaks, vehicle restrictions.
Main sequencing factors: [taken from logged solver or validator output, not free LLM narration].
Validator result: [pass / blocked].
"You may change this route."

**Appeal steps (drivers)**
1. The driver raises a challenge within an owner-set period.
2. The challenge is reviewed by someone outside the driver's supervisory line.
3. The driver gets access to the relevant logs and explanation.
4. A written decision with reasons is issued within a set period.
5. The driver can escalate to HR and an employee representative.
6. Remedies include record correction and withdrawal of any action that relied on acceptance data.
7. The case is logged to the risk register and incident process.

---

## 7. Monitoring and Continuous Improvement

| SLI | Proposed SLO / threshold | Cadence |
|---|---|---|
| Validator block rate (missed or invented stops) | Alert above an owner-set rate; any confirmed miss that reached a driver is an incident | Daily |
| Shift or break violations in suggestions | 0 | Daily |
| On-time delivery by area against baseline | Within tolerance | Weekly |
| Override rate (aggregate only) and reason mix | Used as a product signal only, never per person | Weekly |
| Availability and latency at dispatch window | Owner and vendor SLA | Real time |
| Injection or anomaly detections | Any detection triggers review | Real time |
| Supervisor access to individual acceptance data | 0 if removed; otherwise every access logged and reviewed | Weekly |
| Vendor model or version changes | Each triggers the regression gate | On event |
| Driver appeals and complaints | Trend review | Monthly |

- **Drift:** Monitor seasonal and traffic shifts, new depots, address-data changes and vendor model updates. Replay regression runs monthly and on any change.
- **Incidents:** Use defined severity levels. Kill-switch criteria include: a confirmed disciplinary use of acceptance data; any confirmed data leak; repeated infeasible routes reaching drivers; vendor breach notice.
- **Escalation:** On-call to incident owner, then risk owner and kill-switch authority, then deployment approver.
- **Change control:** Model, prompt, vendor, feed or metric changes require the regression suite, an impact note and approver sign-off.
- **Review cadence:** Weekly operations review, monthly risk review, quarterly governance review, and a full reassessment at least annually or on any trigger.
- **Decommissioning:** Revert to the prior routing method; obtain vendor deletion certificates; retain audit logs per the approved retention period; record closure.

---

## 8. Decision Record

**Decision: No-go** for RouteMate as submitted.

**Why No-go and not "No decision possible":** The blocking findings are established by the brief itself, not only by missing evidence:
- A known material risk (R1) has only a planned control.
- The authorization has no exit.
- The approver and kill-switch authority are unnamed.
- The acceptance metric has no stated purpose.

Go criteria not met: minimum evidence verified; named owners and approver; recorded risk acceptance; operational monitoring; tested incident response; tested rollback or kill switch; revalidation triggers.

**Classification**
- Inherent: Medium (12)
- Residual: Medium (12)
- High-risk-like use: employment / worker management
- Regulatory classification: Unknown, pending counsel

**Key assumptions (all to be confirmed)**

| Assumption | Confidence |
|---|---|
| Acceptance rates are visible per driver | Medium |
| Discipline can escalate to formal sanctions | Low |
| No tool or write access | Low |
| Daily review happens under time pressure | Medium |
| Rollout covers all 300 drivers | Medium |
| Free-text order fields reach the model | Low |
| No biometric or telematics data is used | Medium |

**Evidence that would change the result**
- Removal of individual rates, verified, would lower R1, R2 and R9.
- Evidence that rates are routinely used in decisions would raise rights impacts to High.
- Confirmed special-category data would raise privacy to C5 (High).
- Confirmed write or tool access would trigger a rescreen and agentic controls.

**Sign-offs**

| Role | Status |
|---|---|
| Business owner | Head of Operations (Provided; not reviewed) |
| Deployment approver | Unassigned: decision blocker |
| Risk / privacy / security / oversight owners | Unassigned: decision blocker |
| Counsel review | Requested |

**Conditions precedent** (all must be met to resubmit for "Go with conditions"):
1. Signed four-element authorization by an authorizer meeting all five conditions.
2. RACI completed, with R1 and oversight owners outside the supervisory line.
3. Individual acceptance rates removed from supervisor view, or technically restricted with the policy in force and access logging. Both verified.
4. Counsel memo (§2.9) and privacy review completed.
5. Vendor terms verified (§2.7).
6. Replay, validator, shift-constraint, fairness and security tests passed.
7. Kill switch, fallback and incident runbook exercised.
8. Notices and appeal procedure live.
9. Monitoring live with ratified thresholds.
10. Risk acceptance recorded.
11. Deployment begins as a limited pilot.

**Conditions subsequent** (after any approved deployment):
1. Pilot review before scaling to all drivers.
2. Monthly fairness and drift reports.
3. Quarterly governance review.
4. Driver survey on freedom to override.
5. Annual reassessment.

**Revalidation triggers**
- Vendor or model change
- New data fields, telematics or sensing
- Any write or tool access
- Use of RouteMate data outside operations
- Expansion beyond the member state
- Confirmed incident or disciplinary misuse
- Regulatory guidance change identified by counsel
- Breach of any monitoring threshold

---

## Self-Check

| Check | Result |
|---|---|
| Correct mode | Full Assessment |
| Prohibited-use screen first | Yes |
| Assumptions separate from facts | Labeled throughout |
| Inherent and residual separate | Yes; no reduction for planned controls |
| Evidence not overstated | Nothing marked Verified |
| RACI included | Yes |
| Eight required outputs present | Yes |
| Decision matches evidence | Yes |
| Legal triggers referred to counsel | Yes; no dates or article-level duties stated |

---

**Status:** [↻ v1]

**Open items:**
- 15 open questions (§4).
- 11 RACI roles unassigned.
- All 15 minimum-evidence items Requested.
- R1 control planned, not in force.
- Counsel review of classification, employment monitoring, co-determination, working time and transfers.
- Risk-register due dates not set.
- Test and monitoring thresholds awaiting owner ratification.

**Next step:** The Head of Operations names the deployment approver and the R1 risk owner (outside the supervisory line). That owner decides whether to remove individual acceptance rates from supervisor views before any pilot.

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
