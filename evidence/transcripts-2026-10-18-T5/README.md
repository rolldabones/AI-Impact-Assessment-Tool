# Evidence: T5 logged run, 18 October 2026 (KST)

**AI Impact Assessment Tool · logged run under the release rule (a changed block is accepted only after one logged run of the published instructions) · run label T5**

What this is: the transcripts and scores of the first logged run of the operator verification checklist against the published instruction block, the run that [`tests.md`](../../tests.md) records.

- **When:** 18 October 2026 (KST), in Michael Paik's Terminal. First run finished 10:19 KST at max_tokens 16,000; the re-run of OV6, which the first run truncated, finished 11:37 KST at max_tokens 64,000, streamed, with the same prompt and manifest.
- **Instruction text:** the fenced block of [`INSTRUCTIONS.md`](../../INSTRUCTIONS.md), block v1.4.0, and nothing outside it, 7,657 characters, SHA-256 `bb11b6544dc465d38ce09ad8883b587d3b96dfd8167f8a66019c2cae82d40700` (recorded in both summaries and in CHANGELOG 1.4.0). The repository HEAD at the run was `f7ab69a` (tag v1.3.0); block v1.4.0 was the uncommitted working-tree text released as v1.4.0.
- **Tested model:** `claude-opus-5-5`, API system prompt, no tools, no attached file (CROSSWALK.md not attached; the DOCTRINE.md section not pasted). **Scorer:** `claude-sonnet-5-5`, a different model. LLM scoring is developer testing, not independent assurance.
- **Inputs:** fictional organizations and systems; cases OV1 to OV10 are items 1 to 10 of the operator verification checklist.
- **How produced:** the session tool `t5_run.py` (not shipped in this repository; first run SHA-256 `6f74a965a0329341dd392dd32bfdb5340df4c3f46028af64c6505d07b00b0767`, re-run SHA-256 `2c0648ecf36761a3010ab5e41c629cbbc53b6ebbfb00d6e89f4665635ce43461`) ran each case in a fresh API session and wrote one transcript with its score per case and a summary. The scoring rubric (the scorer's prompt and its list of fail indicators, which the verdicts cite) is not shipped either, so the PASS and FAIL calls cannot be reproduced from this repository; each transcript shows the verdict and the scorer's stated reason.

Files:

- `OV1.md` to `OV10.md`: the result of record for each case, its completed run. OV6 is from the re-run (64,000); the rest are from the first run (16,000).
- `OV6-run1-truncated.md`: the first-run attempt truncated at 16,000, kept so both attempts are on the record. The scorer marked it FAIL on a substantive ground, not on the truncation: evidence statuses outside the four permitted values. OV6's result of record is the re-run.
- `summary.json` (first run) and `summary-rerun64k.json` (re-run).

Each transcript is copied byte for byte from the run output; only the closing line below is appended. The two summaries are copied unchanged. Model output is verbatim: its em dashes, serial commas and UK spellings are the model's and are not edited.

---

Final Liability rests with the Human.
