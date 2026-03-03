# Contributing

## Principles

- Keep `drupal-critic` focused on orchestration, review rigor, and Drupal-specific checks.
- Do not copy third-party skill bodies into this repository.
- Reference external skills through the manifest and routing map.

## Required checks

Before opening a PR:

```bash
python3 scripts/verify_no_copied_skills.py
python3 scripts/refresh_external_skills.py --check
```

## Updating external references

1. Run `python3 scripts/refresh_external_skills.py`.
2. Review manifest pin changes.
3. Update routing/docs only if category or coverage changes are required.

## Audience model

Core perspectives always run: Security, New-hire, Ops.

Additional perspectives are context-driven:
- Open Source Contributor
- Site Builder (Admin UI)
- Content Editor/Marketer
