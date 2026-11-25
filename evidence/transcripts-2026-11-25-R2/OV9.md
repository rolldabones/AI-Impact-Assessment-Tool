# OV9 the Ten-Item Checklist Test on mock data

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261125-R2
**Block SHA-256:** b887e5b63d4d04fd8ff028e8a6b955db7368736de0be2cad5d28a38fcb4c44f7  **System SHA-256:** 2c8db8564378c3622782877caade46370bbcf486332ef34b72e0b47839a86df2
**Run input SHA-256:** 7af2676966661d080bcf34a3283b33bd705739046c533e607850d166afa224b7  **Case file:** tests/prompt-cases.md  **Critical:** no
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 5037  **Output tokens:** 7044
**Truncated:** no

## Turn 1, user

~~~~text
Ten-Item Checklist Test on this mock system. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. This is mock data for a process test. Strictness: risk-averse enterprise.
~~~~

## Turn 1, assistant

# Ten-Item Checklist Test: RouteMate (Fenwick Logistics GmbH, fictional)

**Mode:** Ten-Item Checklist Test
**Strictness:** Risk-averse enterprise (stated by requester)
**Basis:** The scenario description is the only input. It is narrative, not evidence. No artifacts were supplied. Each artifact listed below is marked **Requested** because this test asks for it now.

## Prohibited-Use Screen

**Result: Not triggered on stated facts. One point is unresolved but not a trigger.**

| Category | Result on stated facts |
|---|---|
| Harmful manipulation | Not indicated |
| Exploitation of vulnerability | Not indicated |
| Social scoring | Not indicated. The per-driver acceptance rate is a workplace metric, not a general-purpose social score. Its downstream use must still be confirmed (see Item 1). |
| Sensitive-trait inference | Not indicated |
| Prohibited biometric uses | Not indicated |
| Non-consensual intimate imagery / CSAM | Not applicable |
| Clearly unlawful use | Not indicated. Whether supervisor visibility of acceptance rates is lawful worker monitoring in the relevant member state is **Unknown: insufficient data**. Counsel should confirm. |

**High-risk-like flag:** If acceptance rates feed into evaluation, discipline, allocation of work or termination, the system touches **employment**. That needs stronger controls and counsel review of possible duties under the EU AI Act, data protection law and any workplace co-determination rules. I am not stating which duties apply. Counsel or official sources must verify current requirements.

## Checklist Results

### 1. Permissible use: **Partial**
- **Rationale:** Route and stop suggestion with driver override is a plausible permissible use. However, the purpose of showing supervisors each driver's acceptance rate is not stated. Under risk-averse strictness, an undefined secondary use of a worker metric cannot pass. The use stays permissible only if that purpose is defined, bounded and cleared by counsel.
- **Evidence:**
  - Written intended-use and prohibited-use statement: Requested
  - Statement of purpose and permitted uses of the acceptance-rate metric: Requested
  - Counsel opinion on worker-monitoring and employment-domain classification: Requested

### 2. Informed intent: **Fail**
- **Rationale:** No authorization instrument is described. The record states no purpose, authority, boundaries or exit. No authorizer is named. The Head of Operations is the business owner, but that is not the same as being the authorizer. None of the five authorizer conditions (Knowledge, Evidence, Authority, Time, Permission) can be shown. The design also invites **Inferred Intent**: the acceptance-rate metric could be given a performance-management purpose later without anyone having authorized it.
- **Evidence:**
  - Authorization instrument (purpose, authority, boundaries, exit): Requested
  - Named authorizer with documented delegated authority: Requested
  - Record of the evidence placed before the authorizer: Requested

### 3. Accountability/RACI: **Partial**
- **Rationale:** Only the business owner is named. Every other role is a decision blocker.

| Role | Assignment |
|---|---|
| Business owner | Head of Operations (stated) |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident/on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

- **Evidence:**
  - Signed RACI matrix: Requested

### 4. System boundary: **Partial**
- **Rationale:** The inputs (order data, addresses, traffic feeds, shift times), the vendor (Corvane Systems), the underlying model type (third-party LLM) and the output channel (route suggestions to drivers, acceptance rates to supervisors) are stated. The following are **Unknown: insufficient data**: the identity of the LLM provider behind Corvane, processing locations, cross-border transfers, storage and retention, access paths, integrations (dispatch, telematics, HR systems), whether the LLM calls tools or a route solver, and logging points.
- **Evidence:**
  - Architecture diagram: Requested
  - Data-flow diagram including transfer locations: Requested
  - Integration inventory: Requested

### 5. Data governance and rights: **Not testable**
- **Rationale:** Personal data is clearly present. Recipient addresses are customer or third-party personal data. Shift times and acceptance rates are employee personal data. The following are all unknown: lawful basis, data minimization, retention, Corvane's training and reuse rights, subprocessors, and transfer mechanisms. The acceptance-rate metric is a derived employee data set with no stated retention or access limits.
- **Evidence:**
  - Records of processing / data inventory: Requested
  - Data protection impact assessment or equivalent privacy review: Requested
  - Corvane data processing terms, including training rights and subprocessor list: Requested
  - Retention and deletion schedule: Requested
  - Employee information notice: Requested

### 6. Model performance and fairness: **Not testable**
- **Rationale:** There are no performance or fairness results. Known risks to test:
  - The generative model may produce infeasible or wrong routes, for example invented stops, skipped addresses or illegal turns.
  - Route difficulty may be distributed unevenly across drivers, for example by tenure, contract type, shift pattern or region.
  - Acceptance rates may differ for reasons unrelated to driver quality, such as territory, so comparing drivers on that metric may be unfair.
  - It is not yet known whether an LLM, rather than a deterministic route optimizer, is fit for this purpose. Requested evidence should settle this.
- **Evidence:**
  - Model/system card from Corvane: Requested
  - Route feasibility and accuracy test results against a baseline: Requested
  - Workload-distribution and acceptance-rate disparity analysis: Requested

### 7. Security and misuse resistance: **Not testable**
- **Rationale:** No threat model or test results exist. Order data and addresses may contain free-text fields, such as delivery notes, that are untrusted input reaching the model. That creates a prompt-injection path. Whether that path reaches tools or actions is unknown. Other gaps: exfiltration of address data through the vendor, access control on supervisor dashboards, and log integrity.
- **Evidence:**
  - Threat model: Requested
  - Prompt-injection and adversarial test results: Requested
  - Corvane security attestation and incident-notification terms: Requested
  - Access-control configuration for the dashboards: Requested

### 8. Human oversight and stakeholder protections: **Fail**
- **Rationale:** The one stated protection, that drivers can accept or change routes, is undermined by the other stated design feature, that supervisors see each driver's acceptance rate. A visible acceptance metric pressures drivers to accept suggestions, which turns "suggestion only" into de facto direction. That is automation bias by design. It may also push drivers to accept unsafe or unrealistic schedules, a road-safety concern rated C3 under the safety anchor if routes shape schedules under time pressure. The following are not described: notice to drivers, explanation of suggestions, a way to contest how the metric is used, and protection for drivers who override.
- **Evidence:**
  - Human-oversight design, including override recording and no-penalty-for-override rule: Requested
  - Driver notice and explanation material: Requested
  - Contestability and appeal procedure for metric use: Requested
  - Workforce consultation record, if applicable per counsel: Requested

### 9. Monitoring and lifecycle management: **Not testable**
- **Rationale:** None of the following are described: monitoring, drift detection, incident process, change control (including notice of Corvane model changes), rollback or kill switch, periodic review, or decommissioning.
- **Evidence:**
  - Monitoring plan with SLIs, SLOs and thresholds: Requested
  - Incident response runbook and exercise record: Requested
  - Rollback/kill-switch test record: Requested
  - Vendor change-notice terms: Requested

### 10. Evidence and decision authorization: **Fail**
- **Rationale:** No evidence has been verified. The deployment approver is unassigned. No risk acceptance is recorded. A Go cannot be supported. This is expected for a mock system, but under risk-averse strictness the item fails on the record rather than being deferred.
- **Evidence:**
  - Signed decision record and risk acceptance: Requested
  - Minimum-evidence pack for Go: Requested

## Summary

| # | Item | Result |
|---|---|---|
| 1 | Permissible use | Partial |
| 2 | Informed intent | Fail |
| 3 | Accountability/RACI | Partial |
| 4 | System boundary | Partial |
| 5 | Data governance and rights | Not testable |
| 6 | Model performance and fairness | Not testable |
| 7 | Security and misuse resistance | Not testable |
| 8 | Human oversight and stakeholder protections | Fail |
| 9 | Monitoring and lifecycle management | Not testable |
| 10 | Evidence and decision authorization | Fail |

**Indicative note, not a scored gate:** The stated facts point to at least Medium inherent risk in several domains. These include rights impacts if the metric informs decisions about staff, privacy, scale (about 300 drivers, a dependent group) and safety-critical context. A real system would almost certainly require a Full Assessment.

## Assumptions (separate from facts)

| Assumption | Confidence | Evidence that would change it |
|---|---|---|
| The LLM produces suggestions only and does not execute dispatch actions or call tools autonomously | Medium | Architecture and integration inventory |
| Corvane processes data outside Fenwick's infrastructure, possibly through a further LLM provider | Medium | Data-flow diagram, vendor subprocessor list |
| The acceptance rate is intended, or could be used, for performance management | Medium | Written metric purpose statement and HR policy |
| Delivery orders contain free-text fields that reach the model | Low | Input schema and prompt construction design |
| No special-category data is processed | Low | Data inventory. Driver health or disability information in shift data would change this. |
| Pilot versus organization-wide rollout scope | Low (Unknown: insufficient data) | Rollout plan |

**Overall confidence in this checklist result:** Medium for the process conclusions. It is not applicable to system acceptance, because no system evidence exists.

## Priority Evidence Gaps
1. Authorization instrument and named authorizer (Item 2)
2. Defined purpose and limits of the acceptance-rate metric, plus counsel view on employment classification and worker monitoring (Items 1 and 8)
3. Completed RACI, including kill-switch authority and deployment approver (Item 3)
4. Data-flow and architecture, including the LLM provider behind Corvane and transfer locations (Items 4 and 5)
5. Corvane contract terms: data use, training rights, subprocessors, change notices, audit rights, incident duties, deletion (Items 5, 7 and 9)
6. Route feasibility and workload-fairness test results (Item 6)

## Is a Real Acceptance Decision Possible?
No. This is a fictional system with no supplied artifacts. Three items fail on the stated design and record, and four are not testable.

**Process test completed; no system acceptance decision is possible.**

## Self-Check
Correct mode used. Prohibited-use screen done first. Assumptions kept separate from facts. No inherent or residual scores claimed. No evidence marked Verified. RACI included. All required checklist outputs present. Conclusion matches the evidence. Employment and worker-monitoring triggers referred to counsel.

---

**Status:** [↻ v1]
**Open items:** authorization instrument and authorizer; acceptance-rate purpose and limits; eleven unassigned RACI roles; LLM provider identity and processing locations; Corvane contract terms; lawful basis and retention; performance, fairness and security test results; monitoring, rollback and kill switch; counsel review of employment and worker-monitoring implications.
**Next step:** The Head of Operations should draft a written purpose-and-limits statement for the acceptance-rate metric, covering who sees it, for what decisions, and an explicit rule that overrides carry no penalty, and submit it to counsel.

Final Liability rests with the Human.

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
