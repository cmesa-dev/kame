<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f172a,50:164e63,100:0f172a&height=200&section=header&text=KAME&fontSize=80&fontColor=67e8f9&animation=fadeIn&fontAlignY=42&desc=Local-first%20AI%20assistant%20with%20smart%20multi-LLM%20routing&descAlignY=62&descSize=16&descFontColor=94a3b8" width="100%"/>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ollama-local_first-000000?style=flat-square"/>
  <img src="https://img.shields.io/badge/OpenAI-GPT--4o-412991?style=flat-square&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/Claude-Sonnet_·_Opus-CC785C?style=flat-square"/>
  <img src="https://img.shields.io/badge/status-active-22c55e?style=flat-square"/>
</p>

---

## What is KAME?

KAME is a terminal-based AI coding assistant that **routes each query to the cheapest capable model automatically** — running local inference first and only escalating to cloud APIs when the task demands it.

No API key required to start. No cloud bill for simple tasks.

---

## How routing works

Every message goes through a complexity classifier (levels 1–5) before any model is called:

```
Your query
    │
    ▼
Complexity analysis  ─────────────────────────────────────────────┐
    │                                                             │
    │  Level 1-2 (trivial/fast)                                  │
    ├──► Ollama local model  ·  3b-ish  ·  free  ·  instant      │
    │                                                             │
    │  Level 3-4 (medium / code)                                 │
    ├──► Ollama 7-14b  ──fail──►  Gemini 2.5 Flash  ──fail──►   │
    │    GPT-4o-mini                                              │
    │                                                             │
    │  Level 5 (architecture / math / reasoning)                 │
    └──► deepseek-r1 / qwq local  ──fail──►  GPT-4o / Claude    ─┘
```

If a provider is unavailable or times out, KAME falls back to the next tier silently. Local models are preferred at every level where they are capable enough.

---

## Features

### 🔀 Smart multi-LLM routing
Detects task complexity and domain (code, web, math, architecture) to pick the right model. Supports Ollama, LM Studio, OpenAI, Gemini and Anthropic in the same session.

### 🧠 Semantic memory
Conversations are embedded and stored in a local ChromaDB vector database. KAME recalls relevant past context automatically — no manual `/remember` commands needed. Deduplication prevents noise.

### 🛠 Tool use
KAME executes real tools during reasoning:
- `read_file` — reads any project file
- `run_command` — runs shell commands safely
- `search_code` / `grep_codebase` — regex and ripgrep search across the codebase
- `web_search` / `web_fetch` — searches and reads URLs
- `git_status` — shows repo state and diff
- `list_dir` — navigates the file tree
- `smart_search` — combines web results with local RAG knowledge

### 🐝 Multi-agent swarm
Complex architectural tasks spin up a three-role pipeline:

```
Architect (GPT-4o)  ──►  QA & Security (Gemini)  ──►  Lead Dev (GPT-4o)
```

Each role sees the previous output and builds on it, producing a final implementation plan with `SEARCH/REPLACE` patches.

### 💸 Cost tracking
Every cloud API call is tracked. KAME prints session cost on exit so you know exactly what you spent.

### 🔌 Offline-first
With Ollama installed and any local model pulled, KAME works fully offline. Cloud providers are opt-in.

---

## Stack

| Layer | Technology |
|---|---|
| Runtime | Python 3.11+ |
| Local inference | Ollama · LM Studio |
| Cloud providers | OpenAI · Gemini · Anthropic |
| Vector memory | ChromaDB |
| CLI / UI | Typer · Rich · prompt_toolkit |
| Web tools | urllib (zero dependencies) |

---

## Requirements

```bash
# Local inference (optional but recommended)
# https://ollama.com — then pull any model:
ollama pull qwen2.5-coder:7b

# Python dependencies
pip install kameia
```

Cloud API keys are read from `.env` in the project root:

```env
OPENAI_API_KEY=...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=...
```

No key = no cloud calls. KAME stays local.

---

## Usage

```bash
# Start interactive session
kame

# Ask directly
kame "Refactor this module to use async/await"

# Force a specific provider
kame --provider gemini "Explain this regex"

# Multi-agent swarm on a complex task
kame swarm "Design a rate-limited job queue with retry logic"
```

---

## Status

Private project — actively developed. This repository documents the public interface and architecture. The full source is not published.

---

<p align="center">
  <a href="https://linkedin.com/in/carlosmesaviera">
    <img src="https://img.shields.io/badge/Carlos%20Mesa%20Viera-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://cmesa-dev.github.io/cv/">
    <img src="https://img.shields.io/badge/CV-online-6d28d9?style=for-the-badge&logo=read-the-docs&logoColor=white"/>
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:164e63&height=90&section=footer" width="100%"/>
