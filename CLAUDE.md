# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

drupal-critic is a Drupal-specific harsh-review orchestrator for Claude Code. It provides evidence-backed critique of Drupal plans, code, and operational workflows by coordinating external specialist skills — it does **not** vendor or copy external skill content.

The project ships as:
- A Claude Code **skill** (`.claude/skills/drupal-critic/SKILL.md`) — invoked via `/drupal-critic`
- A Claude Code **agent** (`.claude/agents/drupal-critic.md`) — read-only reviewer (opus model, no Write/Edit tools)

## Commands

```bash
# Refresh external skill pinned commits (fetches HEAD SHA from each upstream repo)
python3 scripts/refresh_external_skills.py

# Check if manifest pins are stale (CI mode — exits non-zero if updates needed)
python3 scripts/refresh_external_skills.py --check

# Verify no-copy policy and manifest integrity
python3 scripts/verify_no_copied_skills.py
```

Both scripts require PyYAML: `pip install pyyaml`

CI runs both checks on every push/PR via `.github/workflows/validate.yml` (Python 3.12).

## Architecture

```
.claude/skills/drupal-critic/
├── SKILL.md                          # Skill behavior: review protocol, output contract, routing rules
├── references/
│   ├── external-skills-manifest.yaml # 24 external skills with pinned commits (source of truth)
│   ├── drupal-review-rubric.md       # 9-dimension review checklist
│   ├── audience-activation-matrix.md # Which perspectives activate for which content
│   └── skill-routing-map.md          # How to select max 2-3 external skills per review run
└── agents/
    └── openai.yaml                   # OpenAI interface metadata

.claude/agents/
└── drupal-critic.md                  # Read-only agent prompt (disallows Write/Edit)

scripts/
├── refresh_external_skills.py        # Manifest pin updater
└── verify_no_copied_skills.py        # Policy enforcement (manifest validity, no copied content, no tracked upstream)
```

### Key Design Decisions

- **No-copy policy**: External skills are referenced by ID, `skills_url`, `repo_url`, and `pinned_commit` SHA. Never copy SKILL.md content from external repos into this repository.
- **Orchestration pattern**: drupal-critic loads max 2-3 external specialist skills per review run, selected via the routing map based on review context.
- **Audience model**: Three perspectives always run (Security, New-hire, Ops). Three more activate based on context (Open Source Contributor, Site Builder, Content Editor/Marketer).
- **Evidence requirement**: All CRITICAL/MAJOR findings must include file:line or artifact references.

### External Skills Manifest

`external-skills-manifest.yaml` is the single source of truth for all 24 referenced skills. Each entry contains:
- `id`, `skills_url`, `repo_url`, `pinned_commit` (40-char SHA)
- `categories`, `audiences_supported`, `priority` (40-100), `status` (active/deprecated)

Categories: core-review, security, operations, contrib, cache, canvas, tooling.

### Validation Scripts

`verify_no_copied_skills.py` checks:
1. Manifest field integrity (valid URLs, 40-char SHAs, valid status values)
2. No suspicious copied content markers in SKILL.md
3. All manifest skill IDs referenced in local markdown docs
4. No forbidden tracked paths under `research/drupal-skills/upstream/` or `extracted/`

`refresh_external_skills.py` fetches current HEAD SHA from each upstream GitHub repo via `git ls-remote` and updates `pinned_commit` values in the manifest.

## Working With This Repo

- The `research/` directory contains analysis reports and upstream clones — it is `.gitignore`d except for `reports/`.
- When adding a new external skill reference, add it to the manifest YAML and ensure it is referenced in the routing map and/or rubric docs. Run both validation scripts before committing.
- The agent at `.claude/agents/drupal-critic.md` is intentionally read-only. Do not add Write or Edit to its allowed tools.
