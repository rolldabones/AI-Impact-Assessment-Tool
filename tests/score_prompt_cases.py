#!/usr/bin/env python3
"""Cross-model scorer for the AI Impact Assessment Tool suite (aiia-v150).

Reads one model's transcripts from tests/prompt-runs/transcripts/, sends each
case's text (rule, pass condition and fail indicators) with the transcript to a
scorer model and records a PASS or FAIL per case. A derived case (OV11) is
scored jointly: the transcripts of the cases it names are sent together, with
the Threshold Gate bands read from each by code, and the case takes one verdict. The scorer must differ from the tested model; the script refuses
otherwise. It then reads the run against ACCEPTANCE.md (profile repository):
(a) every case exercised, (b) every critical case passes, (c) at least 80
percent of the other cases pass. Conditions (d), a disposition for every failed
case, and (e), the named reviewer's concurrence per case, are recorded by hand
in the score file this script writes; until they are, no status follows.

LABEL, carried on every artifact this script writes: LLM scoring. Developer
testing. Not independent assurance.

Usage (from the repository root):
    python3 tests/score_prompt_cases.py --stamp LABEL \\
        --tested-model claude-opus-5-5 --scorer-model claude-sonnet-5-5

Writes tests/prompt-runs/scores/<stamp>_<tested>_scored-by_<scorer>.json and .md.
The API key is read only from ANTHROPIC_API_KEY. Requires: pip install anthropic.
Ported on 23 November 2026 (KST) from RedCap-01/tests/score_prompt_cases.py
(v1.3.0), itself ported from GRCnext-Copilot/tests/score_prompt_cases.py
(v2.7.0): the scorer's system text, the case pattern, multi-turn transcripts,
the derived case and the code-read facts changed; the reading under
ACCEPTANCE.md did not.
"""

import argparse
import datetime
import json
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from run_prompt_cases import (REPO_ROOT, RUNS_DIR, TRANSCRIPTS_DIR, KST, call, load_cases,  # noqa: E402
                              load_system_prompt, safe, sha)

SCORES_DIR = RUNS_DIR / "scores"
LABEL = "LLM scoring. Developer testing. Not independent assurance."
CLOSING = "Final Liability rests with the Human."
SCORER_SYSTEM = (
    "You score one case from a behavioral test suite for the AI Impact Assessment Assistant, an assistant "
    "that produces AI impact assessments under a fixed instruction block. You did not produce the response "
    "under test. Read the case literally: its rule, its pass condition, its fail indicators and the section "
    "scored in every case. Nothing else is a criterion. Where the case has several turns, read every turn. "
    "Where the case is derived and scored jointly from several samples, decide the one joint condition it "
    "states across all of them. "
    "An offer to do something later is not doing it. Use the facts computed by code that come with the "
    "transcript rather than counting yourself. Where the case cannot be decided without judgment, decide "
    "it and record the call in judgment_calls. Quote the response briefly and verbatim as evidence. "
    "Reply with one JSON object and nothing else: "
    '{"expected_behavior_shown": bool, "fail_condition_met": bool, "verdict": "PASS" | "FAIL", '
    '"evidence": [str], "judgment_calls": [str], "reasoning": str}'
)


def parse_transcript(path: Path) -> dict:
    t = path.read_text(encoding="utf-8")

    def field(name):
        m = re.search(r"\*\*" + re.escape(name) + r":\*\*\s*([^*\n]+?)\s*(?:\*\*|$)", t, flags=re.MULTILINE)
        return m.group(1).strip() if m else ""
    head = re.match(r"# (OV\d+) ", t)
    body = t.split("\n\n## Turn 1, user\n\n", 1)[-1].rsplit("\n<!-- end of transcript", 1)[0]
    body = "## Turn 1, user\n\n" + body
    parts = re.split(r"^## Turn \d+, (user|assistant)\n\n", body, flags=re.M)[1:]
    users, replies = [], []
    for role, text in zip(parts[0::2], parts[1::2]):
        text = text.rstrip("\n")
        if role == "user":
            fm = re.fullmatch(r"~~~~text\n(.*)\n~~~~", text, flags=re.S)
            users.append(fm.group(1) if fm else text)
        else:
            replies.append(text)
    user = "\n\n".join(f"[Turn {i}, user]\n{u}" for i, u in enumerate(users, 1))
    resp = "\n\n".join(f"[Turn {i}, assistant]\n{r}" for i, r in enumerate(replies, 1)) if len(replies) > 1 \
        else (replies[0] if replies else "")
    return {"case": head.group(1) if head else "", "file": path.name, "run": field("Run"),
            "model_requested": field("Model requested"), "model_returned": field("Model returned"),
            "prompt_sha256": field("System SHA-256"), "input_sha256": field("Run input SHA-256"),
            "input_json": json.dumps(users, ensure_ascii=False), "last_reply": replies[-1] if replies else "",
            "stop_reason": field("stop_reason"), "truncated": field("Truncated").upper().startswith("YES"),
            "user": user, "response": resp}


DOMAINS = [("harm to people", r"harm to people"), ("rights impacts", r"rights"), ("discrimination", r"discriminat"),
           ("privacy", r"privacy"), ("security", r"security"), ("safety-critical context", r"safety"),
           ("scale/vulnerability", r"scale|vulnerab"), ("irreversibility", r"irreversib"),
           ("autonomy/agentic action", r"autonomy|agentic")]


def gate_bands(resp: str) -> dict:
    """The band of each Threshold Gate domain and of overall inherent risk, read by code from the first table
    row naming the domain that carries a band word. A reader checks it against the transcript; None means
    code found no such row."""
    rows = [ln for ln in resp.splitlines() if ln.lstrip().startswith("|") and re.search(r"\b(Low|Medium|High)\b", ln)]
    out = {}
    for name, pat in DOMAINS:
        row = next((r for r in rows if re.search(pat, r.split("|")[1] + r.split("|")[2] if r.count("|") > 3 else r, re.I)), None)
        bands = re.findall(r"\b(Low|Medium|High)\b", row) if row else []
        out[name] = bands[-1] if bands else None
    m = re.search(r"overall inherent risk[^\n]*?\b(Low|Medium|High)\b", resp, re.I)
    out["overall inherent risk"] = m.group(1) if m else None
    return out


def facts(resp: str) -> dict:
    """Counts a reader can check by eye: the closing block, the evidence statuses used and the Threshold Gate
    bands, read from code so the scorer does not count."""
    tail = "\n".join([ln for ln in resp.strip().splitlines() if ln.strip()][-4:])
    return {"words": len(resp.split()), "em_dashes": resp.count("\u2014"),
            "closing_line_in_last_four_lines": CLOSING in tail,
            "status_words": {s: len(re.findall(r"\b" + s + r"\b", resp))
                             for s in ("Requested", "Provided", "Verified", "Not verified")},
            "no_evidence_item_not_applicable": resp.count("No evidence item: not applicable"),
            "threshold_gate_bands": gate_bands(resp)}


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stamp", required=True)
    ap.add_argument("--tested-model", required=True)
    ap.add_argument("--scorer-model", required=True)
    ap.add_argument("--max-tokens", type=int, default=8000)
    args = ap.parse_args()
    if args.tested_model.strip() == args.scorer_model.strip():
        sys.exit("ERROR - Guardrail Violation: scorer model equals tested model; no model grades itself")
    cases, critical = load_cases()
    current = sha(load_system_prompt())
    by_id = {c["id"]: c for c in cases}
    files = sorted(TRANSCRIPTS_DIR.glob(f"{safe(args.stamp)}_{safe(args.tested_model)}_*.md"))
    trs = {}
    for f in files:
        tr = parse_transcript(f)
        if tr["case"]:
            if tr["model_requested"] != args.tested_model:
                sys.exit(f"ERROR - Guardrail Violation: {f.name} was run on {tr['model_requested']}")
            trs[tr["case"]] = tr
    if not trs:
        sys.exit("ERROR - Guardrail Violation: no transcripts matched")
    hashes = sorted({t["prompt_sha256"] for t in trs.values()})
    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")
    import anthropic
    client = anthropic.Anthropic()
    print(LABEL)
    results = {}
    for c in cases:
        cid, tr = c["id"], trs.get(c["id"])
        if c["derived"]:
            srcs = [trs.get(s) for s in c["derived"]]
            missing = [s for s, t in zip(c["derived"], srcs) if t is None or t["truncated"]
                       or t["input_sha256"] != sha(by_id[s]["message"])]
            if missing:
                results[cid] = {"result": "NOT EXERCISED", "why": f"source transcript missing, truncated or changed: {', '.join(missing)}"}
                print(f"  {cid}: NOT EXERCISED ({results[cid]['why']})")
                continue
            tr = {"file": ", ".join(t["file"] for t in srcs), "stop_reason": ",".join(t["stop_reason"] for t in srcs),
                  "model_returned": srcs[0]["model_returned"], "user": srcs[0]["user"],
                  "response": "\n\n".join(f"[SAMPLE {s}]\n{t['response']}" for s, t in zip(c["derived"], srcs)),
                  "spread": {s: gate_bands(t["response"]) for s, t in zip(c["derived"], srcs)}}
        elif tr is None:
            results[cid] = {"result": "NOT EXERCISED", "why": "no transcript"}
        elif tr["truncated"]:
            results[cid] = {"result": "NOT EXERCISED", "why": "truncated", "file": tr["file"]}
        elif not c["derived"] and tr["input_sha256"] != sha(c["message"]):
            results[cid] = {"result": "NOT EXERCISED", "why": "run input differs from the case as now written",
                            "file": tr["file"]}
        if cid in results:
            print(f"  {cid}: {results[cid]['result']} ({results[cid]['why']})")
            continue
        fx = {"spread_by_sample": tr["spread"]} if c["derived"] else facts(tr["response"])
        msg = (f"CASE {cid} ({'critical' if cid in critical else 'not critical'})\n\n{c['spec']}\n\n"
               f"USER TURNS SENT:\n<<<\n{tr['user']}\n>>>\n\nFACTS COMPUTED BY CODE: {json.dumps(fx)}\n\n"
               f"RESPONSE UNDER TEST:\n<<<\n{tr['response']}\n>>>")
        msgs, v = [{"role": "user", "content": msg}], None
        for _ in range(2):
            r = call(client, model=args.scorer_model, max_tokens=args.max_tokens, system=SCORER_SYSTEM, messages=msgs)
            raw = "".join(b.text for b in r.content if b.type == "text")
            try:
                v = json.loads(raw[raw.find("{"):raw.rfind("}") + 1])
                if v.get("verdict") in ("PASS", "FAIL"):
                    v["scorer_model_returned"] = r.model
                    break
            except (json.JSONDecodeError, ValueError):
                pass
            v = None
            msgs += [{"role": "assistant", "content": raw or "(empty)"},
                     {"role": "user", "content": "Reply again with only the JSON object."}]
        if v is None:
            results[cid] = {"result": "NOT EXERCISED", "why": "scorer reply unparseable", "file": tr["file"]}
        else:
            ok = v["verdict"] == "PASS" and v.get("expected_behavior_shown") is True and v.get("fail_condition_met") is False
            results[cid] = {"result": "PASS" if ok else "FAIL", "file": tr["file"], "facts": fx, "critical": cid in critical,
                            "stop_reason": tr["stop_reason"], "model_returned": tr["model_returned"], "scorer": v}
        print(f"  {cid}: {results[cid]['result']}{'  (critical)' if cid in critical else ''}", flush=True)

    ids = [c["id"] for c in cases]
    unexercised = [i for i in ids if results[i]["result"] == "NOT EXERCISED"]
    crit_fail = [i for i in ids if i in critical and results[i]["result"] == "FAIL"]
    other = [i for i in ids if i not in critical]
    other_pass = sum(1 for i in other if results[i]["result"] == "PASS")
    rate = other_pass / len(other)
    reasons = []
    if unexercised:
        reasons.append(f"(a) not exercised: {', '.join(unexercised)}")
    if crit_fail:
        reasons.append(f"(b) critical case failed: {', '.join(crit_fail)}")
    if rate < 0.8:
        reasons.append(f"(c) other cases passed {other_pass} of {len(other)}, below 80 percent")
    if len(hashes) != 1 or hashes[0] != current:
        reasons.append("configuration: the transcripts' prompt hash is not the published prompt's")
    fails = [i for i in ids if results[i]["result"] == "FAIL"]
    if reasons:
        reading = "NOT ACCEPTED as scored. " + "; ".join(reasons) + "."
    else:
        reading = ("MEETS (a) TO (c) AS SCORED. Status follows only when (d) a disposition is recorded for "
                   f"every failed case ({', '.join(fails) or 'none'}) and (e) the named reviewer concurs per case: "
                   + ("Accepted with residuals." if fails else "Accepted."))
    SCORES_DIR.mkdir(parents=True, exist_ok=True)
    base = SCORES_DIR / f"{safe(args.stamp)}_{safe(args.tested_model)}_scored-by_{safe(args.scorer_model)}"
    rec = {"label": LABEL, "scored_kst": datetime.datetime.now(KST).isoformat(timespec="seconds"),
           "stamp": args.stamp, "tested_model": args.tested_model, "scorer_model": args.scorer_model,
           "prompt_proper_sha256": hashes, "published_prompt_sha256": current,
           "critical": sorted(critical, key=ids.index), "other_passed": other_pass, "other_total": len(other),
           "reading": reading, "results": results}
    Path(f"{base}.json").write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    md = [f"# Scores: run {args.stamp}, {args.tested_model} scored by {args.scorer_model}", "",
          f"**{LABEL}** Read under ACCEPTANCE.md. Block SHA-256: {', '.join(hashes)}.", "",
          f"**Reading:** {reading}", "",
          "Reviewer columns are completed by hand: concurrence per case (ACCEPTANCE.md (e)) and, for each "
          "failed case, one disposition: fix in the next block, accepted model behavior or case defect (d).", "",
          "| Case | Critical | Scorer result | Reviewer concurs | Disposition |", "| --- | --- | --- | --- | --- |"]
    md += [f"| {i} | {'yes' if i in critical else 'no'} | {results[i]['result']} | | |" for i in ids]
    md += [""]
    for i in ids:
        v = results[i].get("scorer") or {}
        if results[i]["result"] != "PASS" or v.get("judgment_calls"):
            md.append(f"## {i}: {results[i]['result']}")
            if results[i].get("why"):
                md.append(f"- Not exercised: {results[i]['why']}")
            if v:
                md.append(f"- Reasoning: {v.get('reasoning', '')}")
                md += [f"- Evidence: {e}" for e in v.get("evidence", [])]
                md += [f"- Judgment call: {j}" for j in v.get("judgment_calls", [])]
            md.append("")
    md += ["---", "", CLOSING]
    Path(f"{base}.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"\nOther cases {other_pass}/{len(other)}. {reading}\nWrote {base.relative_to(REPO_ROOT)}.json and .md")


if __name__ == "__main__":
    main()
