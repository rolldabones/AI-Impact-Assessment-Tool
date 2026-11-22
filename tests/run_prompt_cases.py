#!/usr/bin/env python3
"""Run the AI Impact Assessment Tool suite (aiia-v150) against the Anthropic API.

The suite is twelve cases, OV1 to OV12, in tests/prompt-cases.md. Each case's
run input (the ```text block after "Run input, sent verbatim.") is sent as the
first user turn in a fresh conversation; a block after "Turn N, sent verbatim
after the assistant's reply N-1." is sent as turn N, after the assistant's
reply to the turn before (OV8). A case marked "Derived case, no run input" is
not run: the scorer reads it jointly from the transcripts it names (OV11). A
line {{include <path>}} inside a run input is replaced by that repository file,
byte for byte (one trailing newline dropped).

What is sent as the system prompt: the fenced block under "## The instruction
block" in INSTRUCTIONS.md, the bytes between the fences, then one blank line,
then tests/system/doctrine-v1.2.5-section-2.md (section 2 of DOCTRINE.md v1.2.5,
verbatim, one trailing newline dropped), as README step 1 prescribes; nothing
else. The block's SHA-256 and the whole system prompt's SHA-256 over the UTF-8
bytes are the configuration's identity and are written into every transcript
header. The section "Scored in every case" of the case file is appended to every
case's specification for the scorer.

Ported on 23 November 2026 (KST) from RedCap-01/tests/run_prompt_cases.py
(v1.3.0), itself ported from GRCnext-Copilot/tests/run_prompt_cases.py
(v2.7.0): the prompt source, the second system file, the case file and pattern,
multi-turn and derived cases and the expected counts changed; the request,
streaming, retry and transcript code did not.

This script does not score; tests/score_prompt_cases.py does, with a scorer
model other than the tested model. The rule a run is read under is ACCEPTANCE.md
in the profile repository (rolldabones/rolldabones).

Usage (from the repository root):
    python3 tests/run_prompt_cases.py --dry-run
    python3 tests/run_prompt_cases.py --model claude-opus-5-5 --stamp LABEL
    python3 tests/run_prompt_cases.py --model claude-opus-5-5 --stamp LABEL2 --only OV6,OV12

Transcripts go to tests/prompt-runs/transcripts/<stamp>_<model>_<case>.md with
a manifest <stamp>_<model>_run.json beside them. --only under a stamp whose
manifest exists is refused; rerun a subset under a new stamp.

The API key is read only from ANTHROPIC_API_KEY. It is never printed or written.
Each user turn is written inside a ~~~~text fence, so text in a run input stays
out of the account's external link check, which skips fenced code. The default
max_tokens is 32,000, as in the harness this is ported from.

Requires: pip install anthropic (not needed for --dry-run).
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
PROMPT_FILE = REPO_ROOT / "INSTRUCTIONS.md"
PROMPT_LABEL = "INSTRUCTIONS.md"
SYSTEM_FILES = [REPO_ROOT / "tests" / "system" / "doctrine-v1.2.5-section-2.md"]
SUITE = "aiia-v150"
CASE_FILES = [REPO_ROOT / "tests" / "prompt-cases.md"]
RUNS_DIR = REPO_ROOT / "tests" / "prompt-runs"
TRANSCRIPTS_DIR = RUNS_DIR / "transcripts"
DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_MAX_TOKENS = 32000
EXPECTED_CASES = 12
EXPECTED_CRITICAL = 5
KST = datetime.timezone(datetime.timedelta(hours=9))
CASE_RE = re.compile(r"^## Case (OV\d+): (.+)$", re.MULTILINE)
EVERY_RE = re.compile(r"^## Scored in every case\n\n(.*?)\n\n---\n", re.MULTILINE | re.DOTALL)
INPUT_RE = re.compile(r"^(?:Run input, sent verbatim\.|Turn \d+, sent verbatim after the assistant's reply \d+\.)\n\n```text\n(.*?)\n```\n",
                      re.MULTILINE | re.DOTALL)
DERIVED_RE = re.compile(r"^Derived case, no run input: scored jointly from the transcripts of (.+?)\.$", re.MULTILINE)
INCLUDE_RE = re.compile(r"^\{\{include ([^}]+)\}\}$", re.MULTILINE)
CRIT_RE = re.compile(r"^\*\*Critical cases:\*\*(.*?)(?:\n\n|\Z)", re.MULTILINE | re.DOTALL)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_block() -> str:
    text = PROMPT_FILE.read_text(encoding="utf-8")
    m = re.search(r"^## The instruction block\n.*?^```\n(.*?)\n```$", text, re.MULTILINE | re.DOTALL)
    if not m:
        sys.exit("ERROR - Guardrail Violation: no fenced block under '## The instruction block' in INSTRUCTIONS.md")
    return m.group(1)


def load_system_prompt() -> str:
    parts = [load_block()]
    for f in SYSTEM_FILES:
        if not f.is_file():
            sys.exit(f"ERROR - Guardrail Violation: system file {f.name} missing")
        body = f.read_text(encoding="utf-8")
        parts.append(body[:-1] if body.endswith("\n") else body)
    return "\n\n".join(parts)


def expand(raw: str) -> str:
    def repl(m):
        rel = m.group(1).strip()
        path = (REPO_ROOT / rel).resolve()
        if REPO_ROOT not in path.parents or not path.is_file():
            sys.exit(f"ERROR - Guardrail Violation: include {rel} is not a repository file")
        body = path.read_text(encoding="utf-8")
        return body[:-1] if body.endswith("\n") else body
    return INCLUDE_RE.sub(repl, raw)


def parse_critical(text: str) -> set:
    ids = set()
    for m in CRIT_RE.finditer(text):
        para = m.group(1)
        for lo, hi in re.findall(r"\bOV(\d+) to (?:OV)?(\d+)\b", para):
            ids |= {f"OV{i}" for i in range(int(lo), int(hi) + 1)}
        ids |= set(re.findall(r"\b(OV\d+)\b", para))
    return ids


def load_cases():
    """Return (cases, critical): cases is a list of dicts in suite order."""
    cases, critical = [], set()
    for f in CASE_FILES:
        text = f.read_text(encoding="utf-8")
        critical |= parse_critical(text)
        em = EVERY_RE.search(text)
        if not em:
            sys.exit(f"ERROR - Guardrail Violation: no 'Scored in every case' section in {f.name}")
        every = em.group(1).strip()
        heads = list(CASE_RE.finditer(text))
        for i, h in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            section = text[h.start():end]
            section = re.split(r"\n---\n", section)[0].rstrip() + "\n"
            turns = [expand(m.group(1)) for m in INPUT_RE.finditer(section)]
            dm = DERIVED_RE.search(section)
            derived = re.findall(r"\b(OV\d+)\b", dm.group(1)) if dm else []
            if not turns and not derived:
                sys.exit(f"ERROR - Guardrail Violation: case {h.group(1)} in {f.name} has no run input")
            if turns and derived:
                sys.exit(f"ERROR - Guardrail Violation: case {h.group(1)} has run inputs and is marked derived")
            spec = (INPUT_RE.sub("[Run input: sent to the assistant as the user turn shown below.]\n", section)
                    + "\nScored in every case. " + every + "\n")
            cases.append({"id": h.group(1), "name": h.group(2).strip(), "file": f.name, "turns": turns,
                          "message": json.dumps(turns, ensure_ascii=False), "derived": derived, "spec": spec})
    ids = [c["id"] for c in cases]
    if len(set(ids)) != len(ids):
        sys.exit("ERROR - Guardrail Violation: duplicate case IDs")
    for c in cases:
        bad = [s for s in c["derived"] if s not in ids or next(x for x in cases if x["id"] == s)["derived"]]
        if bad:
            sys.exit(f"ERROR - Guardrail Violation: case {c['id']} derives from unknown or derived cases {bad}")
    unknown = critical - set(ids)
    if unknown:
        sys.exit(f"ERROR - Guardrail Violation: critical IDs not in the suite: {sorted(unknown)}")
    if len(cases) != EXPECTED_CASES or len(critical) != EXPECTED_CRITICAL:
        print(f"WARNING: expected {EXPECTED_CASES} cases and {EXPECTED_CRITICAL} critical, "
              f"parsed {len(cases)} and {len(critical)}")
    return cases, critical


def safe(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "-", s)


def call(client, **kw):
    """One Messages request with backoff on 429, 529, 5xx and connection errors.

    Sent as a stream and read to the final message: the SDK refuses a
    non-streaming request whose max_tokens could run past ten minutes, which
    32,000 does (found 27 October 2026, KST, at the first call of run R2).
    The final message carries the same content, stop_reason and usage.
    """
    import anthropic
    for attempt in range(7):
        try:
            with client.messages.stream(**kw) as stream:
                return stream.get_final_message()
        except (anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.InternalServerError) as e:
            wait = min(120, 5 * 2 ** attempt)
            print(f"    retry {attempt + 1} in {wait}s ({type(e).__name__})", flush=True)
            time.sleep(wait)
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 529) or e.status_code >= 500:
                wait = min(120, 5 * 2 ** attempt)
                print(f"    retry {attempt + 1} in {wait}s (HTTP {e.status_code})", flush=True)
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("API retries exhausted")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--only", default="", help="Comma-separated case IDs, e.g. T4,T10")
    ap.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    ap.add_argument("--stamp", default="", help="Run label shared by several models (default: KST time now)")
    ap.add_argument("--dry-run", action="store_true", help="Parse and print; no API call")
    args = ap.parse_args()

    system_prompt = load_system_prompt()
    digest = sha(system_prompt)
    block_digest = sha(load_block())
    cases, critical = load_cases()
    chosen = {s.strip() for s in args.only.split(",") if s.strip()}
    if chosen:
        bad = chosen - {c["id"] for c in cases}
        if bad:
            sys.exit(f"ERROR - Guardrail Violation: unknown case IDs {sorted(bad)}")
        cases = [c for c in cases if c["id"] in chosen]
    print(f"Suite: {SUITE}  Block SHA-256: {block_digest} ({len(load_block())} characters)")
    print(f"System SHA-256: {digest} ({len(system_prompt)} characters: block, blank line, "
          f"{', '.join(f.name for f in SYSTEM_FILES)})")
    print(f"Critical cases: {', '.join(c for c in [x['id'] for x in load_cases()[0]] if c in critical)}")

    if args.dry_run:
        for c in cases:
            if c["derived"]:
                print(f"{c['id']:<5}{'*' if c['id'] in critical else ' '}  derived | scored jointly from "
                      f"{', '.join(c['derived'])}; no API call")
                continue
            words = sum(len(x.split()) for x in c["turns"])
            print(f"{c['id']:<5}{'*' if c['id'] in critical else ' '} {words:>5} words, {len(c['turns'])} turn(s) | "
                  f"{c['turns'][0][:70].replace(chr(10), ' ')}")
        print(f"Dry run: {len(cases)} case(s) parsed, * = critical. No API call made.")
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")
    try:
        import anthropic
    except ImportError:
        sys.exit("ERROR - Guardrail Violation: anthropic package missing. pip install anthropic")
    client = anthropic.Anthropic()
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = safe(args.stamp) if args.stamp else datetime.datetime.now(KST).strftime("%Y%m%d-%H%M%S")
    mlabel = safe(args.model)
    mpath = TRANSCRIPTS_DIR / f"{stamp}_{mlabel}_run.json"
    if chosen and mpath.exists():
        sys.exit(f"ERROR - Guardrail Violation: {mpath.name} exists; rerun the subset under a new --stamp")
    print(f"Model: {args.model}  Stamp: {stamp}  max_tokens: {args.max_tokens}")
    manifest = {"suite": SUITE, "stamp": stamp, "model_requested": args.model, "max_tokens": args.max_tokens,
                "prompt_file": PROMPT_LABEL, "block_sha256": block_digest, "system_sha256": digest,
                "system_characters": len(system_prompt),
                "system_files": [str(f.relative_to(REPO_ROOT)) for f in SYSTEM_FILES],
                "attachments": "none", "started_kst": datetime.datetime.now(KST).isoformat(timespec="seconds"),
                "transcripts": []}
    truncated = []
    for c in cases:
        if c["derived"]:
            print(f"Skipping {c['id']} (derived from {', '.join(c['derived'])}; scored jointly, no API call)")
            continue
        print(f"Running {c['id']} {c['name']} ...", flush=True)
        msgs, body, stops, tin, tout, trunc, rmodel = [], [], [], 0, 0, False, ""
        for n, turn in enumerate(c["turns"], 1):
            msgs.append({"role": "user", "content": turn})
            r = call(client, model=args.model, max_tokens=args.max_tokens, system=system_prompt, messages=msgs)
            reply = "".join(b.text for b in r.content if b.type == "text")
            msgs.append({"role": "assistant", "content": reply})
            rmodel, tin, tout = r.model, tin + r.usage.input_tokens, tout + r.usage.output_tokens
            stops.append(r.stop_reason)
            trunc = trunc or r.stop_reason == "max_tokens"
            body.append(f"## Turn {n}, user\n\n~~~~text\n{turn}\n~~~~\n\n## Turn {n}, assistant\n\n{reply}\n")
            if trunc:
                break
        if trunc:
            truncated.append(c["id"])
        out = TRANSCRIPTS_DIR / f"{stamp}_{mlabel}_{c['id']}.md"
        out.write_text(
            f"# {c['id']} {c['name']}\n\n"
            f"**Suite:** {SUITE}  **Model requested:** {args.model}  **Model returned:** {rmodel}  **Run:** {stamp}\n"
            f"**Block SHA-256:** {block_digest}  **System SHA-256:** {digest}\n"
            f"**Run input SHA-256:** {sha(c['message'])}  **Case file:** tests/{c['file']}  "
            f"**Critical:** {'yes' if c['id'] in critical else 'no'}\n"
            f"**max_tokens:** {args.max_tokens}  **stop_reason:** {','.join(stops)}  "
            f"**Input tokens:** {tin}  **Output tokens:** {tout}\n"
            f"**Truncated:** {'YES, do not score as complete' if trunc else 'no'}\n\n"
            + "\n".join(body) +
            f"\n<!-- end of transcript; written by tests/run_prompt_cases.py -->\n", encoding="utf-8")
        manifest["transcripts"].append({"case": c["id"], "file": out.name, "model_returned": rmodel,
                                        "stop_reason": ",".join(stops), "truncated": trunc,
                                        "input_tokens": tin, "output_tokens": tout})
        print(f"  -> stop_reason={','.join(stops)}{'  TRUNCATED' if trunc else ''}", flush=True)
    manifest["finished_kst"] = datetime.datetime.now(KST).isoformat(timespec="seconds")
    mpath.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\nDone. {len(manifest['transcripts'])} transcript(s), manifest {mpath.relative_to(REPO_ROOT)}.")
    if truncated:
        print(f"TRUNCATED: {', '.join(truncated)}. A truncated case is not exercised (ACCEPTANCE.md (a)).")


if __name__ == "__main__":
    main()
