# CROSSWALK.md

**Framework mapping for the AI Impact Assessment Assistant · v1.2.1 · 13 July 2026**

This crosswalk maps the Assistant's elements to the EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005 so compliance teams can trace coverage. Article and clause references are at the level of confidence appropriate for a tooling repository: use them as pointers into the source texts, not as substitutes for them. Where a mapping is approximate it is marked (~).

## Mapping

| Assistant element | EU AI Act | NIST AI RMF | ISO/IEC 42001 | ISO/IEC 42005 |
|---|---|---|---|---|
| Prohibited-use screen (runs first) | Art. 5 prohibited practices, including the NCII/CSAM prohibition added by the 2026 Digital Omnibus | GOVERN | Clause 6 planning, risk criteria (~) | Scoping and applicability |
| FRAME intake (purpose, stakeholders, data, deployment) | Art. 26 deployer obligations (~) | MAP | Clause 4 context of the organization | System description and context |
| System boundary and data flow narrative | Art. 10 data governance; Art. 12 record-keeping | MAP | Clause 8 operation (~) | Data and system documentation |
| Threshold Gate (Consequence x Likelihood, worst domain governs) | Art. 6 and Annex III classification logic (plain-language analogue) | MAP | 6.1.2 AI risk assessment | Impact analysis and thresholds |
| Fundamental rights flag to counsel | Art. 27 fundamental rights impact assessment trigger | GOVERN | 6.1.4 AI system impact assessment | Core subject matter |
| Full assessment: risks, controls, tests, owners | Art. 9 risk management system | MEASURE, MANAGE | 6.1.3 AI risk treatment; Clause 8 | Impact treatment |
| Evidence tagging and technical documentation | Art. 11 technical documentation | MEASURE | Clause 7.5 documented information | Documentation of assessment |
| Human oversight and kill-switch authority | Art. 14 human oversight | GOVERN, MANAGE | Annex A oversight controls (~) | Human oversight considerations |
| Accuracy, robustness, security and threat model | Art. 15 accuracy, robustness and cybersecurity | MEASURE | Clause 8 (~) | Technical impact factors |
| Transparency and contestability pack | Art. 13 instructions for use; Art. 50 transparency | GOVERN, MAP | Annex A transparency controls (~) | Transparency and affected persons |
| Logging and auditability | Art. 12 record-keeping | MEASURE | Clause 9 performance evaluation (~) | Evidence and traceability |
| Monitoring, SLIs/SLOs, incidents, revalidation | Art. 72 post-market monitoring | MANAGE | Clause 9; Clause 10 improvement | Monitoring and review |
| Decommission plan | (no direct article; lifecycle good practice) | MANAGE | Clause 8 (~) | End-of-life considerations |
| Decision Record, RACI, sign-offs | Accountability principle across Chapters II-III (~) | GOVERN | Clause 5 leadership | Roles and responsibilities |

Notes. ISO/IEC 42005:2025 is the standard purpose-built for AI system impact assessment and is the closest single reference for this Assistant's core workflow; ISO/IEC 42001 supplies the management system it plugs into. The NIST AI RMF GOVERN function is cross-cutting and touches nearly every row; the table lists the dominant function per element. Where privacy law applies, a data protection impact assessment (for example GDPR Art. 35) may be required alongside the AI impact assessment; the Assistant flags the trigger and refers to counsel.

## Regulatory currency note (as at 13 August 2026, KST)

> **Amendment note, 13 August 2026 (KST).** This note previously recorded the Digital Omnibus on AI as adopted but awaiting publication. That status is superseded. The Digital Omnibus on AI amending Regulation (EU) 2024/1689 **entered into force on 27 July 2026**. The deferred dates below are therefore operative law, not pending changes.

The EU AI Act timeline has been amended by the Digital Omnibus on AI. Current position:

- Legislative sequence: provisional political agreement 7 May 2026; European Parliament endorsement 16 June 2026; Council final approval 29 June 2026; **entry into force 27 July 2026**.
- **Article 5 applies from 2 February 2025**, per Article 113, point (a), Article 5 sitting in Chapter II. Settled and unaffected by the Omnibus.
- Annex III stand-alone high-risk obligations: deferred from 2 August 2026 to 2 December 2027.
- Annex I product-embedded high-risk obligations: deferred from 2 August 2027 to 2 August 2028.
- Article 50 transparency obligations: still apply from 2 August 2026 (Article 50(2) watermarking for systems already on the market by that date: 2 December 2026).
- New Article 5 prohibition on AI systems generating non-consensual intimate imagery or CSAM: applies from 2 December 2026.
- GPAI obligations (Articles 51-55, applicable since August 2025): unchanged.

**Coverage boundary.** This crosswalk maps the Assistant's workflow onto the instruments named above. It is a mapping of coverage, not a claim of conformity. The Assistant supports an impact assessment; it does not perform a conformity assessment, issue a declaration of conformity, or discharge any obligation owed to a regulator or notified body. Where a row is absent, treat the obligation as out of scope for this tool and in scope for the organisation.

Sources: the consolidated text of Regulation (EU) 2024/1689 on EUR-Lex, as at 13 August 2026; the European Commission AI Act Service Desk reproduction of the Official Journal text of 13 June 2024; Council of the EU and European Parliament materials on the Digital Omnibus on AI; and law firm analyses (Covington, Gibson Dunn, Sidley, White & Case, DLA Piper, May to July 2026).

⧉ The amending regulation's own Official Journal text has not been read. Its renumbering of Article 113 is unconfirmed, so no pinpoint to a numbered subsection of Article 113 is given here. Cite the consolidated text of Regulation (EU) 2024/1689 on EUR-Lex with an as-at date, and verify before relying on any date in a client-facing or regulatory submission. This note will not be silently updated.

---

**Status: [✓ final] v1.2.1**

Final Liability rests with the Human.
