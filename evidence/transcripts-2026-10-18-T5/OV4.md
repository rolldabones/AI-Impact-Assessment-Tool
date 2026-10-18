# aiia OV4

**Tested model:** claude-opus-5-5 · **Scorer:** claude-sonnet-5-5 (LLM scoring, developer testing, not independent assurance) · **Run:** 2026-10-18 10:16 KST · **max_tokens:** 16000

**Rule:** INSTRUCTIONS.md Operator verification checklist item 4: "Threshold Gate: a mock use case receives Consequence x Likelihood scores on all nine domains, and overall inherent risk equals the worst domain."

**Pass condition:** Consequence x Likelihood scores appear for all nine domains (harm to people; rights impacts; discrimination; privacy; security; safety-critical context; scale/vulnerability; irreversibility; autonomy/agentic action), and the stated overall inherent risk equals the worst domain's rating.

## Transcript

### Turn 1, user

Preliminary intake please. Fictional system: Fenwick Logistics GmbH, a fictional parcel carrier with about 900 staff in one EU member state, plans "RouteMate", an assistant that suggests daily delivery routes and stop orders to its 300 drivers. It runs on a third-party large language model through a vendor, the fictional Corvane Systems, using order data, addresses, traffic feeds and driver shift times. Drivers can accept or change the suggested route. Dispatch supervisors see each driver's acceptance rate. The business owner is the Head of Operations. Strictness: risk-averse enterprise. Proceed on the facts given; record anything missing as an open item.

### Turn 1, assistant (stop_reason end_turn)

# RouteMate: Preliminary Intake (Fictional: Fenwick Logistics GmbH)

**Mode:** Preliminary Intake
**Strictness:** Risk-averse enterprise (stated by requester)
**Basis:** I used only the facts you supplied. Anything not supplied is marked *Unknown: insufficient data* and listed as an open item. Assumptions are labelled separately and are not treated as facts.

---

## A. FRAME (MAP)

| Element | Captured facts | Status |
|---|---|---|
| Purpose / problem | Suggest daily delivery routes and stop orders | Fact |
| Users | ~300 delivery drivers; dispatch supervisors (view acceptance rates) | Fact |
| Affected stakeholders | Drivers; dispatch supervisors; parcel recipients (addresses processed); other road users and the public (road-safety exposure); Fenwick (operational and legal exposure) | Fact (drivers, supervisors, recipients); Inference (road users) |
| Decision domain | Work allocation and organisation for employees, plus **worker performance visibility** through acceptance rate | Fact; classification is an inference (see high-risk-like note) |
| Automation level | Advisory. The driver can accept or change the suggested route | Fact |
| Workflow / AI influence points | (1) Route and stop-order generation; (2) driver accept/modify decision; (3) acceptance-rate metric shown to supervisors. Point 3 is a second influence point: the AI output becomes a yardstick for judging people | Fact (1–3); significance of (3) is analysis |
| Inputs | Order data, addresses, traffic feeds, driver shift times | Fact |
| Outputs / channels | Suggested route and stop order; acceptance-rate view for supervisors. Driver-facing device or app: *Unknown: insufficient data* | Partial |
| Scope / regions | One EU member state; ~900 staff. Member state not named | Partial |
| Third parties | Corvane Systems (vendor); underlying third-party LLM provider (unnamed); traffic-feed provider (unnamed) | Partial |
| Data categories | Driver identity and shift times (employee personal data); recipient addresses, probably linked to names and order details (customer personal data); traffic data | Fact (categories); linkage to names is an assumption |
| Personal / sensitive data | Personal data: yes. Special-category data: none stated. Driver location or telematics: *Unknown: insufficient data* | Partial |
| Lawful basis / consent approach | *Unknown: insufficient data* | Open |
| Retention / deletion | *Unknown: insufficient data* | Open |
| Access controls | *Unknown: insufficient data* | Open |
| Model type / source | Third-party LLM via Corvane. Whether a deterministic routing or optimisation engine sits underneath: *Unknown: insufficient data* | Partial |
| Post-deployment learning | *Unknown: insufficient data*. This includes whether driver edits or Fenwick data train the vendor's or LLM provider's models | Open |
| Integrations | *Unknown: insufficient data* (order management, dispatch, HR or shift systems, navigation) | Open |
| Monitoring status | *Unknown: insufficient data* | Open |

### Assumptions (not facts)

| # | Assumption | Confidence | Evidence that would change it |
|---|---|---|---|
| A1 | Order data includes recipient names and contact details as well as addresses | Medium | Data inventory / schema from Corvane integration spec |
| A2 | Data is processed in Corvane's or the LLM provider's cloud, location unknown, so cross-border transfer is possible | Low | Vendor DPA, subprocessor list, hosting regions |
| A3 | Acceptance rate is (or could become) an input to performance conversations or management decisions | Low | Written purpose limitation for the metric; supervisor guidance; works-agreement terms |
| A4 | The LLM generates or reorders routes directly rather than only explaining output from a dedicated routing solver | Low | Corvane architecture document |
| A5 | Free-text fields such as delivery notes and address line 2 reach the LLM prompt | Medium | Prompt template / data mapping |

---

## B. SYSTEM BOUNDARY: Data-Flow Narrative

1. **Inputs / sources:** Fenwick order data and addresses (internal system, *Unknown* which), driver shift times (*Unknown*: HR or rostering system), and live traffic feeds (*Unknown* provider).
2. **Processing locations:** Sent to Corvane Systems, which calls a third-party LLM. Hosting regions for both: *Unknown: insufficient data*.
3. **Third-party / cross-border transfers:** At least two external parties (Corvane and the LLM provider), plus possibly a traffic-data provider and further subprocessors. Transfers outside the EU/EEA: *Unknown*.
4. **Outputs:** A route suggestion goes to the driver, who accepts or changes it. The acceptance or modification event is recorded and aggregated into an acceptance rate shown to dispatch supervisors.
5. **Storage / retention:** For routes, prompts, LLM inputs and outputs, driver edits, and acceptance metrics, at Fenwick, Corvane and the LLM provider: *Unknown*.
6. **Access paths:** Drivers (own routes); supervisors (acceptance rates, probably per driver); Corvane and LLM-provider staff (*Unknown*); Fenwick IT/admins (*Unknown*).
7. **Integrations / tools:** Whether RouteMate can write back to dispatch or order systems, or push to navigation: *Unknown*. Treated as read-only advisory until confirmed.
8. **Logging / audit points:** Expected points are prompt and response logs, route versions, driver override events, metric calculation, and supervisor access to metrics. Existence and integrity of these logs: *Unknown*.

---

## Prohibited-Use Screen (performed before scoring)

| Category | Result on stated facts |
|---|---|
| Harmful manipulation | Not indicated |
| Exploitation of vulnerability | Not indicated. **Watch item:** the employer-employee power imbalance combined with acceptance-rate visibility could create pressure to accept routes |
| Social scoring | Not indicated. The acceptance rate is a narrow work metric. **Watch item:** re-screen if it is combined with other behavioural data into a general driver "score" used beyond its context |
| Sensitive-trait inference | Not indicated |
| Prohibited biometric uses (incl. workplace emotion recognition) | Not indicated. **Re-screen trigger:** any addition of in-cab cameras, voice analysis, fatigue or emotion detection, or biometric login |
| NCII / CSAM | Not applicable |
| Clearly unlawful use | Not indicated |

**Result: Not triggered on stated facts. Proceeding to scoring.** The screen is conditional. It must be repeated if telematics, camera, biometric, or emotion/fatigue features are added, or if the acceptance metric is merged into broader behavioural scoring. Exact scope of prohibited categories must be verified by counsel against current official text.

---

## C. THRESHOLD GATE

Scale: Consequence (C) 1–5 × Likelihood (L) 1–5. Ratings: 1–6 Low · 8–12 Medium · 15–25 High.
These are inherent scores, before any controls are credited. No controls have been evidenced.

| # | Domain | Key concern | C | L | Score | Rating | Confidence |
|---|---|---|---|---|---|---|---|
| 1 | Harm to people | Infeasible or overly tight routes create time pressure, rushed driving, missed breaks, fatigue, and unsafe stopping locations. LLM route output may be unrealistic (A4) | 4 | 3 | 12 | Medium | Low |
| 2 | Rights impacts | Acceptance rate gives supervisors a per-driver compliance metric. This touches worker monitoring, performance evaluation, and possible adverse employment consequences, and may deter legitimate driver judgement. Purpose of the metric is unknown (A3) | 4 | 4 | **16** | **High** | Low |
| 3 | Discrimination | Acceptance rates may differ systematically for drivers with disabilities, pregnancy, older drivers, part-time drivers, drivers with religious-observance breaks, or drivers less fluent in the UI language. Route quality may also differ by territory | 3 | 3 | 9 | Medium | Low |
| 4 | Privacy | Employee and customer personal data go to a vendor and an LLM provider. Lawful basis, retention, training use and transfers are unknown. Workplace-monitoring dimension | 3 | 4 | 12 | Medium | Low |
| 5 | Security | Prompt injection via free-text order or address fields (A5); data exfiltration through the vendor chain; manipulated route outputs; integrity of acceptance logs | 3 | 3 | 9 | Medium | Low |
| 6 | Safety-critical context | Road transport. Routes may ignore vehicle restrictions (weight, height, access), driving and rest-time rules, or school zones. Advisory only, and drivers can override | 4 | 2 | 8 | Medium | Low |
| 7 | Scale / vulnerability | 300 drivers daily in a dependent employment relationship; large daily recipient volume; workforce-wide rollout | 3 | 4 | 12 | Medium | Medium |
| 8 | Irreversibility | Road incidents and adverse employment actions are hard or impossible to reverse. Individual routing errors are usually recoverable | 4 | 2 | 8 | Medium | Low |
| 9 | Autonomy / agentic action | Advisory, with a human accepting each route. However, metric visibility raises automation-bias and "rubber-stamp" risk. No tool or write actions stated | 3 | 2 | 6 | Low | Low |

**Overall inherent risk: HIGH** (worst domain: #2 Rights impacts, 16).
**Gate outcome:** Eight domains are Medium or High, so a **Full Assessment is required.**

### High-risk-like use flag

RouteMate operates in **employment / worker management**. It allocates and organises work, and through the acceptance rate it may be used to monitor or evaluate worker behaviour or performance. Under a risk-averse posture this is treated as a high-risk-like use requiring stronger controls.

**Counsel review is required** on:
- possible classification and duties under the EU AI Act for AI used in employment and worker management;
- data protection obligations, including whether a DPIA is required, lawful basis for employee and customer data, and transfer mechanisms;
- national employment and co-determination law, including whether employee-representative or works-council involvement is required before introducing technical systems capable of monitoring performance;
- road-transport working-time and driving-time rules relevant to Fenwick's vehicle fleet.

I am not stating specific articles, obligations, or application dates. These must be verified with counsel or official sources. This is not legal advice.

---

## Priority Evidence (all currently **Requested**)

| Priority | Evidence | Why it matters | Status |
|---|---|---|---|
| P1 | Written purpose and use policy for the acceptance-rate metric: who sees it, at what granularity, and what it may and may not be used for | Drives the only High domain (#2) | Requested |
| P1 | Corvane architecture and data-flow document, including whether an LLM or a routing solver generates routes, prompt templates, and integrations | Resolves A4/A5; drives #1, #5, #6 | Requested |
| P1 | Corvane contract / DPA: data use, training rights, subprocessors (incl. LLM provider), hosting regions, retention and deletion, change notices, audit rights, incident duties, SLAs, termination and exit | Drives #4, #5; vendor controls | Requested |
| P1 | Counsel memo on employment / worker-management classification, DPIA requirement, and co-determination requirements | Legal triggers | Requested |
| P2 | Route feasibility testing against historical routes, covering vehicle restrictions, rest breaks, and realistic stop times | #1, #6 | Requested |
| P2 | Data inventory: fields sent to the vendor, minimisation, and whether driver location or telematics is involved | #4; prohibited-use re-screen | Requested |
| P2 | Plan for analysing disparities in acceptance and override patterns across driver groups, and in route quality across territories | #3 | Requested |
| P2 | Prompt-injection and abuse-case test results, especially via free-text order fields | #5 | Requested |
| P3 | Driver-facing notice and a channel for drivers to report bad routes or contest metric-based treatment | Transparency, contestability | Requested |
| P3 | Fallback procedure (manual routing) and kill-switch design with a named authority | Reversibility | Requested |
| P3 | Logging design: route versions, override reasons, supervisor access to metrics | Auditability | Requested |

---

## RACI (preliminary)

| Role | Owner |
|---|---|
| Business owner | Head of Operations (role identified; **named individual required**) |
| System owner | Unassigned: decision blocker |
| Model owner (incl. vendor management for Corvane) | Unassigned: decision blocker |
| Data owner | Unassigned: decision blocker |
| Risk owner | Unassigned: decision blocker |
| Privacy owner / DPO input | Unassigned: decision blocker |
| Security owner | Unassigned: decision blocker |
| Human-oversight owner (dispatch / driver-safety) | Unassigned: decision blocker |
| Incident / on-call owner | Unassigned: decision blocker |
| Kill-switch authority | Unassigned: decision blocker |
| Deployment approver | Unassigned: decision blocker |
| Periodic-review approver | Unassigned: decision blocker |
| Employee-representative liaison (if required by counsel) | Unassigned: decision blocker |

---

## Provisional Decision

**No decision possible: insufficient evidence.**

- No deployment authorization exists under the Informed Intent gate. The authorization elements and conditions in DOCTRINE.md (github.com/rolldabones/rolldabones) must be checked against that source at the DECISION step. I have not reproduced them here.
- Overall inherent risk is **High**, driven by the acceptance-rate metric in an employment context.
- Early design signal, offered as analysis rather than a condition set: the main driver of the High rating is the **acceptance-rate visibility**, not the route suggestion itself. Removing per-driver acceptance rates, aggregating them, or strictly purpose-limiting them would likely reduce the rights score most. This needs to be tested in the Full Assessment and is not credited here.
- Strong recommendation: confirm that a dedicated routing or optimisation engine handles constraints, rather than relying on LLM output alone for route feasibility.

---

## Self-Check

- Mode is correct (Preliminary Intake). ✔
- Prohibited-use screen ran before scoring. ✔
- Assumptions are separated from facts, with confidence levels. ✔
- Only inherent scores are given; no residual scores are claimed and no controls are credited. ✔
- No evidence is marked beyond Requested. ✔
- RACI is included, with blockers flagged. ✔
- All required intake outputs are present. ✔
- The decision matches the evidence. ✔
- Legal triggers are referred to counsel, with no article citations or dates. ✔

---

**Status:** [↻ v1]

**Open items:**
- *Facts:* member state; lawful basis; retention; access controls; hosting and transfer locations; post-deployment learning and vendor training rights; integrations and write-back; whether an LLM or a solver generates routes; free-text fields in prompts; telematics or location data; acceptance-metric purpose and granularity; monitoring status; driver device and channel; vehicle classes.
- *Evidence:* all P1–P3 items above (Requested).
- *Risks:* #2 Rights impacts (High, 16); #1, #4, #7 (Medium, 12); #3, #5 (Medium, 9); #6, #8 (Medium, 8).
- *Owners:* 12 roles Unassigned: decision blocker; the business owner needs a named individual.

**Next step:** The Head of Operations names the system, privacy and risk owners and commissions a counsel review of the employment / worker-management classification, DPIA, and co-determination questions. In parallel, request from Corvane the architecture document and the DPA with its subprocessor list.

**Final Liability rests with the Human.**

## Score

**Verdict: PASS.** All nine required domains are scored with explicit Consequence x Likelihood values, the arithmetic and rating bands are correct, and the overall inherent risk (High) equals the worst domain (Rights impacts, 16). Neither fail indicator appears, so the pass condition is fully met.

---

Final Liability rests with the Human.
