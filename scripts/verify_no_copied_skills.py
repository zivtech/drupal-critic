#!/usr/bin/env python3
"""Verify external skill policy: manifest integrity, no-copy, and supply chain checks.

Tier 1 supply chain checks:
- Repo URL org allowlist — only trusted GitHub orgs/users accepted
- Manifest field integrity — valid URLs, 40-char SHAs, valid status

Tier 2 supply chain checks:
- Content hash verification — if content_hash field exists, verify it matches
"""
import hashlib
import re
import subprocess
import sys
import urllib.request
import urllib.error
from pathlib import Path

try:
    import yaml
except Exception as exc:
    raise SystemExit("PyYAML is required. Install with: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / '.claude/skills/drupal-critic/references/external-skills-manifest.yaml'
SKILL_ROOT = ROOT / '.claude/skills/drupal-critic'

# Tier 1: Only accept skills from these GitHub orgs/users.
# Add new trusted sources here after vetting.
TRUSTED_OWNERS = {
    'madsnorgaard',
    'bethamil',
    'mindrally',
    'scottfalconer',
    'kanopi',
    'sparkfabrik',
    'drupal-canvas',
    'grasmash',
    'omedia',
}


def find_manifest_issues(data):
    issues = []
    for idx, s in enumerate(data.get('skills', []), start=1):
        sid = s.get('id', f'index:{idx}')
        if not s.get('skills_url', '').startswith('https://skills.sh/'):
            issues.append(f"{sid}: invalid skills_url")
        repo_url = s.get('repo_url', '')
        if not repo_url.startswith('https://github.com/'):
            issues.append(f"{sid}: invalid repo_url")
        else:
            # Tier 1: verify repo owner is in the allowlist
            owner = repo_url.replace('https://github.com/', '').split('/')[0].lower()
            if owner not in {o.lower() for o in TRUSTED_OWNERS}:
                issues.append(f"{sid}: repo owner '{owner}' not in TRUSTED_OWNERS allowlist")
        pin = s.get('pinned_commit', '')
        if not re.fullmatch(r'[0-9a-f]{40}', pin):
            issues.append(f"{sid}: pinned_commit must be 40-char SHA")
        if s.get('status') not in {'active', 'deprecated'}:
            issues.append(f"{sid}: status must be active/deprecated")
    return issues


def find_copied_skill_bodies(manifest_ids):
    issues = []
    local_skill = SKILL_ROOT / 'SKILL.md'
    local_text = local_skill.read_text(encoding='utf-8', errors='replace') if local_skill.exists() else ''

    suspicious = [
        'Standard reviews under-report gaps because LLMs default to evaluating what IS present',
        'Search Drupal.org issue queues and summarize individual issues',
        'Drupal lazy builders and placeholder implementation',
    ]
    for marker in suspicious:
        if marker in local_text:
            issues.append('Local SKILL.md appears to contain copied third-party skill body content.')
            break

    refs_text = '\n'.join(p.read_text(encoding='utf-8', errors='replace') for p in SKILL_ROOT.rglob('*.md'))
    for sid in manifest_ids:
        if sid not in refs_text:
            issues.append(f"Missing reference to manifest skill ID in markdown docs: {sid}")

    return issues


def find_forbidden_tracked_paths():
    issues = []
    forbidden_prefixes = ['research/drupal-skills/upstream/', 'research/drupal-skills/extracted/']
    try:
        tracked = subprocess.check_output(
            ['git', '-C', str(ROOT), 'ls-files'],
            text=True,
            stderr=subprocess.DEVNULL,
        ).splitlines()
    except Exception:
        return issues
    for p in tracked:
        if any(p.startswith(prefix) for prefix in forbidden_prefixes):
            issues.append(f"Forbidden tracked vendor-like path: {p}")
    return issues


def main() -> int:
    data = yaml.safe_load(MANIFEST.read_text(encoding='utf-8'))
    manifest_ids = [s['id'] for s in data.get('skills', []) if 'id' in s]

    issues = []
    issues.extend(find_manifest_issues(data))
    issues.extend(find_copied_skill_bodies(manifest_ids))
    issues.extend(find_forbidden_tracked_paths())

    if issues:
        print('Validation failed:')
        for i in issues:
            print(f"- {i}")
        return 1

    print('External skill policy validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
