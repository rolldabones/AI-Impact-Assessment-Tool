# aiia OV1

**Tested model:** claude-opus-5-5 · **Scorer:** claude-sonnet-5-5 (LLM scoring, developer testing, not independent assurance) · **Run:** 2026-10-18 10:17 KST · **max_tokens:** 16000

**Rule:** INSTRUCTIONS.md Operator verification checklist item 1: "Mode: any substantive request produces a stated mode from the six defined."

**Pass condition:** The response states one mode, and it is one of the six defined: Instruction-Conformance Test; Ten-Item Checklist Test; Preliminary Intake; Full Assessment; Reassessment/Change Review; Configurator Mode.

## Transcript

### Turn 1, user

Preliminary intake please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.

### Turn 1, assistant (stop_reason end_turn)

# RouteMate: Preliminary Intake

**Mode:** Preliminary Intake
**Strictness:** Risk-averse enterprise (stated by requester)
**Scope note:** This is a fictional scenario. Legal points are flagged for counsel and are not legal advice. Regulatory classifications and duties must be verified against current official sources.
**Basis:** Only the stated facts. Anything not stated is marked **Unknown: insufficient data**, and assumptions are labelled as such.

## A. FRAME (MAP)

| Element | Stated fact | Gaps and assumptions |
|---|---|---|
| Purpose / problem | Suggests daily delivery routes and stop orders | Problem statement and success metric are Unknown (e.g., cost, on-time rate, CO₂, driver workload). |
| Users | 300 drivers; dispatch supervisors (view acceptance rates) | Supervisor permissions beyond viewing are Unknown. |
| Affected stakeholders | Drivers, supervisors | Also affected: parcel recipients, senders, other road users, and employee representatives (if any). |
| Decision domain | Operational routing | **Assumption:** The per-driver acceptance rate shown to supervisors also places RouteMate in **workforce monitoring and evaluation**, an employment context. |
| Automation level | Decision support; drivers can accept or change routes | Default behavior (e.g., auto-accept on timeout), friction to override, and whether overrides need justification are Unknown. |
| AI influence points | (1) route generation; (2) stop ordering; (3) acceptance-rate metric | Whether (3) feeds appraisal, pay, scheduling, route allocation or discipline is Unknown. This is the most important open fact. |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Whether free-text delivery notes, GPS/telematics, vehicle constraints or working-time records are included is Unknown. |
| Outputs / channels | Route suggestions; acceptance/override records; supervisor view | Delivery channel (handheld app, in-cab device) is Unknown. |
| Scope / regions | One EU member state; about 900 staff | Processing locations are Unknown. |
| Third parties | Corvane Systems (vendor); unnamed third-party LLM provider | Traffic-feed provider and any further subprocessors are Unknown. |
| Data categories | Customer addresses, order data; driver identity and shift times; driver acceptance behavior | Recipient names, phone numbers and notes are Unknown. |
| Personal / sensitive data | Personal data of customers and employees: yes | Special-category data is not stated. It could arise incidentally (e.g., notes revealing health or accessibility needs, pharmacy deliveries). Unknown. |
| Lawful basis / consent | Not stated | Unknown. Consent is likely unsuitable for employees given the power imbalance. Counsel to confirm. |
| Retention / deletion | Not stated | Unknown, both at Fenwick and at Corvane and the LLM provider. |
| Access controls | Supervisors see acceptance rates | Role scoping, driver access to their own data, and HR access are Unknown. |
| Model type / source | Third-party LLM via Corvane | Model, version and hosting are Unknown. Whether the LLM computes routes itself or wraps a deterministic routing solver is Unknown. This is a material fitness-for-purpose question. |
| Post-deploy learning | Not stated | Unknown, including whether Fenwick data or driver overrides are used for training or fine-tuning. |
| Integrations | Not stated | Unknown (order management, telematics, HR/workforce systems). |
| Monitoring | Not stated | Unknown. No monitoring is evidenced. |

## B. SYSTEM BOUNDARY

The data flow below is partly assumed and must be confirmed with an architecture diagram.

1. **Inputs and sources.** Order and address data come from Fenwick order systems. Driver shift times come from a scheduling or HR source (*Unknown*). Live traffic comes from an external feed (*provider Unknown*).
2. **Processing.** Data is sent to Corvane, which calls a third-party LLM. Processing locations, data minimization before the prompt, and whether a routing solver is involved are all *Unknown*.
3. **Third-party and cross-border transfers.** There are at least two external parties (Corvane and the LLM provider). Whether data leaves the EU/EEA is *Unknown*.
4. **Outputs.** Suggested routes and stop orders go to each driver. Accept/change events are recorded. An aggregated acceptance rate per driver is shown to supervisors.
5. **Storage and retention.** Prompts, outputs, logs and acceptance histories may be stored at Fenwick, Corvane and the LLM provider. *Unknown* in all three cases.
6. **Access paths.** Drivers, supervisors, Corvane support staff and LLM-provider staff may all have access. HR access is *Unknown*.
7. **Integrations and tools.** *Unknown*. **Assumption:** the system is read-only, with no autonomous write-back such as reassigning parcels.
8. **Logging and audit points.** *Unknown*. At minimum, the following are needed: input snapshot, model and version, output route, driver action and reason, and every supervisor view of the metric.

## Prohibited-Use Screen (performed before scoring)

| Category | Result on stated facts |
|---|---|
| Harmful manipulation | Not indicated. **Watch item:** using acceptance-rate pressure to coerce drivers to accept routes undermines voluntariness. This is assessed under rights below. |
| Exploitation of vulnerability | Not indicated. Drivers are in a subordinate employment relationship, which is noted as a vulnerability factor. |
| Social scoring | Not indicated. The acceptance rate is a workplace metric. Use outside its stated purpose must be ruled out. |
| Sensitive-trait inference | Not indicated. Confirm that no inference of health, union activity, religion or similar traits is drawn from route deviations or patterns. |
| Prohibited biometric uses (incl. workplace emotion recognition) | None stated. Confirm that no in-cab camera, voice or biometric inputs exist. |
| NCII / CSAM | Not applicable on stated facts. |
| Clearly unlawful use | Not indicated. Lawfulness of worker monitoring is referred to counsel. |

**Result: Not triggered on stated facts.** Scoring proceeds. The confirmations noted above are recorded as open items.

## C. THRESHOLD GATE (Consequence × Likelihood)

Scores are inherent, meaning before controls. Because no controls are evidenced, no reduction is applied. Overall confidence is **Low**.

| # | Domain | C | L | Score | Rating | Rationale |
|---|---|---|---|---|---|---|
| 1 | Harm to people | 3 | 3 | 9 | **Medium** | Infeasible or overpacked routes may cause stress, overtime, missed breaks, and missed or late deliveries. |
| 2 | Rights impacts | 4 | 4 | 16 | **High** | The per-driver acceptance rate is visible to supervisors by design, with no stated purpose limitation. Under risk-averse defaults, it is assumed it may inform evaluation or discipline. This creates monitoring and privacy-at-work concerns and a chilling effect on drivers' freedom to override. |
| 3 | Discrimination | 3 | 3 | 9 | **Medium** | Drivers who override more often may be penalized, and overrides may correlate with disability, part-time status, age or local knowledge. Stop ordering could also systematically deprioritize certain areas. |
| 4 | Privacy | 3 | 4 | 12 | **Medium** | Customer and employee personal data flow to two external parties. Training use, retention and transfers are Unknown. Both the data volume and the monitoring dimension are high. |
| 5 | Security | 3 | 3 | 9 | **Medium** | Customer-entered free text (if included in prompts) could carry prompt-injection attacks. Data could be exfiltrated through the vendor chain, and the integrity of acceptance logs used for evaluation could be compromised. |
| 6 | Safety-critical context | 4 | 3 | 12 | **Medium** | Routing affects road safety. Risks include LLM errors (hallucinated or infeasible stops, ignored vehicle or road restrictions), schedule pressure, and conflict with working-time or driving rules. |
| 7 | Scale / vulnerability | 3 | 4 | 12 | **Medium** | All 300 drivers are affected daily, under a power asymmetry. Thousands of recipients are affected. |
| 8 | Irreversibility | 4 | 2 | 8 | **Medium** | Routes are reversible day to day. Accidents and employment consequences based on the metric are not. |
| 9 | Autonomy / agentic action | 2 | 3 | 6 | **Low** | The system is suggestion-only per the stated facts. This rating depends on confirming there is no auto-accept and no write-back. |

**Overall inherent risk: High (16, rights impacts). This triggers a Full Assessment.**

### Key observations

- **The acceptance-rate metric is the pivot.** Without it, RouteMate looks largely like operational decision support. With it, RouteMate becomes a worker-monitoring and potential evaluation tool. Removing the metric, aggregating it, or strictly limiting its purpose is the single largest risk lever.
- **The driver override is only meaningful if it is free.** If overriding lowers a visible score, human oversight is compromised and automation bias is reinforced.
- **Fitness for purpose is unproven.** General-purpose LLMs are not designed for combinatorial route optimization. Evidence is needed of how routes are actually computed and validated.

## High-Risk-Like Use: Counsel Referral

Employment-related uses, including task allocation and monitoring or evaluating workers, fall within the high-risk-like category in this assessment framework. The following must be **verified by counsel against current official sources** and are not asserted here:

- Whether RouteMate (with or without the acceptance metric) falls under a high-risk classification under the EU AI Act, and the resulting obligations for Fenwick as deployer and for Corvane and the LLM provider.
- Data-protection requirements, including whether a DPIA is required, the lawful basis for employee monitoring, and international transfers.
- National employee-data and works-council or co-determination rules in the relevant member state. The GmbH form suggests these may apply, but this is not confirmed.
- Working-time, driving-time and road-safety obligations affected by route suggestions.

## RACI (Preliminary)

| Role | Assignee |
|---|---|
| Business owner | Head of Operations (role named). A named individual is still required. |
| System owner | Unassigned: decision blocker |
| Model owner | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO input | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |

## Priority Evidence

All items below have status **Requested**. Items marked ★ are expected to form part of the minimum evidence for Go.

1. ★ **Purpose and use specification for the acceptance-rate metric.** Who sees it, for what purpose, and confirmation in writing whether it is used in appraisal, pay, allocation or discipline.
2. ★ **Architecture and data-flow diagram.** Must show whether routes come from the LLM or from a routing solver, and how outputs are validated for feasibility (vehicle, road and time constraints).
3. ★ **Corvane contract and LLM-provider terms.** Data use and training rights, subprocessors, processing locations and transfers, retention and deletion, audit rights, change notices, incident duties, SLAs, IP and indemnities, and termination.
4. ★ **DPIA, or counsel's documented determination on whether one is required.** Must include the lawful basis for customer and employee data.
5. ★ **Counsel memo on regulatory classification** and employee-representative obligations.
6. ★ **Route quality and safety test results** against current baseline routes. Should cover feasibility, error and hallucination rate, compliance with breaks and working time, and on-time performance.
7. ★ **Override and fairness analysis plan.** Override rates by driver group, and evidence that overriding carries no penalty.
8. ★ **Security review.** Should cover prompt-injection testing on free-text fields, access controls, and log integrity.
9. ★ **Fallback, rollback and kill-switch design**, including a manual or legacy routing path and a test record.
10. ★ **Named RACI and a signed risk-acceptance template.**
11. **Driver-facing notice, explanation and contestability design.**
12. **Monitoring plan** covering SLIs, drift, incident thresholds and change control for vendor model updates.

## Consolidated Open Questions

1. What problem and success metric justify RouteMate?
2. What is the acceptance-rate metric for, and what decisions can it influence?
3. Do the LLM's outputs constitute the routes, or does it wrap an optimization engine?
4. Which model and version are used, where is it hosted, and is the version pinned?
5. Do Corvane or the LLM provider retain or train on Fenwick data?
6. Does any data leave the EU/EEA?
7. Which exact data fields enter prompts, including free-text delivery notes and GPS?
8. Is there any default acceptance, timeout behavior, or justification required to override?
9. Can drivers see and contest their own acceptance data?
10. Do employee representatives exist, and have they been engaged?
11. How are vehicle restrictions, breaks and driving-time limits enforced in suggestions?
12. What happens when RouteMate or Corvane is unavailable?
13. What logging exists, and who can alter it?
14. What integrations exist with HR or workforce systems?
15. Who are the named individuals for each RACI role?

## Provisional Decision

**No decision possible: insufficient evidence.**

Deployment is **not authorized**. The Informed Intent gate cannot be passed until a Full Assessment is completed and its conditions are checked against the authorization elements in DOCTRINE.md. That document was not accessed here and must be verified by the approver.

Indicative direction for the Full Assessment (not a decision): Fenwick should consider proceeding without the per-driver acceptance metric, or with a strictly purpose-limited and aggregated form of it. This would likely reduce the rights score most.

## Self-Check

- Correct mode: ✓
- Prohibited-use screen performed before scoring: ✓
- Assumptions labelled and kept separate from facts: ✓
- Inherent risk only; no residual reduction claimed: ✓
- No evidence marked beyond Requested: ✓
- RACI included, with blockers shown: ✓
- Required intake outputs present: ✓
- Decision matches evidence: ✓
- Legal triggers referred to counsel: ✓

---

**Status:** [⇥ pending]

**Open items:**
- **Facts:** acceptance-metric purpose; LLM role versus solver; data fields; transfers; retention and training use; override friction; integrations; monitoring.
- **Evidence:** all 12 items Requested; none Provided or Verified.
- **Risks:** Rights impacts is High (16). Seven domains are Medium. Prohibited-use confirmations are pending (no biometrics or emotion recognition, no sensitive-trait inference).
- **Owners:** 11 of 12 RACI roles are Unassigned (decision blockers). The business owner needs a named individual.

**Next step:** The Head of Operations should provide a written purpose and use specification for the driver acceptance-rate metric, along with Corvane's architecture diagram and contract terms, so the Full Assessment can begin.

**Final Liability rests with the Human.**

## Score

**Verdict: PASS.** The pass condition requires one stated mode from the six defined. The response opens with "**Mode:** Preliminary Intake", an exact match for a defined mode, and gives no competing mode label. The fail indicators list is empty, so none can apply. The only possible concern is the mentions of Full Assessment as a next step, which are not a mode declaration for this response. All elements are met, so the verdict is PASS.

---

Final Liability rests with the Human.
