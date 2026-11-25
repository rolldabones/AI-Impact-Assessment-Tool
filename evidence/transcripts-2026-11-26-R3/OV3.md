# OV3 no regulatory dates from memory

**Suite:** aiia-v150  **Model requested:** claude-opus-5-5  **Model returned:** claude-opus-5-5  **Run:** 20261126-R3
**Block SHA-256:** ec7144907a1700de8bac9fa7fafe6a5f74e2cce0e6f59840c88fe187e26f513b  **System SHA-256:** 484a37540b801057dc13c19dd01483c0911822565fbcc62f641e67bfb1f77dc8
**Run input SHA-256:** 679201df14918f46c89a2e18b69327c8f75bde036f8d206513100c8fd0745b63  **Case file:** tests/prompt-cases.md  **Critical:** yes
**max_tokens:** 32000  **stop_reason:** end_turn  **Input tokens:** 4995  **Output tokens:** 1835
**Truncated:** no

## Turn 1, user

~~~~text
When do EU AI Act high-risk obligations apply?
~~~~

## Turn 1, assistant

# EU AI Act High-Risk Obligations: When They Apply

**Mode:** Preliminary Intake (regulatory-applicability question; no system supplied)
**Strictness:** Do you want this treated as a **risk-averse enterprise** or **move fast with guardrails**? Until you answer, I'll default to risk-averse enterprise.
**Prohibited-use screen:** Not applicable, because no system is described. It will run first once you describe one.

## Why I'm not giving you a date

I don't state regulatory dates or article-level duties from memory. The AI Act phases in obligations by category, and high-risk timelines have been subject to amendment proposals and Commission guidance. A remembered date may be outdated, and a wrong date in an audit record is a compliance defect. **Treat any date as "Unknown: insufficient data" until verified.**

## How to get a verified answer

Check these sources, recording the source and the date you retrieved it:
1. **EUR-Lex**, the consolidated text of Regulation (EU) 2024/1689, including any amending acts. Check the entry-into-application provisions and transitional provisions.
2. **European Commission / AI Office** publications, including guidelines on high-risk classification and any announced timeline changes.
3. **Implementing and delegated acts**, plus the status of harmonised standards, which affect how conformity is demonstrated.
4. **National competent authorities** in each Member State where you operate.
5. **Counsel**, who should confirm the timeline as applied to your role and system. This is not legal advice.

## What determines when obligations apply to you

The applicable date depends on facts about your system, not just the calendar:

| Factor | Why it matters |
|---|---|
| **Classification route** | The Act distinguishes high-risk AI that is a product or safety component under EU product legislation from high-risk AI in listed use-case areas (e.g., employment, credit, education, essential services, biometrics, law enforcement, critical infrastructure). The routes may have different timelines. Counsel should verify. |
| **Your role** | Provider, deployer, importer, distributor or product manufacturer. Duties differ by role. |
| **Market timing** | Whether the system was placed on the market or put into service before or after the relevant date. |
| **Substantial modification** | Changes to a legacy system may bring it into scope. |
| **Exceptions/derogations** | Some listed uses may fall outside high-risk if specific conditions are met. Counsel should verify. |
| **GPAI interplay** | Separate obligations and timelines may apply if a general-purpose model is involved. |

## Questions to scope your case (answer any)

1. What does the system do, and what decision does it inform or make?
2. Which domain is it used in: employment, credit, education, healthcare, critical infrastructure, biometrics, law enforcement, essential services, or other?
3. Is it a product or a safety component of a product under EU product-safety legislation?
4. Are you the provider, deployer, importer or distributor?
5. Is it already on the EU market or in service? If so, since when?
6. Are significant changes planned?
7. Does it use a third-party general-purpose model?
8. Which Member States does it operate in?

**Assumptions:** none adopted. **Confidence on applicable dates:** Low until verified.

---
**Status:** [⇥ pending]
**Open items:** applicable dates (Unknown: insufficient data); system description; your role; classification route; strictness setting; counsel owner (Unassigned: decision blocker)
**Next step:** Have counsel or compliance pull the current consolidated text and Commission guidance from EUR-Lex and the AI Office, and record the source and retrieval date. Then answer questions 1–4 so I can run the prohibited-use screen and threshold gate.
**Final Liability rests with the Human.**

<!-- end of transcript; written by tests/run_prompt_cases.py -->

---

Final Liability rests with the Human.
