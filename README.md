WebMobi Hybrid Automation (Mock API + UI)
Goal

Automate authentication (mock API), create an event in the real WebMobi UI (Selenium), and verify it appears in the events list. Provide assertions, evidence, and a minimal GitHub Action CI.

Quick File Map

api_part.py — mock API (returns event id & writes last_event.json)

ui_part.py — Selenium UI: logs in, creates event, validates presence; writes artifacts/*

main.py — orchestrator

requirements.txt

helpers/config_example.env — sample env vars (do not commit real creds)

.env (local only) — put real credentials; do not commit

.github/workflows/ci-test.yml — CI workflow

Prerequisites

Python 3.10+

Chrome installed (for local runs)

Git and GitHub account for CI

Setup (Local)

Open project folder.

Create virtual environment and activate:

Windows:

python -m venv venv
venv\Scripts\activate


macOS/Linux:

python -m venv venv
source venv/bin/activate


Install dependencies:

pip install -r requirements.txt


Create .env in project root (do not commit):

BASE_URL=https://events.webmobi.com
EMAIL=your_email@example.com
PASSWORD=YourPasswordHere
HEADLESS=false

Evidence Produced

last_event.json (mock API)

artifacts/events_after_create.png

artifacts/events_list.png

artifacts/ui_result.log

failure.txt (only if failed)

CI (GitHub Actions)

Push repo to GitHub.

Add repository secrets in Settings → Secrets:

EMAIL

PASSWORD

(optional) BASE_URL, HEADLESS

Workflow .github/workflows/ci-test.yml runs on push and uploads artifacts.

What Is Validated

UI login success

Event created via UI (title = mock event id)

Event present in events list (assertion raises error if missing)

Notes

Free WebMobi accounts don’t expose full API; this repo uses a Mock API to satisfy the hybrid requirement and uses real UI automation for creation and validation.

Do not commit .env to GitHub. Keep credentials in GitHub Secrets for CI.
