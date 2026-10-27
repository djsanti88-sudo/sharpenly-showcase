# Release timeline

**174 releases shipped; the dated history runs from May 4, 2026 to Oct 26, 2026.** Releases v1 to v66 predate the dated log (the repository's first snapshot, on May 1, was already at v15), so the table counts them separately.

Every release is a numbered, rollback-able snapshot of the app. A release counts only when it was packaged and versioned so returning users get fresh code instead of a stale cache.

## Activity by month

| Month | Releases | Commits |
|---|---:|---:|
| Before May 4 (undated, v1 to v66) | 66 | n/a |
| May 2026 | 76 | 250 |
| June 2026 | 20 | 197 |
| July 2026 | 2 | 107 |
| August 2026 | 1 | 3 |
| September 2026 | 0 | 0 |
| October 2026 | 9 | 175 |
| **Total** | **174** | **732** |

Commit counts are from the app repository's main branch. May is rapid iteration on a live product, June to July goes into content volume, quality, and the manager and hiring side, and the August to September lull is a pause before the October redesign.

## Milestones at a glance

- **Rebrand to Sharpenly** and the study-guide curriculum (v83, v85, May 2026)
- **Curriculum doubled** to 21 categories and 168 lessons, each category with a hero photo (v100 to v106)
- **Security hardening** of data access and sign-in (v115, v117, v141)
- **B2B go-live:** candidate hiring assessment plus employee points and leaderboard (v140)
- **Eight-level structure** for every training track, 16,887 questions at that point (v146)
- **Faster load:** first-load lesson data cut from 4.3 MB to 1.35 MB (v162)
- **Moved hosting to Vercel** with the same security headers (v164)
- **Clean Coach redesign** of all 34 screens, light and dark (v167 to v174)
- **Test suites:** phones, multiple browsers, local emulated backend, pixel baselines, speed budgets (v168)

## October 2026

- **v174** (Oct 26) Weekly-review fix batch: a brake-fade diagram was corrected for accuracy in English and Spanish, and first-run guidance was tightened.
- **v173** (Oct 26) Home screen gains a daily goal ring, a 7-day streak strip, a coach tip, a ranking podium, and a "continue studying" card with bilingual search. A streak-date bug was fixed.
- **v172** (Oct 26) Clean Coach finishing touches: "Learn more" in a quiz opens the real lesson and returns to the quiz, a keyboard skip link, and offline banner polish.
- **v171** (Oct 24) Clean Coach on every screen: infographics redrawn as per-language vector art; badges, lesson elements, results effects, and pop-ups unified.
- **v170** (Oct 24) Lesson art that exists now renders inside lessons. Shipped with the backend upgrade and tighter database rules.
- **v166 to v169** (Oct 18 to 19) Manager live results (each finished level reaches the shop's dashboard), the full Clean Coach redesign in light and dark with a safe-area fix for modern phones, the first complete local test build-out, and an offline-banner and lazy-loading fix.

## September and August 2026

- **v165** (Aug 5) Quality remediation: localized native controls, keyboard-operable home, resume, avatar and ranking actions, stricter browser-proof checks, and safer service-worker cache updates. No releases in September; the time went into the B2B manager dashboard, hiring assessments, and the website.

## July 2026

- **v164** (Jul 6) Hosting migration to Vercel with identical headers and a first-party sign-in proxy. The previous hosting is kept as a rollback path.
- **v163** (Jul 4) Hotfix: a missing character that broke the main script was found and fixed within days, and a guard against that class of error followed.

## June 2026

- **v162** (Jun 29) Performance sprint: 68% less first-load data, 10,589 stray quiz tags cleaned up, accessibility blockers fixed (keyboard tiles, dialogs, reduced motion), badge progress bars, and a level-unlock celebration.
- **v161** (Jun 28) Readable quiz feedback: bold verdict, tap-to-expand "why", in-flow Next button, and an inline visual of the mechanism.
- **v158** (Jun 24) 216 lesson and hero images with graceful gradient fallbacks; failed quiz writes are now logged instead of swallowed.
- **v155 to v157** (Jun 24) Offline write queue, leaderboard de-duplication, "start here" level markers, guest sign-up gate, sharing and shop invites, and an automotive headline hook.
- **v152** (Jun 8) Home learner card driven by each user's real due reviews and daily goal.
- **v143 to v151** (Jun 1 to 7) Questions harvested from lessons (+550), then the **8-level restructure** for every track with Pro Skills (Communication and Leadership), a mobile UX fix sprint, manager prototype, candidate demo, CSV import, and resilient sign-in loading.
- Plus 8 polish releases (contrast, language leaks, tap targets, accessibility labels).

## May 2026

- **v142** (May 31) Design refresh to the brand kit: 15 screens, restored Feed tab, article callouts, safe-area fixes.
- **v141** (May 28) **Security hardening:** score and comment access now require sign-in, database rules tightened, backend functions authenticated.
- **v140** (May 25) **B2B go-live:** candidate hiring assessment page plus employee points, streaks, and leaderboard.
- **v136 to v139** (May 24 to 25) QA sweep: professional answer-feedback tone, light-theme contrast, English leaks in the Spanish build, profile photo upload, new app icon, leaner question bank.
- **v133 to v135** (May 12) Industry-news Feed tab with curated articles, likes, comments, and mixed card layouts.
- **v123 to v132** (May 11) Tire-tech Level 8, UX density cleanup, iOS Safari flashcard and safe-area fixes, clearer right/wrong quiz feedback, longer Google sign-in grace period.
- **v111 to v122** (May 9 to 10) Fail-loud error logging, security hardening of leaderboard rendering, accessibility trio, product analytics for retention and funnels, light/dark contrast pass, mixed-language lesson guard.
- **v109 to v110** (May 6) First-quiz onboarding path and an acquisition survey at 50 XP.
- **v100 to v108** (May 6) **Curriculum doubled:** 13 new categories, 26 topics, 104 generated lessons; hero photos for all 21 categories; uniform banner brightness; privacy and terms links.
- **v92 to v99** (May 6) Pre-demo polish: feedback channel, trust links, analytics, error logging, topic photo banners.
- **v89 to v90** (May 6) Home redesign: 5-tab bottom nav, custom illustrated icons, light-mode contrast.
- **v85** (May 5) **Study Guides:** a four-level curriculum (category, topic, lesson, section).
- **v83** (May 4) **Brand rename to Sharpenly**, with the sharpenlyapp.com domain.
- **v67 to v82** (May 4) Cross-device progress sync, quiz history timeline, custom quiz builder, shop leaderboard, PDF certificate, voice-narrated explanations, review mode, question difficulty calibration, SEO baseline, accessibility focus rings, and tooling (linting, type checks, supply-chain audit, frontend tests).
- Plus roughly 15 polish releases across the month.

## Before May 4 (v1 to v66)

The original quiz app: bilingual multiple-choice training with explanations, role-based tracks, XP and leaderboards, and a content pipeline that turns a reference library into reviewed questions. These releases predate the dated log, so no month-level detail is claimed.

## How releases are made

Each release bumps a cache version, snapshots the built app, and adds a one-line entry to the changelog. Production releases pass an automated pre-launch gate (static checks for silent failures, injection risks, and stale counts) and a post-deploy smoke test against the live site before they count as shipped.
