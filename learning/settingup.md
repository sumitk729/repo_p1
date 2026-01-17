# Design a Codespaces-safe + local-first workflow

## 🎯 Design Principle (Non-Negotiable)

> Local-first for competence. Codespaces-safe for continuity.

If Codespaces disappears tomorrow, your work must continue without loss.
If your laptop breaks today, Codespaces must let you move forward.

That’s the bar.

1️⃣ Core Architecture (This Is the Spine)
Repo structure (works identically everywhere)

```
project-name/
│
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
│
├── src/
│   ├── __init__.py
│   ├── main.py
│   └── modules/
│
├── notebooks/
│
├── tests/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── scripts/
│
├── requirements.txt
├── requirements-dev.txt
├── pyproject.toml   (optional but ideal)
├── README.md
└── .gitignore
```

2️⃣ Environment Strategy (The Most Important Part)
Rule

> One source of truth: Docker

Local machine

* Install:
    * Docker
    * VS Code

* Open repo → “Reopen in Container”

Codespaces

* Open repo → “Create Codespace”
* Same .devcontainer/
* Same Dockerfile
* Same Python, same versions

Result

No “works on my machine” nonsense.

Minimal Dockerfile
```
FROM python:3.11-slim

WORKDIR /workspace

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
```
This is deliberately boring. Boring = stable.

3️⃣ Git Workflow (Zero Confusion, Zero Drama)
Branching

* main → always stable

* dev → active work

* feature/* → experiments

Daily rule

* Commit small

* Commit often

* Messages like:

```
feat: add NFHS data loader
fix: handle missing district codes


```

If you don’t commit daily, you’re lying to yourself about progress.

4️⃣ Codespaces Usage Rules (Discipline Required)
Allowed in Codespaces

✅ Running code

✅ Quick experiments

✅ Fixing bugs

✅ Reviewing PRs

✅ Writing tests

✅ Emergency access


Forbidden mindset

❌ “I’ll learn Python properly inside Codespaces”

❌ “I’ll debug complex logic on a tablet”

Codespaces is a battlefield hospital, not a gym.

5️⃣ Local Workflow (Where Growth Happens)
Daily local routine

1. Pull latest changes

1. Run tests

1. Write code

1. Commit

1. Push

Weekly ritual (non-negotiable)

* Break something intentionally

* Fix it

* Write a test for it

This is how confidence is built.

6️⃣ Data Handling (This Saves You From Disaster)
Rules

❌ Never commit raw large data

✅ Commit scripts that generate data

✅ Use .gitignore aggressively

```
data/raw/*
data/processed/*

```

If your repo exceeds 100MB, you’ve failed basic hygiene.

7️⃣ Notebook Discipline (Most People Screw This Up)
Rules

* Notebooks = exploration only

* Production logic = src/

* Every notebook must:

    * Run top to bottom

    * Be reproducible

    * Export logic to .py eventually

If notebooks become your main codebase, your project is already dead.

8️⃣ Testing Strategy (Yes, Even for You)

Minimum bar:

```
tests/
├── test_data_loader.py
├── test_utils.py

```

Run

```
pytest
```

If tests don’t exist, bugs are just waiting to embarrass you.

9️⃣ Fallback Matrix (Reality Planning)
| Situation | What You Do |
|-----------|-------------|
| Laptop crashes | Codespaces |
| Internet bad	 | Local |
| Traveling	     | Tablet + Codespaces |
| Experimenting	 | Feature branch |
| Deadline near	 | Local + tests |

No panic. No improvisation.

🔥 What “Best-in-Class” Looks Like (Aspirational)

Top 5% practitioners:

* Same repo runs on:

    * Laptop

    * Codespaces

    * CI pipeline

* One command:

```
make setup
make test
make run

```

* README explains:

    * Problem

    * Architecture

    * Repro steps

* Anyone can clone and run in 10 minutes

That’s the cover drive you should be watching.

**Final Hard Truth (Coach Mode)**

If you design for convenience first, you’ll stay average.
If you design for robustness, convenience follows automatically.

You’re capable of the second path.
Most people aren’t willing to do it.