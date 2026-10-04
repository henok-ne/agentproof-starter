# AgentProof Starter

A demonstration test kit for AI chatbots, copilots, and agents.

## What this demonstrates

AI systems should be tested for more than whether they return an answer. They
should also be tested for:

- Unsupported claims
- Hallucinations
- Privacy failures
- Prompt injection
- Ambiguous requests
- Multi-turn behavior
- Unauthorized actions
- Regression after prompt or model changes

## Demo product

The fictional product in this repository is TaskFlow, a SaaS project
management platform.

The knowledge base contains plans, cancellation rules, support response times,
data export information, and security policies.

## Files

- `knowledge_base.md` — fictional source of truth.
- `test_cases.yaml` — 20 example AI QA scenarios.
- `run_tests.py` — loads and displays the test cases.
- `sample_report.md` — example QA findings.
- `.gitignore` — excludes local files and secrets.

## Run locally

Create and activate a virtual environment:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install pyyaml
```

Run the test case loader:

```powershell
python run_tests.py
```

## Important

This is a demonstration project using fictional data. It is not a security
certification or a report about a real company.