#!/usr/bin/env python3
import argparse
import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

try:
    import yaml
except Exception as exc:  # pragma: no cover
    raise SystemExit("PyYAML is required. Install with: pip install pyyaml") from exc

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / '.claude/skills/drupal-critic/references/external-skills-manifest.yaml'
REPORT = ROOT / 'research/drupal-skills/reports/external-skills-refresh-report.md'


def get_head_sha(repo_url: str) -> str:
    out = subprocess.check_output(['git', 'ls-remote', repo_url + '.git' if not repo_url.endswith('.git') else repo_url, 'HEAD'], text=True)
    return out.split()[0]


def main() -> int:
    parser = argparse.ArgumentParser(description='Refresh pinned commits in external skills manifest.')
    parser.add_argument('--check', action='store_true', help='Do not write manifest; fail if updates are needed.')
    args = parser.parse_args()

    data = yaml.safe_load(MANIFEST.read_text(encoding='utf-8'))
    skills = data.get('skills', [])

    changed = []
    for s in skills:
        repo = s['repo_url']
        current = s.get('pinned_commit', '')
        latest = get_head_sha(repo)
        if latest != current:
            changed.append((s['id'], current, latest))
            s['pinned_commit'] = latest

    report_lines = [
        '# External Skill Refresh Report',
        '',
        f"Generated: {datetime.now(timezone.utc).isoformat()}",
        '',
        f"Checked skills: {len(skills)}",
        f"Changed pins: {len(changed)}",
        '',
    ]

    if changed:
        report_lines.append('| Skill | Old | New |')
        report_lines.append('|---|---|---|')
        for sid, old, new in changed:
            report_lines.append(f"| `{sid}` | `{old or '-'}` | `{new}` |")
    else:
        report_lines.append('No pin changes detected.')

    REPORT.parent.mkdir(parents=True, exist_ok=True)
    REPORT.write_text('\n'.join(report_lines) + '\n', encoding='utf-8')

    if args.check:
        if changed:
            print(f"Manifest update required for {len(changed)} skills.")
            return 1
        print('Manifest pins are current.')
        return 0

    data['generated_at'] = datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')
    MANIFEST.write_text(yaml.safe_dump(data, sort_keys=False), encoding='utf-8')
    print(f"Updated manifest: {MANIFEST}")
    print(f"Wrote report: {REPORT}")
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
