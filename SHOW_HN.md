# Show HN post — Redline

## Title (keep it under 80 chars)
Show HN: Redline – an AI code reviewer that fact-checks its own findings

## URL
https://redline-cs25.onrender.com

## First comment (post this yourself right after submitting)

I got tired of LLM code reviewers crying wolf — they flag plausible-sounding
"issues" that aren't real, and you quickly learn to ignore them. So I built
Redline around a two-stage pipeline:

1. **Find** — an LLM pass flags defects in a git diff or GitHub PR.
2. **Verify** — a *separate, adversarial* pass whose only job is to REFUTE each
   finding. Only the ones that survive get shown.

That second pass is the whole point: it's what kills the false positives that
make naive LLM reviewers untrustworthy. Findings are grounded to exact
file:line via unified-diff parsing, ranked by severity, and it can review real
GitHub PRs and post inline comments.

Try it with zero setup: open the link and hit "Load demo diff → Review code" —
it catches all 8 planted bugs in the sample (SQL injection, a function that
returns success when it didn't act, non-atomic balance updates, an unclosed
file, a swallowed exception, etc.), and you can watch the find→verify trace
stream live.

Stack: Python/FastAPI, any OpenAI-compatible LLM (I default to Groq's
gpt-oss-120b because it's fast and free), SSE for the live trace, a small
React UI. Code: https://github.com/Sair0703/Redline

Honest limitations I'd love feedback on:
- It reviews the diff + a window of surrounding file context, not the whole
  repo, so cross-file bugs can slip through. Whole-repo retrieval is the
  obvious next step.
- I tuned it for precision over recall — I'd rather show 3 real bugs than 10
  maybes — but that means it'll miss things.
- The demo runs on a free tier, so the first request may take ~30s to wake.

Would especially appreciate thoughts on the verification approach — is
"adversarial second pass" the right way to cut false positives, or is there a
better pattern?

## Where to post
- news.ycombinator.com → "submit" (title + URL above), then paste the comment.
- Also good: r/programming, r/coding, and a LinkedIn post linking the live demo.
- Best days/times for Show HN: weekday mornings US Pacific.

## Tip
Ask a couple of friends to genuinely try it and comment — early engagement
helps it stay on the /show page long enough to get real traffic + stars.
