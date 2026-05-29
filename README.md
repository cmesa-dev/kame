<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=venom&color=0:0f172a,50:164e63,100:0f172a&height=200&section=header&text=KAME&fontSize=80&fontColor=67e8f9&animation=fadeIn&fontAlignY=42&desc=The%20coding%20assistant%20that%20always%20picks%20the%20cheapest%20model%20capable%20of%20solving%20your%20task&descAlignY=63&descSize=13&descFontColor=94a3b8" width="100%"/>
</div>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Ollama-local_·_free-000000?style=flat-square"/>
  <img src="https://img.shields.io/badge/Gemini-2.5_Flash-4285F4?style=flat-square&logo=google&logoColor=white"/>
  <img src="https://img.shields.io/badge/GPT--4o-OpenAI-412991?style=flat-square&logo=openai&logoColor=white"/>
  <img src="https://img.shields.io/badge/Claude-Anthropic-CC785C?style=flat-square"/>
  <img src="https://img.shields.io/badge/status-active-22c55e?style=flat-square"/>
  <br/>
  <a href="README.es.md">🇪🇸 Español</a>
</p>

---

## The Problem

You have subscriptions to several AI models but end up using the most expensive one out of habit, even for trivial tasks. A simple "hello" costs the same as a full refactor.

**KAME solves this.** It analyses every request before sending it and automatically decides which is the cheapest model capable of handling it well.

---

## How the Analyser Works

Before making any call, KAME breaks your request into signals:

```
"implement JWT with refresh tokens, Redis blacklist and tests for FastAPI"
         │
         ▼
   parse_query()  ──► intent: generate · domain: backend · modifiers: production
         │
   semantic_triage()  ──► level 5 / Critical architecture
         │
         ▼
   Result: GPT-4o  (the only level capable of solving it well)
```

```
"what's the weather in Seville?"
         │
         ▼
   intent: search · level 1 / Trivial query
         │
         ▼
   Result: Gemini Flash  (sufficient, ~100× cheaper)
```

```
"hi"  ──►  level 1  ──►  Local Ollama  (cost: $0)
```

No manual configuration. No `/model gpt-4o` before every message. The right level of power for each task.

---

## Routing Levels

| Level | Task type | Chosen model |
|:---:|---|---|
| 1 | Greeting, trivial query | Local Ollama · free |
| 2 | Quick question, short explanation | Local Ollama / Gemini Flash |
| 3 | Standard editing, minor refactor | Gemini Flash |
| 4 | Complex bug, deep debugging | GPT-4o-mini / GPT-4o |
| 5 | Architecture, security, multi-file | GPT-4o / Claude Sonnet/Opus |

Local models (Ollama, LM Studio) are always preferred when capable. The API is only used when the problem requires it.

---

## More Than a Router

### 🛠 Real Tools
KAME reads your project, executes commands and searches the web during reasoning:
```
read_file · run_command · search_code · grep_codebase
web_search · web_fetch · git_status · list_dir
```

### 🧠 Semantic Memory Across Sessions
Every conversation is vectorised locally in ChromaDB. KAME remembers previous decisions and retrieves them automatically when relevant — without you repeating yourself.

### 🐝 Swarm Mode
For architecture tasks, three agents collaborate in a pipeline:
```
Architect (GPT-4o)  →  QA & Security (Gemini)  →  Lead Dev (GPT-4o)
```
Each role critiques the previous one. The result is an implementation plan with directly applicable `SEARCH/REPLACE` blocks.

### 💸 Cost Tracking
Every cloud call records tokens and cost in USD. When you close the session you see exactly how much you spent.

---

## Main Commands

```bash
kame chat                    # Interactive session
kame ask "explain this bug"  # Quick query about the project
kame route "your request"    # Shows which model would be used and why
kame budget                  # Status of all available backends
kame agent "task"            # Agent: plans, reads the repo and proposes changes
kame swarm "complex task"    # Pipeline Architect → QA → Coder
kame work "task"             # Autonomous loop until tests pass
```

---

## Quick Start

```bash
# Local inference (recommended, no cost)
ollama pull qwen2.5-coder:7b

# Install KAME
pip install kameia

# Optional cloud keys in .env
OPENAI_API_KEY=...
GEMINI_API_KEY=...
ANTHROPIC_API_KEY=...

# Start
kame chat
```

With no keys configured, KAME runs 100% locally.

---

## Status & Roadmap

KAME is under active development. **The goal is to release the first public version before August 2026.**

---

## Why Open Source

KAME is my first serious AI project. I'm a developer, not a researcher — and I'm the first to admit I'm not the best at building AI systems. But I think that's exactly the reason to open it up.

The foundation is there: the request analyser, the routing, the memory, the tools. What one person can do alone has a limit. What a community can do, doesn't.

If someone improves the router, another the memory, another adds a better interface or integrates a new provider — the result is a product none of us would have built alone. An open-source coding assistant, maintained by developers for developers — no fixed subscriptions or fees. You only pay your real API consumption, with each request analysed and routed by KAME so the cheapest capable model resolves the task: better performance, lower cost.

**If you're interested in contributing, improving something, or simply following the project — you're welcome.**

---

<p align="center">
  <a href="https://www.linkedin.com/in/carlos-mesa-viera-747501197">
    <img src="https://img.shields.io/badge/Carlos%20Mesa%20Viera-LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://github.com/cmesa-dev">
    <img src="https://img.shields.io/badge/cmesa--dev-GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://cmesa-dev.github.io/cv/es.html">
    <img src="https://img.shields.io/badge/CV-Español-6d28d9?style=for-the-badge&logo=read-the-docs&logoColor=white"/>
  </a>
  &nbsp;
  <a href="https://cmesa-dev.github.io/cv/index.html">
    <img src="https://img.shields.io/badge/CV-English-6d28d9?style=for-the-badge&logo=read-the-docs&logoColor=white"/>
  </a>
</p>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f172a,100:164e63&height=90&section=footer" width="100%"/>
