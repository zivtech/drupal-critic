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

## Referenced External Skills

The current referenced skills are:

- `madsnorgaard/agent-resources/drupal-expert`
- `madsnorgaard/agent-resources/drupal-security`
- `bethamil/agent-skills/drupal-update`
- `mindrally/skills/drupal-development`
- `scottfalconer/drupal-issue-queue/drupal-issue-queue`
- `scottfalconer/drupal-contribute-fix/drupal-contribute-fix`
- `kanopi/cms-cultivator/drupalorg-issue-helper`
- `kanopi/cms-cultivator/drupalorg-contribution-helper`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-contexts`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-tags`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-maxage`
- `sparkfabrik/sf-awesome-copilot/drupal-dynamic-cache`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-debugging`
- `sparkfabrik/sf-awesome-copilot/drupal-lazy-builders`
- `drupal-canvas/skills/canvas-component-definition`
- `drupal-canvas/skills/canvas-component-metadata`
- `drupal-canvas/skills/canvas-component-utils`
- `drupal-canvas/skills/canvas-data-fetching`
- `drupal-canvas/skills/canvas-styling-conventions`
- `drupal-canvas/skills/canvas-component-composability`
- `drupal-canvas/skills/canvas-component-upload`
- `grasmash/drupal-claude-skills/drupal-ddev`
- `omedia/drupal-skill/drupal-tooling`
- `madsnorgaard/drupal-agent-resources/ddev-expert`

Update source:
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
