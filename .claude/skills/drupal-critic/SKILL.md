---
name: drupal-critic
description: Drupal-specific harsh review orchestration for plans, code, and implementation notes. Use when reviewing Drupal modules/themes/config/deploy workflows, contrib patch decisions, cache behavior, migration plans, Drush/DDEV/Composer updates, or any Drupal change where you need evidence-backed critique. Always run security/new-hire/ops perspectives; activate open-source-contributor, site-builder, and content-editor perspectives when context indicates they will reveal additional fixes.
---

# Drupal Critic

## Overview
Run a harsh-critic style review with Drupal-specific checks, explicit evidence requirements, and context-driven audience perspectives.

## External Skill References (No Copy Policy)
Use external skills as references only.

- Canonical reference file: [external-skills-manifest.yaml](references/external-skills-manifest.yaml)
- Routing policy: [skill-routing-map.md](references/skill-routing-map.md)

Rules:
- Do not copy external skill body content into this repository.
- Use manifest IDs/URLs and pinned commit metadata for traceability.
- If a referenced skill is unavailable in runtime, continue with local rubric fallback and state the limitation.

## Workflow
1. Confirm review target and scope.
2. Run harsh-critic protocol: pre-commitment, verification, multi-perspective analysis, gap analysis, synthesis.
3. Apply Drupal rubric from [drupal-review-rubric.md](references/drupal-review-rubric.md).
4. Activate perspectives based on [audience-activation-matrix.md](references/audience-activation-matrix.md).
5. Load at most 2-3 specialist external skills from the routing map when needed.
6. Return structured verdict with evidence.

## Required Output Contract
Use this exact top-level structure:
- `VERDICT: [REJECT | REVISE | ACCEPT-WITH-RESERVATIONS | ACCEPT]`
- `Overall Assessment`
- `Pre-commitment Predictions`
- `Critical Findings`
- `Major Findings`
- `Minor Findings`
- `What's Missing`
- `Multi-Perspective Notes`
- `Verdict Justification`
- `Open Questions (unscored)`

Rules:
- CRITICAL and MAJOR findings must include concrete evidence (`file:line` or backtick-quoted artifact reference).
- If a section has no items, write `None.`
- Keep speculative points in `Open Questions` only.

## Perspectives
Always run:
- Security
- New-hire
- Ops

Context-driven (activate when triggered):
- Open Source Contributor
- Site Builder (Drupal admin UI)
- Content Editor/Marketer

Perspective notes must appear in `Multi-Perspective Notes`.

## Drupal-Specific Must-Check List
Always check these before final verdict:
- Contrib-first decision quality: should this be upstream patch/work instead of custom code?
- Access and trust boundaries: routes, entity queries, permissions, token checks.
- Render safety: `#markup`, Twig raw output, sanitization path.
- Cache correctness: tags/contexts/max-age and BigPipe/Dynamic Page Cache implications.
- Config workflow safety: `drush cex/cim`, environment drift and import risk.
- Update/deploy safety: composer constraint risk, DB updates, rollback/snapshot path.
- Migration safety: source assumptions, idempotency, replay/rollback behavior.
- Operability: logging, failure handling, and blast radius.

## Skill Loading Rules
- Default: one core review skill + one specialist skill.
- Avoid loading overlapping core skills simultaneously unless scope is broad.
- Prefer higher-priority, active entries in external manifest.

## Severity Calibration
- CRITICAL: exploit/security bypass/data-loss/deploy-blocking flaws.
- MAJOR: likely regressions or significant rework required.
- MINOR: non-blocking correctness/maintainability issues.
- Do not inflate severity for style-only points.

## Stop Conditions
- If review scope is too broad, narrow by component/feature/path.
- If evidence cannot be found, move concern to `Open Questions`.
