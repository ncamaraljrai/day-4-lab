# Build a Feature List with WIP=1 and VCR Enforcement

This repository contains the Module 4 lab for **Harness Engineering for Production AI Agents**. It uses a small FastAPI Notes API to compare an unconstrained backlog run against a strict WIP=1 + Verified Completion Rate (VCR) gate on the same five-feature backlog.

## Required deliverables

- [`feature_list.json`](feature_list.json) — final structured primitive with `behavior`, executable `verification`, `state`, and `evidence` for every feature.
- [`COMPARISON.md`](COMPARISON.md) — line counts, files touched, features passing, and both VCR calculations.
- [`REFLECTION.md`](REFLECTION.md) — exactly three reflection sentences covering code volume, overreach, and re-scoping.

Supporting evidence is in [`WIP1_AUDIT.md`](WIP1_AUDIT.md) and [`RUN_EVIDENCE.md`](RUN_EVIDENCE.md).

## Results

| Metric | Control | WIP=1 Treatment |
|---|---:|---:|
| Changed lines | 92 | 68 |
| Files touched | 8 | 3 |
| Features passing | 2/5 | 5/5 |
| VCR | **0.40** | **1.00** |

## Run locally

```bash
python -m pip install -r requirements.lock
python -m pytest -q
python -m uvicorn app.main:app --app-dir src --port 8000
```

The exact verification command for every feature lives in `feature_list.json`.

## Granularity correction

The initial concept “manage notes” was rejected because it was too broad to prove with one verification command. It was decomposed into create, read, list, update, and delete behaviors.

## Integrity note

This is a controlled assistant replay. All reported VCR values, git statistics, and pytest results came from the experiment rather than the lesson's example numbers.
