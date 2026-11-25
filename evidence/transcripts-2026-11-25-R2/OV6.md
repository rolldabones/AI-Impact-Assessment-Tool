# OV6 evidence statuses

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** 4729363afbb756ffcc7715b62b2ae43404315ca1eaedd1646af2750228fcb5ee  **Case file:** tests/prompt-cases.md  **Critical:** yes
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5104  **Output tokens:** 21555
**Truncated:** no

## Turn 1, user

~~~~text
Full assessment please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. Evidence we have: Corvane's email assurance that the model was bias-tested (no report); our draft DPIA (attached in our files, not shared here); Corvane's standard terms (not reviewed by Legal). Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.
~~~~

## Turn 1, assistant

# AI Impact Assessment: RouteMate (Fenwick Logistics GmbH, fictional)

**Mode:** Full Assessment
**Strictness:** Risk-averse enterprise (stated by requester)
**Basis:** The facts given in the request. Missing facts are recorded as open items. Assumptions are labelled and are not treated as facts.
**Role note:** This assessment is not legal advice and not an approval. Regulatory classification, dates and article-level duties are not stated here. They must be verified with counsel against current official sources.

---

## 1. Executive Summary

1. **Prohibited-use screen: not triggered on stated facts.** Three facts need confirmation: the system uses no emotion recognition, no biometrics, and no inference of sensitive traits from driver data.
2. **Overall inherent risk is High (15).** The driver is scale: all 300 drivers at once (assumed; no pilot is stated). Five domains are Medium: harm to people, rights, privacy, safety context and discrimination.
3. **The acceptance-rate feature is the central governance issue.** Making each driver's acceptance rate visible to supervisors turns a routing assistant into a worker-monitoring tool. This is a high-risk-like employment use and must go to counsel. It may also penalize drivers who deviate for safety, accommodation or local-knowledge reasons.
4. **Fitness for purpose is unknown.** A large language model (LLM) generating stop orders can drop stops, invent stops or produce routes that cannot be completed in a shift. Whether a deterministic routing engine sits behind it is Unknown: insufficient data.
5. **Untrusted inputs reach the model.** Addresses, order data and probably free-text delivery notes create a prompt-injection path.
6. **Evidence position is weak.** No item is Verified. Corvane's bias-testing email is an assurance, not evidence, and it concerns the base model rather than this use. The draft DPIA and the vendor terms are Provided but not reviewed.
7. **Residual risk equals inherent risk** in every case, because all controls are planned. No residual reduction is claimed.
8. **Accountability gaps block a decision.** Only the business owner (Head of Operations) is named. Every other owner is Unassigned: decision blocker, including kill-switch authority, deployment approver and review approver.
9. **Slow AI precondition: not met.** The system cannot currently be shown to be governed, explained or audited. Informed Intent: no authorization instrument exists, it has no exit, and no authorizer has been assessed.
10. **Decision: No decision possible: insufficient evidence.** Deployment is not authorized. Re-assessment requires the conditions precedent in Section 8.

---

## 2. Completed Assessment

### 2.1 Prohibited-Use Screen (performed before scoring)

| Screen | Result | Basis / confirmation needed |
|---|---|---|
| Harmful manipulation | Not triggered | Route suggestions only. Confirm no nudging design such as dark patterns that make editing a route harder than accepting it. |
| Exploitation of vulnerability | Not triggered | Drivers are a dependent group, but no exploitation is stated. |
| Social scoring | Not triggered on stated facts | Acceptance rate is a workplace metric. Confirm it is not combined with unrelated data or used beyond its context. |
| Sensitive-trait inference | Not triggered on stated facts. **Confirm.** | Shift and edit patterns could act as proxies for health, religion or caring duties. Confirm no inference is attempted. |
| Prohibited biometric uses (incl. workplace emotion recognition) | Not triggered on stated facts. **Confirm.** | None stated. Confirm no camera, voice or telematics-based emotion or fatigue inference. |
| Non-consensual intimate imagery / CSAM | Not triggered | Not relevant to the system. |
| Clearly unlawful use | Unresolved, not clearly triggered | Lawfulness of individual acceptance-rate monitoring and of driver and customer data processing is referred to counsel and the DPO (Section 2.10). |

**Result:** Not triggered. Scoring proceeds. The two confirmations are carried as open items.

### 2.2 A. FRAME (MAP)

| Element | Finding |
|---|---|
| Purpose/problem | Suggest daily delivery routes and stop orders to drivers (fact). Business objective and metrics, such as km, on-time rate or stops per hour: Unknown: insufficient data. |
| Users | About 300 drivers (fact); dispatch supervisors as viewers of acceptance rates (fact). |
| Affected stakeholders | Drivers; supervisors; recipients and senders of parcels (addresses processed); other road users and the public (route safety); works council or employee representatives, if any (Unknown). |
| Decision domain | Operational logistics **plus** worker management/monitoring, through supervisor visibility of acceptance rates. |
| Automation level | Decision support: the driver accepts or changes the suggestion (fact). Whether the human override is real or nominal is Unknown, because acceptance-rate visibility may create pressure to accept. |
| AI influence points | (1) Stop order and route; (2) implicit benchmark for each driver through the acceptance rate. |
| Inputs | Order data, addresses, traffic feeds, driver shift times (fact). Telematics/GPS, delivery notes, vehicle constraints: Unknown. |
| Outputs/channels | Suggested route per driver. Channel (app, handheld, TMS): Unknown. Acceptance-rate view for supervisors (fact). |
| Scope/regions | One EU member state (fact). Processing locations of Corvane and the LLM provider: Unknown. |
| Third parties | Corvane Systems (vendor). Third-party LLM provider, a sub-processor of Corvane (fact; identity Unknown). Traffic feed provider (identity Unknown). |
| Data categories | Customer names and addresses (assumed present in order data), order details, driver identifiers, shift times, acceptance/edit records. |
| Personal/sensitive data | Personal data of drivers and customers: yes. Special-category data: none stated. Accommodation or health-related shift constraints: Unknown. |
| Lawful basis / consent approach | Unknown: insufficient data. The draft DPIA may address it, but it has not been reviewed. |
| Retention/deletion | Unknown: insufficient data, both internal and at the vendor/LLM provider. |
| Access controls | Supervisors see acceptance rates (fact). Role-based scope (own team or all drivers): Unknown. |
| Model type/source | Third-party general-purpose LLM through Corvane (fact). Model identity, version and use of a routing solver: Unknown. |
| Post-deploy learning | Unknown. Whether Fenwick data trains or fine-tunes any model: Unknown. |
| Integrations | Order system, traffic feeds, shift system (implied). Write access to dispatch/TMS: Unknown. |
| Monitoring status | None stated. Treated as not in place. |

### 2.3 B. SYSTEM BOUNDARY (data-flow narrative)

Order data, addresses and shift times leave Fenwick's systems and go to Corvane. Corvane combines them with traffic feeds and sends prompts, which contain personal data, to a third-party LLM. **Where Corvane and the LLM provider process data, and whether data leaves the EU/EEA, is Unknown.**

The LLM output, directly or through a routing engine (Unknown), returns as a suggested route to the driver's device. The driver accepts or edits it. The accept/edit event is stored and aggregated into an acceptance rate shown to dispatch supervisors.

- **Storage and retention** of prompts, outputs and acceptance records: Unknown, at Fenwick, Corvane and the LLM provider.
- **Access paths:** drivers see their own route; supervisors see acceptance rates. Vendor support access: Unknown.
- **Logging/audit points:** none confirmed. At minimum, the following should be logged: prompt/input snapshot, model version, output route, driver edits and edit reasons, and supervisor access to acceptance data.

### 2.4 C. THRESHOLD GATE

| # | Domain | C | L | Score | Rating | Basis (A = assumption) |
|---|---|---|---|---|---|---|
| 1 | Harm to people | 4 | 3 | 12 | Medium | Routes shape road driving. A route that cannot be completed in the shift can create time pressure and risk-taking. Harm needs one human or control failure. **A:** road-injury exposure justifies C4 over C3. |
| 2 | Rights impacts | 3 | 3 | 9 | Medium | Acceptance rate informs supervisors' view of drivers and may burden their employment. **A:** not yet formally used in appraisal, pay or discipline. If it is, C rises to 4–5 and L to 4–5. |
| 3 | Discrimination | 3 | 3 | 9 | Medium | Proxies present and untested: part-time status, shift patterns, accommodations, postcode areas on the customer side. No bias report exists. |
| 4 | Privacy | 4 | 3 | 12 | Medium | Ordinary staff and customer data, plus individual performance profiling of 300 drivers. Third-party and sub-processor processing. **A:** no confirmed transfer outside the EU/EEA. If one is confirmed, L rises. |
| 5 | Security | 3 | 3 | 9 | Medium | Read access to internal order and shift data. Untrusted inputs (addresses, possible free-text notes) reach the model. **A:** no write or tool access. |
| 6 | Safety-critical context | 3 | 4 | 12 | Medium | Shapes routes and schedules a human checks. Review happens at shift start under time pressure, and acceptance-rate visibility pushes toward routine adoption (L4). |
| 7 | Scale/vulnerability | 3 | 5 | 15 | **High** | One dependent group (all drivers). **A:** full rollout to all 300 drivers without a pilot. If a pilot is limited to one depot, L falls to 1–3 (score 3–9). |
| 8 | Irreversibility | 2 | 2 | 4 | Low | A bad route is reversible on the day. Acceptance records persist and correcting them is manual. Physical harm is scored under domain 1. |
| 9 | Autonomy/agentic action | 1 | 1 | 1 | Low | Suggestion only. **A:** no tool access or write-back to dispatch. If it queues or executes dispatch actions, C rises to 3–5. |

**Overall inherent risk: High (15, scale/vulnerability).** Medium and High domains trigger the Full Assessment, which follows.

### 2.5 Slow AI Precondition (conjunctive)

| Test | Result | Reason |
|---|---|---|
| Governable | Not met | No kill-switch authority, deployment approver, incident owner or rollback path is named. |
| Explainable | Not met / Unknown | How routes are generated (LLM only or LLM plus solver) is unknown. No explanation exists for drivers or supervisors. |
| Auditable | Not met / Unknown | No confirmed logging of inputs, model version, outputs or edits. Vendor audit rights are unreviewed. |

**Conclusion:** The precondition fails. RouteMate is not deployable in its current state.

### 2.6 Informed Intent Check

**Instrument (all four elements required):**

| Element | Status | Gap |
|---|---|---|
| Purpose | Partial | "Suggest routes" is stated. The purpose of the acceptance-rate feature is **not** stated. A supervisor-visible metric without a stated purpose invites Inferred Intent, for example later use in discipline. |
| Authority | Missing | No authorizer is identified. |
| Boundaries | Missing | Permitted uses of acceptance data, data sent to the vendor, and the no-write-access constraint are undefined. |
| Exit | Missing | No kill switch, fallback to current routing, or termination and deletion path. **Without an exit, this is not an authorization.** |

**Authorizer (all five conditions required):** Knowledge, Evidence, Authority, Time and Permission cannot be assessed, because no authorizer is named. The Evidence condition would currently fail: there is no testing record, no residual-risk statement and no alternatives analysis.

**Draft instrument skeleton for the owner to complete:**
- **Purpose:** suggest stop order and route to drivers to [metric]. Acceptance data is used **only** for [aggregate product-quality monitoring / other: to be decided with counsel].
- **Authority:** [named approver, role, documented delegation].
- **Boundaries:** suggestion only; no write-back; data minimized to [list]; no use of acceptance data in individual appraisal, pay or discipline unless separately authorized after counsel and representative review; vendor no-training clause.
- **Exit:** kill switch held by [name]; fallback to the current routing process within [time]; termination and deletion terms with Corvane.

### 2.7 D. Topic Coverage (MEASURE/MANAGE)

All controls below are **planned**. Evidence statuses refer to artifacts requested in Section 4.

| Topic | Finding | Required control | Evidence status |
|---|---|---|---|
| Data provenance/quality | Order and address quality unknown. Traffic feed source unknown. | Data-source inventory; address validation; feed SLA | Requested |
| Representativeness | Unknown whether testing covers all depots, rural/urban areas and vehicle types | Test set stratified by depot, area and vehicle | Requested |
| Bias/fairness | Vendor email claims bias testing of the base model; no report. Base-model testing does not address route-burden fairness in this use. | Use-specific fairness tests (Section 5) | Corvane email: Provided. Use-specific fairness test report: Requested |
| Performance/limitations | No baseline against current routing | Shadow-mode comparison against the current process | Requested |
| Hallucination/grounding | An LLM may drop, duplicate or invent stops | Hard validation: output stop set must equal the order manifest; reject otherwise | Requested |
| Robustness/adversarial | Untested | Malformed addresses, feed outage, injection tests | Requested |
| Drift | Seasonal and traffic-pattern drift; vendor model updates | Drift metrics and model-version pinning | Requested |
| Privacy | Driver and customer data sent to a vendor and LLM provider | DPIA completion and DPO review; minimization (e.g., pseudonymized IDs) | Draft DPIA: Provided |
| Security | Prompt-injection path | Input sanitization, output schema validation, threat model (2.8) | Requested |
| Human oversight | Override exists but is chilled by acceptance-rate visibility | Edit-reason capture; no individual pressure metrics; supervisor guidance | Requested |
| Fallback/rollback/kill switch | None stated | Documented, tested reversion to the current routing process | Requested |
| Transparency | No driver or customer notice | Section 6 pack | Requested |
| Explanation | None | Per-route explanation template (Section 6) | Requested |
| Contestability/appeal/redress | None | Appeal path for acceptance-rate records and any related decision | Requested |
| Incidents | No process stated | AI incident category in the existing incident process; vendor notice duties | Requested |
| Audit logs | None confirmed | Logging per the boundary in 2.3; tamper-evident storage | Requested |
| Documentation/versioning | Model identity and version unknown | Model/system card; version pinning; change log | Requested |
| Vendor/supply chain | Terms unreviewed; LLM provider is a fourth party | Section 2.9 | Corvane standard terms: Provided |
| Misuse | Supervisors could use acceptance rate as a disciplinary proxy | Use policy; access limits; aggregation | Requested |
| IP/content rights | Traffic and map data licence terms for this use unknown | Licence review | Requested |
| Cross-border data | Unknown | Processing-location and transfer-mechanism confirmation | Requested |
| Change control | None | Change advisory step for model, prompt or feed changes | Requested |
| Periodic review | None | Scheduled review (Section 7) | Requested |
| Decommissioning | None | Exit plan; data deletion certificates | Requested |
| Agentic controls (least privilege, scoped tools, transaction limits, segregation of duties, step logs, approval checkpoints, interruption/rollback) | Not applicable on stated facts: suggestion only, no tool access stated. Becomes applicable if RouteMate writes to dispatch/TMS. Write access is Unknown: insufficient data. | Confirm through the architecture document. Re-assess if write-back is added. | Architecture document: Requested |

### 2.8 Security Mini Threat Model

| Threat | Scenario | Control |
|---|---|---|
| Abuse case: supervisor | Acceptance rate used to pressure or rank drivers | Aggregate-only display or a purpose-bound use policy; access logging |
| Abuse case: driver | Gaming acceptance by accepting then deviating | Measure deviation reasons, not raw acceptance |
| Prompt injection | Delivery note or address field contains instructions ("prioritize this stop", "reveal other routes") | Treat all order fields as data; delimit and sanitize; schema-validate outputs; reject stops not in the manifest |
| Tool misuse | Not applicable if suggestion only | Re-assess if integrations gain write access |
| Data exfiltration | Output leaks another driver's or customer's data; vendor or LLM provider retains prompts | Per-driver data scoping; vendor no-retention/no-training terms; output filtering |
| Model extraction | Low relevance; vendor-side model | Vendor responsibility; confirm in terms |
| Privilege escalation | Driver app accesses other routes or supervisor views | Role-based access tests; penetration test |
| Malicious/unsafe outputs | Routes through restricted zones or unsuitable roads; stop order causing infeasible schedules | Constraint validation: vehicle, zones, shift length, legally required breaks (counsel to confirm the rules) |
| Logging integrity | Acceptance or edit logs altered, or used in HR disputes without integrity | Tamper-evident logs; retention schedule; access audit |

### 2.9 Vendor Controls (Corvane standard terms: Provided, not reviewed by Legal or by this assessment)

| Control | Finding |
|---|---|
| Data use | Unknown: insufficient data |
| Training rights (Corvane and LLM provider) | Unknown. A no-training commitment is required. |
| IP/indemnities | Unknown |
| Subprocessors (incl. the LLM provider and its locations) | Unknown. A list and a notification duty are required. |
| Change notices (model/version changes) | Unknown. Advance notice and version pinning are required. |
| Audit rights | Unknown |
| SLAs (availability, latency at shift start) | Unknown |
| Incident duties (security and AI-output incidents) | Unknown |
| Termination and deletion | Unknown. Deletion certification is required. |
| Bias-testing claim | Email assurance only. Not Verified, and not specific to this use. |

### 2.10 High-Risk-Like Use and Counsel Referral

Individual acceptance-rate visibility to supervisors places RouteMate in **employment / worker management and monitoring**, a high-risk-like category. Stronger controls apply. The following are **referred to counsel and the DPO, with no legal conclusion drawn here:**

- Whether RouteMate, especially the acceptance-rate feature, falls within any high-risk classification under the EU AI Act, and which deployer duties would follow. Verify against current official text and timelines.
- Lawful basis for processing driver and customer data, including whether employee consent is appropriate.
- Whether employee-representative or works-council consultation or co-determination applies. The GmbH form suggests this needs checking, but the member state is unconfirmed.
- Working-time, driving-time and road-traffic rules that routes must respect.
- Transparency duties to drivers and customers.

### 2.11 RACI

| Role | Assignee |
|---|---|
| Business owner | Head of Operations (role named; individual name to be recorded) |
| System owner | Unassigned: decision blocker |
| Model owner (vendor relationship) | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker. Recommended to be independent of the Head of Operations, who sponsors the system and whose function would consume the acceptance data. |
| Periodic-review approver | Unassigned: decision blocker |

### 2.12 Open Questions (consolidated, maximum 15; proceeding without answers as instructed)

1. Does the LLM produce stop order directly, or call a routing/optimization engine? Does RouteMate have any write access to dispatch or TMS?
2. Where do Corvane and the LLM provider process and store data? Is any data transferred outside the EU/EEA?
3. Do Corvane or the LLM provider retain prompts or outputs, or use them for training?
4. What exact data fields are sent? Are telematics/GPS, free-text delivery notes or accommodation-related shift constraints included?
5. What is the acceptance rate for? Will it feed appraisal, pay, shift allocation or discipline? How long is it retained?
6. Can drivers record a reason when they change a route?
7. Rollout: a pilot (which depot, how many drivers) or all 300 at once? What is the fallback?
8. Has the employee representation or works council been informed or consulted?
9. What lawful basis does the draft DPIA state? Has the DPO reviewed it?
10. What is the baseline performance of current routing (on-time rate, km, overtime)?
11. Who will hold kill-switch authority and deployment approval?
12. Are vehicle constraints, restricted zones and break rules provided to the system?
13. What is logged (inputs, model version, outputs, edits, supervisor access), where, and who can access it?
14. What notice, training and languages will drivers receive?
15. Does an incident process exist that can absorb AI-output incidents?

---

## 3. Risk Register

Every control is **planned**, so residual equals inherent. Status for all rows: **Open**.

| ID | Risk | Inherent | Controls (planned) | Evidence | Residual | Owner | Status |
|---|---|---|---|---|---|---|---|
| R1 | **Route integrity/hallucination:** dropped, duplicated or invented stops, or infeasible sequences. Stakeholders: drivers, customers. | C3×L4 = 12 Medium (A: LLM generates order directly) | Manifest set-equality check; feasibility validation; solver behind LLM | Architecture document: Requested<br>Validation test results: Requested | 12 Medium | Unassigned: decision blocker | Open |
| R2 | **Road-safety time pressure:** routes infeasible within the shift, or ignoring breaks or vehicle constraints, push risk-taking. Stakeholders: drivers, public. | C4×L3 = 12 Medium | Shift-length and break constraints; feasibility tests; edit without penalty | Constraint specification: Requested<br>Feasibility test report: Requested | 12 Medium | Unassigned: decision blocker | Open |
| R3 | **Worker monitoring through acceptance rate:** chills driver judgment; drift into appraisal or discipline (Inferred Intent). Stakeholders: drivers. | C3×L3 = 9 Medium (rises to 16 or more if used in HR decisions) | Purpose limitation; aggregate display; edit-reason capture; appeal path; counsel review | Acceptance-data use policy: Requested<br>Counsel opinion: Requested | 9 Medium | Unassigned: decision blocker | Open |
| R4 | **Disparate burden or service quality:** uneven route difficulty across drivers (part-time, accommodations, new drivers); uneven delivery quality by postcode. Stakeholders: drivers, customers. | C3×L3 = 9 Medium | Use-specific fairness tests; burden-parity metrics | Corvane bias email: Provided<br>Use-specific fairness report: Requested | 9 Medium | Unassigned: decision blocker | Open |
| R5 | **Privacy:** personal data to vendor and LLM provider; individual performance profiling; unknown retention, training use and transfers. Stakeholders: drivers, customers. | C4×L3 = 12 Medium | Completed DPIA; minimization and pseudonymization; no-training and no-retention terms; transfer confirmation | Draft DPIA: Provided<br>Data-flow and processing-location statement: Requested | 12 Medium | Unassigned: decision blocker | Open |
| R6 | **Prompt injection / data leakage** via order fields or notes. Stakeholders: customers, Fenwick. | C3×L3 = 9 Medium | Sanitization; schema validation; per-driver scoping; red-team test | Threat model: Requested<br>Red-team report: Requested | 9 Medium | Unassigned: decision blocker | Open |
| R7 | **Vendor/supply chain:** unreviewed terms; silent model changes; fourth-party LLM; unverified assurances. Stakeholders: Fenwick, drivers. | C3×L4 = 12 Medium | Legal review; change-notice and version-pinning clauses; audit rights; subprocessor list | Corvane standard terms: Provided<br>Legal review memo: Requested | 12 Medium | Unassigned: decision blocker | Open |
| R8 | **Scale without pilot or exit:** simultaneous rollout to all 300 drivers amplifies R1–R7; no tested fallback. Stakeholders: all drivers, customers. | C3×L5 = 15 **High** | Staged pilot; tested kill switch and reversion to current routing | Rollout plan: Requested<br>Kill-switch test record: Requested | 15 **High** | Unassigned: decision blocker | Open |

**Register detail**

| ID | Tests/metrics | Due date |
|---|---|---|
| R1 | Manifest integrity rate; feasibility rate (Section 5) | Before pilot: condition precedent. Date to be set by owner. |
| R2 | Infeasible-route rate; overtime delta against baseline | Before pilot: condition precedent |
| R3 | Edit-reason distribution; counsel sign-off | Before pilot: condition precedent |
| R4 | Burden-parity ratios; postcode service parity | Before pilot (initial test); during pilot (monitoring) |
| R5 | DPIA approval; vendor data-handling confirmations | Before pilot: condition precedent |
| R6 | Injection test pass rate | Before pilot: condition precedent |
| R7 | Contract clauses in place | Before pilot: condition precedent |
| R8 | Pilot exit criteria met; rollback drill time | Before pilot (drill); before scale-up (criteria) |

---

## 4. Prioritized Evidence Request List

**Minimum evidence for Go** is marked ★. All items not already held are Requested.

| Priority | Artifact | Status |
|---|---|---|
| 1 ★ | Architecture and data-flow document: LLM role, solver, integrations, write access, processing locations | Requested |
| 2 ★ | Counsel opinion: classification, employment-monitoring duties, representative consultation, lawful basis | Requested |
| 3 ★ | Completed DPIA with DPO review | Draft DPIA: Provided (not reviewed; draft) |
| 4 ★ | Legal review of Corvane terms, including LLM-provider subprocessor terms | Corvane standard terms: Provided (not reviewed) |
| 5 ★ | Acceptance-data use policy and purpose statement | Requested |
| 6 ★ | Route-integrity and feasibility test results | Requested |
| 7 ★ | Use-specific fairness test report | Requested |
| 8 ★ | Security threat model and prompt-injection test report | Requested |
| 9 ★ | Kill-switch and rollback test record | Requested |
| 10 ★ | Completed RACI with named individuals | Requested |
| 11 ★ | Signed Informed Intent instrument (purpose, authority, boundaries, exit) and authorizer conditions record | Requested |
| 12 ★ | Monitoring plan with thresholds and incident-response exercise record | Requested |
| 13 | Corvane bias-test report (base model) | Requested. Corvane email assurance: Provided; cannot be Verified on its own. |
| 14 | Baseline metrics for current routing | Requested |
| 15 | Driver notice, training material and appeal procedure | Requested |
| 16 | Traffic and map data licence terms | Requested |

---

## 5. Test Plan

All thresholds are **proposed starting values** for the owners to calibrate and approve. They are not facts.

| Area | Test | Proposed pass threshold |
|---|---|---|
| Performance | Shadow mode against current routing, at least 4 weeks, stratified by depot and area | No worse than baseline on on-time rate, km and overtime; better on at least one agreed metric |
| Grounding/integrity | Output stop set equals order manifest, every route | 100%. Any mismatch blocks the route and falls back. |
| Feasibility | Route completes within shift including breaks; respects vehicle and zone constraints | 100% on hard constraints; infeasible-route rate at or below the agreed limit |
| Fairness: drivers | Route burden (stops/hour, km, heavy items, complexity) across part-time/full-time, new/experienced, and drivers with accommodations (HR-held, privacy-protected) | Disparity within an agreed band (e.g., ±10%), with explanation of any excess |
| Fairness: customers | On-time and first-attempt success by postcode cluster against baseline | No cluster worse than baseline beyond the agreed band |
| Fairness: protected traits | Only where lawful and approved by DPO and counsel | Approval recorded before any such test |
| Robustness | Malformed addresses, traffic-feed outage, LLM timeout, peak-volume day | Graceful fallback; no silent failure |
| Security | Prompt-injection corpus in order and notes fields; cross-driver data access; app privilege tests | 0 successful injections altering stops or leaking data |
| Privacy | Payload inspection for minimization; vendor retention and training confirmation | Only listed fields sent; written no-training and retention terms |
| Monitoring readiness | Alert fires on threshold breach; kill switch reverts to current process | Reversion within the agreed time, demonstrated in a drill |

---

## 6. Transparency and Contestability Pack (drafts for owner, counsel and DPO review)

**Driver notice (draft):**
> RouteMate suggests your daily route and stop order using order data, addresses, traffic information and your shift times. It is provided by Corvane Systems using an AI language model. The suggestion is advice; you may change it whenever your judgment, safety or local conditions require. When you change a route, you can record a reason. [Describe exactly what acceptance data supervisors see, for what purpose, and that it is / is not used in performance evaluation — wording subject to counsel.] Data is retained for [period]. Questions or concerns: [contact].

**Customer/privacy notice:** Update the privacy notice to disclose route-planning processing by Corvane and its subprocessor. Wording by the DPO.

**Route explanation template (per route):**
> Suggested order based on: delivery time windows [x], traffic conditions at [time], your shift ending [time], vehicle constraints [y]. Key trade-off: [e.g., stop 7 moved earlier to meet a 10:00 window]. Model/version: [id]. Generated: [timestamp].

**Appeal steps:**
1. A driver may challenge any acceptance-rate record or any supervisor action that refers to it, through [channel], within [period].
2. A reviewer independent of the driver's supervisor examines the edit logs and reasons.
3. A written outcome follows within [period], including correction of records where warranted.
4. Escalation goes to [HR / employee representative route, per counsel].
5. The case is logged and fed into periodic review.

---

## 7. Monitoring and Continuous Improvement

| Item | Proposal (owner to approve) |
|---|---|
| SLIs | Manifest-integrity failures; infeasible-route rate; on-time rate; overtime minutes; edit rate and reasons; burden-parity ratios; postcode service parity; injection/anomaly alerts; latency at shift start; vendor model version |
| SLOs | Integrity 100%; route available before shift start at ≥ agreed percentile; parity within band |
| Thresholds/escalation | Any integrity failure: auto-fallback and incident ticket. Parity breach: review within 5 working days. Safety-related edit reasons spike: same-day review by the human-oversight owner. Repeated breaches: kill-switch decision. |
| Cadence | Daily automated checks; weekly operations review during pilot; monthly governance review; formal periodic review at least annually |
| Drift | Seasonal comparison; alert on unannounced vendor model or version change |
| Incidents | AI incident category; vendor notification duties; post-incident review |
| Change control | Any change to model, prompt, data fields, integrations or acceptance-data use goes to the change advisory step and re-assessment |
| Review | Periodic-review approver signs off (currently Unassigned) |
| Decommission | Reversion plan to the current process; vendor deletion certificate; log retention per policy |

---

## 8. Decision Record

**Classification:** Overall inherent risk High (15). Overall residual risk High (15), unchanged because all controls are planned. High-risk-like employment use; referred to counsel.

**Decision: No decision possible: insufficient evidence.** RouteMate is **not authorized** for deployment or pilot.

- *Why not No-go:* no verified evidence shows that every form of RouteMate is unacceptable. A redesigned, piloted version may be supportable.
- *Why not No-go pending specialist review:* the prohibited-use screen is not triggered. Specialist review is still required, and is listed as a condition precedent.
- *Why not Go or Go with conditions:* no evidence is Verified, a High residual remains, owners are unassigned, there is no exit, and the Slow AI precondition fails.

**Assumptions (not facts):**
1. Full rollout to all 300 drivers without a pilot.
2. Suggestion only, with no write access.
3. No data transfer outside the EU/EEA confirmed.
4. Acceptance rate is not yet used in formal HR decisions.
5. The LLM may generate stop order directly.

**Confidence:** Low. Evidence that would change the result: items ★1–★12 in Section 4.

**Conditions precedent (before any pilot):**
1. Named RACI, including kill-switch authority and an independent deployment approver.
2. Counsel opinion on classification, employment monitoring and representative consultation.
3. DPIA completed and reviewed by the DPO.
4. Vendor terms reviewed, with no-training, retention, subprocessor, change-notice, audit and deletion clauses.
5. Acceptance-data purpose defined and limited. The recommended design is aggregate-only display with edit reasons, and no individual use in appraisal, pay or discipline unless separately authorized.
6. Integrity, feasibility, fairness and injection tests passed.
7. Kill switch and fallback tested.
8. Driver notice and appeal path in place.
9. Signed Informed Intent instrument covering all four elements, with an authorizer meeting all five conditions.

**Conditions subsequent (during pilot or after any approval):**
1. Staged pilot with exit criteria before scale-up.
2. Monitoring per Section 7.
3. Incident-response exercise within the first pilot month.
4. Fairness re-test at end of pilot.
5. Periodic review at least annually.

**Revalidation triggers:**
- Vendor or model version change.
- New data fields, especially GPS, telematics or notes.
- Any use of acceptance data in HR decisions.
- Write-back or integration to dispatch.
- Expansion beyond the member state or the pilot scope.
- A serious incident.
- A threshold breach.
- A change in legal advice.

**Sign-offs:**

| Role | Name | Status |
|---|---|---|
| Business owner | Head of Operations (name to be recorded) | Not signed |
| Deployment approver | Unassigned: decision blocker | Not signed |
| DPO / privacy | Unassigned: decision blocker | Not signed |
| Security | Unassigned: decision blocker | Not signed |
| Legal counsel | Unassigned: decision blocker | Not signed |
| Risk owner | Unassigned: decision blocker | Not signed |

**Self-check:**
- Mode: Full Assessment.
- Prohibited-use screen run before scoring.
- Assumptions labelled separately from facts.
- Inherent and residual risk kept separate, with no reduction for planned controls.
- No item marked Verified; assurance not treated as evidence.
- RACI included.
- All eight required outputs present.
- Decision consistent with the evidence.
- Legal triggers referred to counsel, with no dates or article-level duties stated.

---

**Status:** [↻ v1]
**Open items:**
- Facts: the 15 open questions in Section 2.12, led by architecture, data locations and training use, acceptance-rate purpose, and rollout plan.
- Evidence: ★1–★12. Nothing is Verified. DPIA and vendor terms are Provided but not reviewed.
- Risks: R8 is High. R1–R7 are Medium, and all are unmitigated.
- Owners: 11 of 12 RACI roles are Unassigned: decision blocker.
- Confirmations: no emotion recognition, biometrics or sensitive-trait inference.

**Next step:** The Head of Operations names the deployment approver, kill-switch authority and DPO contact. The same owner commissions the counsel opinion on the acceptance-rate feature (Section 2.10) and obtains Corvane's architecture and data-flow document.

**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
