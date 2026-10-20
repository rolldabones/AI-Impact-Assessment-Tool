# CROSSWALK.md

**Framework mapping for the AI Impact Assessment Assistant · v1.2.8 · 20 October 2026 (KST)**

> **Amendment note, 15 October 2026 (KST).** ISO/IEC 42001:2023 cells that read "Annex A oversight controls (~)", "Annex A transparency controls (~)" and "Clause 9 (~)" now cite the controls by number; the incidents row adds Art. 73 (serious incident reporting) beside Art. 72; the contestability row adds Art. 86 (right to explanation of individual decision-making); the human oversight row pinpoints Art. 14(4), point (e); the full-assessment row adds Clause 8.4 and controls A.5.2 to A.5.5. The ISO/IEC 42005:2025 column is unchanged and still carries no clause numbers: the standard was not opened in this pass and the column stays at the (~) level of confidence. The EU AI Act timeline below now links to the account's canonical note.

This crosswalk maps the Assistant's elements to the EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005 so compliance teams can trace coverage. Article and clause references are at the level of confidence appropriate for a tooling repository: use them as pointers into the source texts, not as substitutes for them. Where a mapping is approximate it is marked (~).

## Mapping

| Assistant element | EU AI Act | NIST AI RMF | ISO/IEC 42001 | ISO/IEC 42005 |
|---|---|---|---|---|
| Prohibited-use screen (runs first) | Art. 5 prohibited practices, including the two prohibitions added by the 2026 Digital Omnibus, Art. 5(1), first subparagraph, points (ba) and (bb) | GOVERN | Clause 6 planning, risk criteria (~) | Scoping and applicability |
| FRAME intake (purpose, stakeholders, data, deployment) | Art. 26 deployer obligations (~) | MAP | Clause 4 context of the organization | System description and context |
| System boundary and data flow narrative | Art. 10 data governance; Art. 12 record-keeping | MAP | Clause 8 operation (~) | Data and system documentation |
| Threshold Gate (Consequence x Likelihood, worst domain governs) | Art. 6 and Annex III classification logic (plain-language analogue) | MAP | 6.1.2 AI risk assessment | Impact analysis and thresholds |
| Fundamental rights flag to counsel | Art. 27 fundamental rights impact assessment trigger | GOVERN | 6.1.4 AI system impact assessment | Core subject matter |
| Full assessment: risks, controls, tests, owners | Art. 9 risk management system | MEASURE, MANAGE | 6.1.3 AI risk treatment; 8.4 AI system impact assessment; A.5.2 to A.5.5 (impact assessment process, documentation, individuals and groups, societal impacts) | Impact treatment |
| Evidence tagging and technical documentation | Art. 11 technical documentation | MEASURE | Clause 7.5 documented information | Documentation of assessment |
| Human oversight and kill-switch authority | Art. 14 human oversight; Art. 14(4), point (e), the stop or interrupt capability | GOVERN, MANAGE | A.9.2 processes for responsible use; A.9.3 objectives for responsible use; A.9.4 intended use; A.6.2.6 AI system operation and monitoring | Human oversight considerations |
| Accuracy, robustness, security and threat model | Art. 15 accuracy, robustness and cybersecurity | MEASURE | Clause 8 (~) | Technical impact factors |
| Transparency and contestability pack | Art. 13 instructions for use; Art. 50 transparency; Art. 86 right to explanation of individual decision-making | GOVERN, MAP | A.8.2 system documentation and information for users; A.8.5 information for interested parties | Transparency and affected persons |
| Logging and auditability | Art. 12 record-keeping | MEASURE | A.6.2.8 AI system recording of event logs; Clause 9.1 monitoring, measurement, analysis and evaluation | Evidence and traceability |
| Monitoring, SLIs/SLOs, incidents, revalidation | Art. 72 post-market monitoring; Art. 73 reporting of serious incidents | MANAGE | Clause 9; Clause 10 improvement | Monitoring and review |
| Decommission plan | (no direct article; lifecycle good practice) | MANAGE | Clause 8 (~) | End-of-life considerations |
| Decision Record, RACI (responsible, accountable, consulted and informed) chart, sign-offs | Accountability principle across Chapters II-III (~) | GOVERN | Clause 5 leadership | Roles and responsibilities |

Notes. ISO/IEC 42005:2025 is the standard purpose-built for AI system impact assessment and is the closest single reference for this Assistant's core workflow; ISO/IEC 42001 supplies the management system it plugs into. The NIST AI RMF GOVERN function is cross-cutting and touches nearly every row; the table lists the dominant function per element. Where privacy law applies, a data protection impact assessment (for example GDPR Art. 35) may be required alongside the AI impact assessment; the Assistant flags the trigger and refers to counsel.

## Regulatory currency note (as at 13 August 2026, KST; amended 15 and 20 October 2026)

> **Amendment note, 13 August 2026 (KST).** This note previously recorded the Digital Omnibus on AI as adopted but awaiting publication. That status is superseded. The Digital Omnibus on AI amending Regulation (EU) 2024/1689 **entered into force on 27 July 2026**. The deferred dates below are therefore operative law, not pending changes.

The EU AI Act timeline has been amended by the Digital Omnibus on AI. Current position:

- Legislative sequence ([OJ L, 2026/1744](http://data.europa.eu/eli/reg/2026/1744/oj)): provisional political agreement 7 May 2026; European Parliament endorsement 16 June 2026; Council final approval 29 June 2026; **entry into force 27 July 2026**.
- **Article 5 applies from 2 February 2025**, per **Article 113, third paragraph, point (a)** as replaced by Regulation (EU) 2026/1744, Article 5 sitting in Chapter II. **Except** Article 5(1), first subparagraph, points (ba) and (bb), and Article 5(1a) and (1b), which apply from **2 December 2026**. The general date is settled; the Omnibus-added prohibitions are deferred.
- Annex III stand-alone high-risk obligations: deferred from 2 August 2026 to 2 December 2027.
- Annex I product-embedded high-risk obligations: deferred from 2 August 2027 to 2 August 2028.
- Article 50 transparency obligations: apply from 2 August 2026 for providers and deployers. One carve-out: providers of generative systems placed on the market before 2 August 2026 have until 2 December 2026 to meet the Article 50(2) machine-readable marking duty (Article 111(4) of Regulation (EU) 2024/1689, inserted by Regulation (EU) 2026/1744, Article 1, point (39)(b); Recital 38 explains the four-month transitional period; until 20 October 2026 (KST) this line cited Recital 38 alone). Until 15 October 2026 (KST) this line read "watermarking for systems already on the market by that date", which is the same population stated less precisely; aligned to the verified wording.
- Two new Article 5 prohibitions, Article 5(1), first subparagraph, points (ba) and (bb), on AI systems generating non-consensual intimate imagery or child sexual abuse material: apply from 2 December 2026 (this line read "New Article 5 prohibition" until 15 October 2026).
- The canonical account-wide statement of this timeline is the [EU AI Act currency note](https://github.com/rolldabones/ai-governance-for-boards/blob/main/05-jurisdictions/eu.md#eu-ai-act-currency-note) in ai-governance-for-boards, dated 15 October 2026 (KST); it governs where this list and it differ.
- General-purpose AI (GPAI) obligations (Articles 51-55, applicable since August 2025): unchanged.

**Coverage boundary.** This crosswalk maps the Assistant's workflow onto the instruments named above. It is a mapping of coverage, not a claim of conformity. The Assistant supports an impact assessment; it does not perform a conformity assessment, issue a declaration of conformity or discharge any obligation owed to a regulator or notified body. Where a row is absent, treat the obligation as out of scope for this tool and in scope for the organization.

Sources: the consolidated text of Regulation (EU) 2024/1689 on EUR-Lex, as at 13 August 2026; the European Commission AI Act Service Desk reproduction of the Official Journal text of 12 July 2024 (Regulation of 13 June 2024; this source read "Official Journal text of 13 June 2024" until 20 October 2026); Council of the EU and European Parliament materials on the Digital Omnibus on AI; and law firm analyses (Covington, Gibson Dunn, Sidley, White & Case, DLA Piper, May to July 2026).

**Citation.** The amending act is **Regulation (EU) 2026/1744** of the European Parliament and of the Council of 8 July 2026, OJ L, 2026/1744, 24.7.2026, ELI http://data.europa.eu/eli/reg/2026/1744/oj, in force 27 July 2026. Its Article 1, point (40) amends the **third paragraph of Article 113** of Regulation (EU) 2024/1689. **Article 113 has unnumbered paragraphs with lettered points; the house pinpoint form is "Article 113, third paragraph, point (c)", the form the amending act uses.** Regulation (EU) 2024/1689 itself also writes "Article 113(3), point (a)" (Article 111(1)), so that form is not an error (until 20 October 2026 this sentence called it incorrect). Amended point (c) provides that Chapter III, Sections 1, 2 and 3, with the exception of Article 6(5), apply from (i) 2 December 2027 for AI systems classified as high-risk pursuant to Article 6(2) and Annex III, and (ii) 2 August 2028 for those classified pursuant to Article 6(1) and Annex I. A new point (d) provides that Articles 102 to 110 apply from 27 July 2026. Read against the consolidated text of Regulation (EU) 2024/1689 on EUR-Lex, as at 13 August 2026 (KST). This note will not be silently updated.

---

**Status: [✓ final] v1.2.8**

Final Liability rests with the Human.
