# BUILD-GUIDE.md

**How the AI Impact Assessment Assistant was built · v1.2.3 · 13 August 2026**

This is the build log, kept because the method is the product as much as the Assistant is. It shows how to bootstrap a professional-grade governance tool from public source material using an AI platform's builder, and how to iterate it. The steps below were run in OpenAI's GPT builder with GPT-5.2 Thinking; substitute your platform's equivalents freely. The current instruction block lives in [INSTRUCTIONS.md](INSTRUCTIONS.md); do not copy prompts from this file.

This is long, so I'll be curt.

## Phase 1: Source and scaffold

1. Start with a good overview, such as the Australian government's [Artificial intelligence impact assessment tool](https://www.digital.gov.au/ai/impact-assessment-tool).
2. Upload it into your AI chat interface and ask: "Please review the attached, and then create a best practice generic AI impact assessment that I can then use to create a custom GPT that will help enterprises by acting as an Assistant for impact assessment."
3. In a second tool (or a fresh chat), ask for "a list of 100 questions that would be asked in an AI impact assessment. No citations, just the questions." Bring those questions back to the original chat and ask: "Does the information you have (for creating the comprehensive prompt that will enable me to create the custom GPT) cover the following questions: [paste the questions]". This sets context for the next steps.

## Phase 2: Research and draft

4. Turn on Deep Research (or your platform's equivalent) and instruct: "Consider the entirety of this conversation, and conduct further research to fill in any gaps that will need to be addressed for a jurisdiction-agnostic enterprise AI impact assessment GPT. Once you have completed this research to your satisfaction, create the comprehensive prompt that will enable me to create the custom GPT AI Impact Assessment Assistant. The satisfaction condition should be whether the custom GPT will yield professional-grade results. This is a high bar: best practices captured in a GPT that enables enterprise Users to do this work guided by the GPT, whether they have been trained in AI impact assessment or not."
5. You will likely be asked clarifying questions. My response: "EU AI Act, NIST AI RMF, ISO 42001 and other relevant guidelines, optimized for use within enterprises, sector-agnostic and all of the outputs you have listed, plus, further, the comprehensive prompt that will enable the User to create their own enterprise-specific custom GPT, for follow-up, continuous improvement, monitoring and review."
6. Review the output, then remind the AI that the Instructions box has a character limit: "There is limited space for Instructions in the Configuration process for creating custom GPTs. Give me a tight but comprehensive prompt that I can enter into Instructions." (The OpenAI limit is 8,000 characters. Verify your draft's length before pasting.)

## Phase 3: Configure and test

7. Take the resulting prompt and paste it into Instructions on the Configure page. If it does not fit, compress: ask the model to preserve every rule while cutting prose, then verify behavior with the operator verification checklist. The deployed, compressed block is in [INSTRUCTIONS.md](INSTRUCTIONS.md); the uncompressed long form is in [INSTRUCTIONS-EXTENDED.md](INSTRUCTIONS-EXTENDED.md).
8. Name it (for example "AI Impact Assessment Assistant") and describe it (for example: "Produces professional, audit-ready AI impact assessments that are jurisdiction-agnostic and aligned to the EU AI Act, NIST AI RMF, ISO/IEC 42001 and ISO/IEC 42005."). Add a profile picture if you like. Turn ON Code Interpreter. Choose a reasoning-capable model. I chose GPT-5.2 Thinking. Press Create.
9. Test it: "Run five self-tests with mock data to confirm that you are operating properly."
10. Ask it to introduce itself: "Provide a concise explanation of your capabilities" or "How can we begin our work together?"

## Phase 4: Iterate

11. Periodically go back into the Builder and, using the Create chat interface rather than the Configure page, ask: "How could this GPT be improved?" Decide whether to adopt its recommendations. Mine proposed, and I adopted: an up-front prohibited-use screen; a deterministic scoring rubric for the Threshold Gate; an Assumptions and Confidence section; evidence quality tags with a minimum-evidence-for-Go checklist; a system boundary and data flow narrative; a mini threat model for security; a vendor contract-controls checklist; SLI/SLO-driven monitoring; a Decision Record with RACI and explicit kill-switch authority; and an optional crosswalk appendix. All of these are now baked into the v1.1.0 instruction block rather than left as chat-level behavior.
12. I then instructed: "Ask the User for preferred strictness and be able to provide responses appropriate to both the risk-averse enterprise and the move-fast-with-guardrails enterprise." It thought for a long time, probably because extended thinking was enabled. Fun to watch. It even kept going after an interim "Thank you." It finally completed the build-out.
13. Update the custom GPT and re-test: "Please run ten extended self-tests using mock data, to confirm you are operating properly." Then run the [Builder Conformance Checklist](INSTRUCTIONS.md#builder-conformance-checklist), which replaces ad hoc self-tests with pass/fail criteria.
14. Here is my custom GPT: [AI Impact Assessment Assistant](https://chatgpt.com/g/g-69882df5cb388191952447d6324de455-ai-impact-assessment-assistant).

## Phase 5: When the tool improves itself

15. During v1.1.0 acceptance testing, the Assistant responded to a conformance test by drafting a full revision of its own instruction set: operating modes, a residual-risk rule, a five-outcome decision taxonomy, a self-conformance check. The draft was good and it was flawed in the same breath: nearly twice the character limit, doctrine names diluted, one mode declared but never specified, and two v1.1.0 features silently dropped. It was evaluated against these instructions, eight defects were corrected and the result shipped as v1.2.0 ([INSTRUCTIONS-EXTENDED.md](INSTRUCTIONS-EXTENDED.md) and [INSTRUCTIONS.md](INSTRUCTIONS.md)). The episode is the method in miniature: let the tool propose, never let it approve. The proposal was machine-made; the acceptance decision was not.

## The lesson

The key is to focus these tools. Don't put too much on one of them. Build multiple narrow tools instead. And keep the instruction block under version control with an acceptance checklist, because a governance tool that cannot itself show its evidence has no business asking others for theirs.

---

**Status: [✓ final] v1.2.3**

Final Liability rests with the Human.
