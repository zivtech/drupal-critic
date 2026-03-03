# drupal-critic

Drupal-specific harsh review skill and agent that focuses on evidence-backed critique for Drupal plans, code, and operational workflows.

## Purpose

`drupal-critic` extends harsh-review workflows with Drupal-specific checks and targeted perspective coverage:
- Core: Security, New-hire, Ops
- Context-driven: Open Source Contributor, Site Builder (Admin UI), Content Editor/Marketer

It is designed as an orchestrator, not a vendorized skill bundle.

## External Skill Policy

This project references external skills by ID/URL and pinned commit metadata.
It does **not** copy external SKILL.md content into this repository.

Reference source of truth:
- `.claude/skills/drupal-critic/references/external-skills-manifest.yaml`

## Project Layout

- `.claude/skills/drupal-critic/SKILL.md` - primary skill behavior
- `.claude/agents/drupal-critic.md` - read-only reviewer agent prompt
- `.claude/skills/drupal-critic/references/` - rubric, routing, manifest, activation matrix
- `scripts/` - manifest refresh + policy validation scripts
- `.github/workflows/validate.yml` - CI checks

## Maintenance

Refresh external references:
```bash
python3 scripts/refresh_external_skills.py
```

Verify no copied third-party skill content:
```bash
python3 scripts/verify_no_copied_skills.py
```

## License

Apache-2.0
