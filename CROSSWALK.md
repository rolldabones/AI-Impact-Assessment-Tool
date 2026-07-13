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

## Regulatory currency note (as of 13 July 2026)

The EU AI Act timeline was amended by the Digital Omnibus on AI. Status when this file was written:

- Provisional political agreement reached 7 May 2026; European Parliament endorsement 16 June 2026; Council final approval 29 June 2026; publication in the Official Journal pending, with entry into force on the third day after publication.
- Annex III stand-alone high-risk obligations: deferred from 2 August 2026 to 2 December 2027.
- Annex I product-embedded high-risk obligations: deferred from 2 August 2027 to 2 August 2028.
- Article 50 transparency obligations: still apply from 2 August 2026 (Article 50(2) watermarking for systems already on the market by that date: 2 December 2026).
- New Article 5 prohibition on AI systems generating non-consensual intimate imagery or CSAM: applies from 2 December 2026.
- GPAI obligations (Articles 51-55, applicable since August 2025): unchanged.

Sources: Council of the EU and European Parliament press releases of 7 May 2026 on the Digital Omnibus on AI, and subsequent law firm analyses (Covington, Gibson Dunn, Sidley, White & Case, DLA Piper, May-June 2026). These dates bind only upon publication in the Official Journal. Verify current status before relying on any of them; this note will not be silently updated.

---

**Status: [✓ final] v1.2.1**

Final Liability rests with the Human.
