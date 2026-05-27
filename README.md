<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:164e63&height=190&section=header&text=KAME&fontSize=72&fontColor=67e8f9&animation=fadeIn&fontAlignY=39&desc=Auditable%20Operations%20Workflow%20Demo&descAlignY=57" width="100%"/>
</div>

<div align="center">
  <img src="https://img.shields.io/badge/Workflow-Executable-0891B2?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Public%20Code-Python-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Inputs-Synthetic%20Only-334155?style=for-the-badge"/>
</div>

## Problem

Operational teams need concise incident briefings without losing the evidence behind them. KAME is a public, bounded workflow demo that turns a local incident dataset into a prioritised Markdown briefing and a machine-readable execution trace.

This repository does not claim to be an autonomous LLM agent. It demonstrates the deterministic orchestration, tool boundaries and traceability that a broader private automation project can build upon.

## What I Built

- A Python workflow agent with an explicit three-step plan.
- A validated synthetic incident source under `examples/`.
- Real tools for loading data, prioritising active incidents and writing a report.
- A JSON trace containing every executed step and its result.
- Unit tests and a GitHub Actions verification workflow.

## Run Locally

No API keys or third-party packages are required.

```bash
python -m kame.cli
```

Or record a custom request in the generated brief:

```bash
python -m kame.cli "Prepare the morning reliability handoff."
```

Generated artifacts are written to `runs/latest/`:

```text
runs/latest/operations-brief.md
runs/latest/trace.json
```

An example generated artifact is committed at [docs/sample-operations-brief.md](docs/sample-operations-brief.md).

## Verify

```bash
python -m unittest discover -s tests -v
```

## Workflow

```text
Task
  -> Planner creates a bounded plan
  -> load_incidents reads validated synthetic JSON
  -> analyse_incidents prioritises non-resolved work
  -> write_brief creates Markdown report
  -> trace.json records the execution
```

## Engineering Decisions

| Decision | Reason | Future extension |
|---|---|---|
| Deterministic local workflow | Reviewers can execute and validate behavior without credentials | Add an optional approved model provider for narrative synthesis |
| Synthetic incident records | Keeps the public repository safe to share | Replace with authenticated incident-system connector |
| JSON trace beside the report | Makes each action inspectable | Add structured evaluations, retries and observability exports |

## Scope Boundary

The private original project is not published here. This repository proves public implementation of planning, data processing, report generation and tracing only; it does not assert external tools, autonomous actions or LLM integration.
