<div align="center">

# Sharpenly

**Bilingual training where every AI-generated question passes a quality gate first.**
An EN/ES learning app, a manager dashboard, and the LLM data-quality pipeline behind ~20,000 questions.

[![Live app](https://img.shields.io/badge/Live%20app-app.sharpenlyapp.com-2e7d32?style=for-the-badge)](https://app.sharpenlyapp.com)
[![Website](https://img.shields.io/badge/Website-sharpenlyapp.com-1b5e20?style=for-the-badge)](https://sharpenlyapp.com)
[![Manager demo](https://img.shields.io/badge/Manager%20demo-no%20login-0d47a1?style=for-the-badge)](https://sharpenlyapp.com/manager-preview)
[![Languages](https://img.shields.io/badge/Languages-EN%20%2F%20ES-6a1b9a?style=for-the-badge)](https://app.sharpenlyapp.com)

<img src="docs/screenshots/app-strip.png" alt="Sharpenly app screens: a lesson, a quiz with feedback, and the Spanish home screen" width="100%">

</div>

> The source of the production app is private. This repo is a curated, read-only showcase:
> screenshots, a data-quality case study, real sample questions, and trimmed code excerpts.

## For AI data and LLM-evaluation reviewers: start here

I built and measured a pipeline that has an LLM write 11,870 bilingual (EN/ES) training questions, then rejects or escalates the weak ones against a written rubric.

- **Rubric and gate:** 15 written rules, enforced in code wherever a rule can check it, otherwise by human review. [RUBRIC.md](data-quality/RUBRIC.md), [gate_excerpt.py](data-quality/gate_excerpt.py)
- **Measured iteration:** first pilot accepted 14% of items; after fixing the prompt and gate, a targeted repilot accepted 84%. [Case study](data-quality/README.md)
- **Failure analysis:** a batch reported 617 of 617 requests "succeeded" and produced zero usable questions. [Postmortem](data-quality/POSTMORTEM.md)
- **Bilingual QA:** English and Spanish answers must line up by position. [validators_excerpt.py](data-quality/validators_excerpt.py), [20 real samples](data-quality/samples/questions_sample.json)
- **Run it yourself:** `python data-quality/run_checks.py` (standard library only) validates the 20 samples and shows why the gate uses a proportional length rule: the strict rule flags 17 of 20 good items, the proportional rule flags 0.
- **Honest limits:** the gate's agreement with human judges is not yet measured. The case study says so and lays out the study I would run next.

## Try it

- Live app: <https://app.sharpenlyapp.com>
- Website: <https://sharpenlyapp.com>
- Manager dashboard demo (no login): <https://sharpenlyapp.com/manager-preview>
- Candidate assessment demo (no login): <https://sharpenlyapp.com/candidate-preview>

### Install in 30 seconds

| Device | Steps |
|---|---|
| iPhone (Safari) | Open the app, tap Share, tap Add to Home Screen. |
| Android (Chrome) | Open the app, open the menu, tap Install app. |
| Desktop (Chrome or Edge) | Click the install icon in the address bar. |

The app works offline after the first load.

## At a glance

| What | Number |
|---|---|
| Bilingual EN/ES questions | 20,308 in 71 bank files |
| Study lessons | 168 across 21 categories |
| Difficulty levels per track | 8 |
| App releases shipped | 174 |
| Python test functions | 458 |
| Cloud Functions | 12 |
| Commits | 730 |
| Questions the AI pipeline generated in its full batch | 11,870 |
| Accepted by the automated gate / sent to human review / rejected | 10,356 / 451 / 1,063 |
| First pilot acceptance, then after the fix | 14% (7/50), then 84% (21/25) |

## For managers

The manager dashboard shows who is trained, who is not, and where the skill gaps are. Try it without logging in: <https://sharpenlyapp.com/manager-preview>.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="docs/screenshots/dashboard-heatmap-dark.png">
  <img src="docs/screenshots/dashboard-heatmap.gif" alt="Skills-gap heatmap: employees by topic" width="100%">
</picture>

| Feature | Status |
|---|---|
| Alerts and KPI tiles | Live |
| Skills-gap heatmap (employees by topic; 9 topics in the demo) | Live |
| Training compliance | Live |
| Employee drill-down | Live |
| Team join code, rotate, deactivate | Live |
| CSV export | Live |
| Candidate invite links | Live |
| Candidate report card with fit rating | Live |
| Integrity trust signals (aggregate tab-hidden and paste counts, shown as "review recommended") | Live |
| Proctored stage 2 exam | Live |
| Convert a candidate to an employee | Live |
| Leaderboard | Live |
| English and Spanish, light and dark | Live (the public preview is English only) |
| Auto-remediation assignments | Demo only |
| Stripe billing | Coded, not live |

<table align="center">
  <tr>
    <td><img src="docs/screenshots/dashboard-overview.png" alt="Dashboard overview with alerts and KPI tiles" width="100%"></td>
    <td><img src="docs/screenshots/candidate-report.png" alt="Candidate report card with fit rating" width="100%"></td>
    <td><img src="docs/screenshots/team.png" alt="Team management with join code" width="100%"></td>
  </tr>
  <tr>
    <td align="center">Overview</td>
    <td align="center">Candidate report</td>
    <td align="center">Team</td>
  </tr>
  <tr>
    <td><img src="docs/screenshots/hiring.png" alt="Hiring pipeline with candidate invite form" width="100%"></td>
    <td><img src="docs/screenshots/dashboard-assignments.png" alt="Employee detail with an auto-remediation assignment" width="100%"></td>
    <td><img src="docs/screenshots/site-es.png" alt="Spanish marketing site with the heatmap preview" width="100%"></td>
  </tr>
  <tr>
    <td align="center">Hiring pipeline</td>
    <td align="center">Employee detail + remediation (demo)</td>
    <td align="center">Website in Spanish</td>
  </tr>
</table>

Screens show the public demo shop with sample data; the names are fictional.

## For employees

Short quizzes, scenario questions, and lessons built from four typed section primitives: flashcard, hotspot, sequence, scenario. Progress, streaks, and a ranking keep people coming back.

<table align="center">
  <tr>
    <td><img src="docs/screenshots/app-quiz.png" alt="Quiz question with explanation" width="100%"></td>
    <td><img src="docs/screenshots/app-lesson.png" alt="Study lesson" width="100%"></td>
    <td><img src="docs/screenshots/app-home-es.png" alt="Home screen in Spanish" width="100%"></td>
    <td><img src="docs/screenshots/app-ranking.png" alt="Ranking screen" width="100%"></td>
  </tr>
  <tr>
    <td align="center">Quiz</td>
    <td align="center">Lesson</td>
    <td align="center">Home (Spanish)</td>
    <td align="center">Ranking</td>
  </tr>
</table>

## For candidates

A manager sends an invite link. The candidate takes a timed assessment. The manager gets a report card.

<table align="center">
  <tr>
    <td><img src="docs/screenshots/candidate-intro.png" alt="Candidate assessment intro" width="100%"></td>
    <td><img src="docs/screenshots/candidate-exam.png" alt="Candidate exam question" width="100%"></td>
  </tr>
  <tr>
    <td align="center">Intro</td>
    <td align="center">Exam</td>
  </tr>
</table>

## The AI content pipeline

Questions are generated from a curated corpus of automotive reference material. Nothing reaches a learner until it passes a rubric gate and a human check.

```mermaid
flowchart LR
    A[Curated corpus of automotive reference material] --> B[Vector index<br/>MiniLM embeddings]
    B --> C[Role-filtered retrieval]
    C --> D[LLM generation<br/>Claude Sonnet 4.5]
    D --> E{Rubric gate}
    E -->|accept| G[Bilingual QA]
    E -->|review| F[Human review]
    E -->|reject| X[Discarded, reason logged]
    F --> G
    G --> H[8-level staging]
    H --> I[App]
```

- Retrieval uses Chroma with `sentence-transformers/all-MiniLM-L6-v2`, filtered by role so a service-advisor question is grounded in service-advisor material.
- Each item must cite the passage it came from. Citations are stripped from this public repo.
- The gate checks structure, trivia, recall-style stems, theory that does not belong on a shop floor, answer-length giveaways, and near-duplicates by embedding similarity.
- A run only counts as a success if the output parsed and questions survived the gate. See the postmortem below.

## Data-quality work (what this proves)

| Skill | Artifact |
|---|---|
| Defining a quality rubric for training data | [data-quality/RUBRIC.md](data-quality/RUBRIC.md) |
| Turning a rubric into an automated gate | [data-quality/gate_excerpt.py](data-quality/gate_excerpt.py) |
| Bilingual validation (EN/ES alignment) | [data-quality/validators_excerpt.py](data-quality/validators_excerpt.py) |
| Measuring iteration: pilot, fix, repilot, full batch | [data-quality/README.md](data-quality/README.md) |
| Failure analysis and prevention rules | [data-quality/POSTMORTEM.md](data-quality/POSTMORTEM.md) |
| Real bilingual samples across roles and levels | [data-quality/samples/questions_sample.json](data-quality/samples/questions_sample.json) |

Headline result: first pilot accepted 14% of items. After tightening the prompt and the gate, a smaller, targeted repilot accepted 84% with 0 rejected, and cost per kept item fell about 4.4x. A later batch where the API reported 617 of 617 requests "succeeded" produced 0 usable questions. That led to one rule: product success, not API success.

## Engineering

| Layer | Stack |
|---|---|
| App | Installable single-file web app (PWA) with offline support, Firebase Realtime Database and Auth, Vercel |
| Site and dashboard | Next.js 16, TypeScript, Tailwind CSS 4, next-intl (EN/ES), Playwright and axe-core |
| Backend | 12 Firebase Cloud Functions (Node 22) |
| Content pipeline | Python, Chroma, sentence-transformers, Claude Sonnet 4.5 |

- Testing: 458 Python test functions, Playwright end-to-end tests, visual-regression baselines.
- CI: GitHub Actions for tests, a pre-release launch gate, and a scheduled security scan.
- Security: audits for XSS sinks, silent write failures, and public-data hygiene run before every release. A smoke test runs against the live deploy.

More detail in [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

## About me

- Name: TODO
- LinkedIn: TODO
- Email: djsanti88@gmail.com
- GitHub: [djsanti88-sudo](https://github.com/djsanti88-sudo)

Open to AI data annotation, LLM evaluation, and AI training-data roles.

---

Copyright (c) 2026 Santiago. See [LICENSE.md](LICENSE.md).
