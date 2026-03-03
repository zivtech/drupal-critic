#!/usr/bin/env python3
import csv
import hashlib
import json
import os
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

BASE = Path('/Users/AlexUA/drupal-critic/research/drupal-skills')
RAW = BASE / 'raw'
UP = BASE / 'upstream'
EXT = BASE / 'extracted'
REP = BASE / 'reports'

API_JSON = RAW / 'skills-search-drupal.json'

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.S)
NAME_RE = re.compile(r"^name:\s*(.+?)\s*$", re.M)
DESC_RE = re.compile(r"^description:\s*(.+?)\s*$", re.M)


def safe_id(s: str) -> str:
    return s.replace('/', '__')


def parse_skill_md(path: Path) -> Tuple[Optional[str], Optional[str], str]:
    text = path.read_text(encoding='utf-8', errors='replace')
    name = None
    desc = None
    m = FRONTMATTER_RE.search(text)
    if m:
        fm = m.group(1)
        nm = NAME_RE.search(fm)
        dm = DESC_RE.search(fm)
        if nm:
            name = nm.group(1).strip().strip('"\'')
        if dm:
            desc = dm.group(1).strip().strip('"\'')
    return name, desc, text


def extract_summary(text: str, desc: Optional[str]) -> str:
    if desc and desc.strip() not in {'>', '>-', '|', '|-'}:
        return ' '.join(desc.strip().split())
    body = FRONTMATTER_RE.sub('', text, count=1)
    for raw in body.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.startswith('#') or line.startswith('```') or line.startswith('<'):
            continue
        if line.startswith('- ') or line.startswith('* ') or re.match(r'^\\d+\\.\\s', line):
            continue
        return ' '.join(line.split())
    return ''


@dataclass
class Candidate:
    source: str
    repo_dir: Path
    repo_sha: str
    skill_md: Path
    rel: str
    folder_name: str
    frontmatter_name: Optional[str]
    description: Optional[str]


def repo_sha(repo_dir: Path) -> str:
    head = repo_dir / '.git' / 'HEAD'
    if not head.exists():
        return ''
    # repo is shallow clone, HEAD commit is enough provenance
    import subprocess
    try:
        out = subprocess.check_output(['git', '-C', str(repo_dir), 'rev-parse', 'HEAD'], text=True).strip()
        return out
    except Exception:
        return ''


def collect_candidates(sources: List[str]) -> Dict[str, List[Candidate]]:
    out: Dict[str, List[Candidate]] = {}
    for source in sources:
        repo_dir = UP / safe_id(source)
        sha = repo_sha(repo_dir)
        cands: List[Candidate] = []
        if repo_dir.exists():
            for p in repo_dir.rglob('SKILL.md'):
                if not p.is_file():
                    continue
                rel = str(p.relative_to(repo_dir))
                folder = p.parent.name
                name, desc, _ = parse_skill_md(p)
                cands.append(Candidate(
                    source=source,
                    repo_dir=repo_dir,
                    repo_sha=sha,
                    skill_md=p,
                    rel=rel,
                    folder_name=folder,
                    frontmatter_name=name,
                    description=desc,
                ))
        out[source] = cands
    return out


def choose_candidate(skill_id: str, candidates: List[Candidate]) -> Tuple[Optional[Candidate], str]:
    exact_name = [c for c in candidates if c.frontmatter_name == skill_id]
    if exact_name:
        exact_name.sort(key=lambda c: (len(c.rel), c.rel))
        return exact_name[0], 'mapped-frontmatter-name'

    exact_folder = [c for c in candidates if c.folder_name == skill_id]
    if exact_folder:
        exact_folder.sort(key=lambda c: (len(c.rel), c.rel))
        return exact_folder[0], 'mapped-folder-name'

    contained = [c for c in candidates if skill_id in c.rel]
    if contained:
        contained.sort(key=lambda c: (len(c.rel), c.rel))
        return contained[0], 'mapped-path-contains-skill-id'

    return None, 'unresolved'


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def write_json(path: Path, obj) -> None:
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def score_dim(text: str, patterns: List[str]) -> int:
    t = text.lower()
    hits = sum(1 for p in patterns if p in t)
    if hits >= 8:
        return 5
    if hits >= 5:
        return 4
    if hits >= 3:
        return 3
    if hits >= 1:
        return 2
    return 1


def analyze_skill(text: str, description: str) -> Tuple[Dict[str, int], List[str], List[str]]:
    trigger = score_dim(text + '\n' + description, ['use when', 'trigger', 'auto-activates', 'invoke when', 'should be used'])
    drupal_depth = score_dim(text, ['drupal', 'drush', 'module', 'entity', 'twig', 'hook', 'ddev', 'composer', 'migration', 'cache'])
    op_safety = score_dim(text, ['security', 'validate', 'access', 'rollback', 'snapshot', 'error handling', 'permissions', 'xss', 'sql injection'])
    review_use = score_dim(text, ['review', 'checklist', 'severity', 'findings', 'evidence', 'audit', 'verify'])
    tooling = score_dim(text, ['drush', 'ddev', 'composer', 'phpunit', 'curl', 'api', 'git', 'docker'])
    maintain = score_dim(text, ['step', 'workflow', 'example', 'reference', 'script', 'resources'])

    dims = {
        'trigger_precision': trigger,
        'drupal_depth': drupal_depth,
        'operational_safety': op_safety,
        'review_usefulness': review_use,
        'tooling_realism': tooling,
        'maintainability_signal': maintain,
    }

    strengths: List[str] = []
    weaknesses: List[str] = []

    if trigger >= 4:
        strengths.append('Trigger conditions are explicit and likely to activate at the right time.')
    else:
        weaknesses.append('Trigger guidance is broad or implicit, which can cause under/over-triggering.')

    if drupal_depth >= 4:
        strengths.append('Strong Drupal-specific coverage with concrete platform concepts and terminology.')
    else:
        weaknesses.append('Limited Drupal depth; guidance may be too generic for complex Drupal work.')

    if op_safety >= 4:
        strengths.append('Includes operational/safety guardrails (security, validation, rollback, or access controls).')
    else:
        weaknesses.append('Operational and failure-mode coverage is thin for risky changes.')

    if review_use >= 4:
        strengths.append('Useful for rigorous review workflows (checklists/evidence/audit framing).')
    else:
        weaknesses.append('Weak review rigor; mostly procedural guidance without deep critique structure.')

    if tooling >= 4:
        strengths.append('Tooling guidance is concrete and executable in real Drupal environments.')
    else:
        weaknesses.append('Tooling instructions are sparse or not specific enough for repeatable execution.')

    if maintain >= 4:
        strengths.append('Good structure for long-term maintainability (steps/examples/references/scripts).')
    else:
        weaknesses.append('Maintainer signal is weak; fewer structured steps/examples/resources.')

    return dims, strengths[:3], weaknesses[:3]


def main() -> None:
    data = json.loads(API_JSON.read_text(encoding='utf-8'))
    skills = data.get('skills', [])

    sources = sorted(set(s['source'] for s in skills))
    candidates_by_source = collect_candidates(sources)

    records = []
    unresolved = []

    for s in skills:
        skill_id = s['skillId']
        source = s['source']
        candidates = candidates_by_source.get(source, [])
        selected, status = choose_candidate(skill_id, candidates)

        rec = {
            'id': s['id'],
            'source': source,
            'skill_id': skill_id,
            'skill_name': s['name'],
            'installs': s['installs'],
            'skills_url': f"https://skills.sh/{s['id']}",
            'github_repo_url': f"https://github.com/{source}",
            'mapped_skill_md_path': '',
            'mapped_skill_folder': '',
            'repo_sha': '',
            'mapping_status': status,
            'description': '',
            'content_sha256': '',
            'canonical_id': '',
            'alias_of': '',
        }

        if selected:
            _, desc, text = parse_skill_md(selected.skill_md)
            rec['mapped_skill_md_path'] = str(selected.skill_md)
            rec['mapped_skill_folder'] = str(selected.skill_md.parent)
            rec['repo_sha'] = selected.repo_sha
            rec['description'] = extract_summary(text, desc)
            rec['content_sha256'] = sha256_text(text)
        else:
            unresolved.append(rec['id'])

        records.append(rec)

    # canonical grouping by sha
    by_sha: Dict[str, List[dict]] = {}
    for r in records:
        if r['content_sha256']:
            by_sha.setdefault(r['content_sha256'], []).append(r)

    canonical_map = {}
    for sha, group in by_sha.items():
        group_sorted = sorted(group, key=lambda x: (-int(x['installs']), x['id']))
        canonical = group_sorted[0]['id']
        canonical_map[sha] = canonical
        for r in group:
            r['canonical_id'] = canonical
            if r['id'] != canonical:
                r['alias_of'] = canonical

    # extract canonical bundles + analysis
    canonical_records = [r for r in records if r['canonical_id'] and r['id'] == r['canonical_id']]
    canonical_records.sort(key=lambda x: (-int(x['installs']), x['id']))
    canonical_analysis = []

    for r in canonical_records:
        src_folder = Path(r['mapped_skill_folder'])
        can_slug = safe_id(r['canonical_id'])
        out_dir = EXT / can_slug
        if out_dir.exists():
            shutil.rmtree(out_dir)
        shutil.copytree(src_folder, out_dir)

        skill_md = out_dir / 'SKILL.md'
        name, desc, text = parse_skill_md(skill_md)
        aliases = sorted([x['id'] for x in records if x.get('canonical_id') == r['canonical_id'] and x['id'] != r['canonical_id']])
        dims, strengths, weaknesses = analyze_skill(text, desc or r.get('description', ''))

        provenance = {
            'canonical_id': r['canonical_id'],
            'source': r['source'],
            'repo_sha': r['repo_sha'],
            'original_skill_md_path': r['mapped_skill_md_path'],
            'aliases': aliases,
            'content_sha256': r['content_sha256'],
        }
        write_json(out_dir / 'provenance.json', provenance)

        canonical_analysis.append({
            'canonical_id': r['canonical_id'],
            'skill_name': name or r['skill_id'],
            'description': extract_summary(text, desc or r.get('description', '')),
            'installs': r['installs'],
            'source': r['source'],
            'repo_sha': r['repo_sha'],
            'aliases': aliases,
            'content_sha256': r['content_sha256'],
            'scores': dims,
            'strengths': strengths,
            'weaknesses': weaknesses,
            'path': str(out_dir / 'SKILL.md'),
        })

    # write machine outputs
    write_json(RAW / 'inventory-records.json', records)
    write_json(RAW / 'canonical-analysis.json', canonical_analysis)

    # csv inventory
    csv_fields = [
        'id', 'source', 'skill_id', 'skill_name', 'installs', 'skills_url', 'github_repo_url',
        'mapped_skill_md_path', 'mapped_skill_folder', 'repo_sha', 'mapping_status',
        'content_sha256', 'canonical_id', 'alias_of'
    ]
    with (REP / 'drupal-skills-inventory.csv').open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=csv_fields)
        w.writeheader()
        for r in sorted(records, key=lambda x: (-int(x['installs']), x['id'])):
            w.writerow({k: r.get(k, '') for k in csv_fields})

    # markdown inventory
    inv_lines = []
    inv_lines.append('# Drupal Skills Inventory (skills.sh query: drupal)')
    inv_lines.append(f"- Generated from live API snapshot: `{API_JSON}`")
    inv_lines.append(f"- Query count: **{len(records)}**")
    inv_lines.append(f"- Unique sources: **{len(sources)}**")
    inv_lines.append(f"- Mapped records: **{sum(1 for r in records if r['mapped_skill_md_path'])}**")
    inv_lines.append(f"- Unresolved mappings: **{len(unresolved)}**")
    inv_lines.append('')
    inv_lines.append('| Skill ID | Installs | Source | Mapping | Canonical | Alias Of | What It Does |')
    inv_lines.append('|---|---:|---|---|---|---|---|')
    for r in sorted(records, key=lambda x: (-int(x['installs']), x['id'])):
        what = (r.get('description') or 'n/a').replace('|', '\\|')
        inv_lines.append(
            f"| `{r['id']}` | {r['installs']} | `{r['source']}` | `{r['mapping_status']}` | `{r['canonical_id'] or '-'}` | `{r['alias_of'] or '-'}` | {what} |"
        )
    (REP / 'drupal-skills-inventory.md').write_text('\n'.join(inv_lines) + '\n', encoding='utf-8')

    # what-it-does focused report
    did_lines = []
    did_lines.append('# What Each Drupal Skill Does')
    did_lines.append('')
    did_lines.append('| Skill ID | Canonical | Installs | Summary |')
    did_lines.append('|---|---|---:|---|')
    for r in sorted(records, key=lambda x: (-int(x['installs']), x['id'])):
        summary = (r.get('description') or 'Unavailable (upstream listing present, SKILL.md not found in cloned source).').replace('|', '\\|')
        did_lines.append(f"| `{r['id']}` | `{r['canonical_id'] or '-'}` | {r['installs']} | {summary} |")
    (REP / 'drupal-skills-what-it-does.md').write_text('\n'.join(did_lines) + '\n', encoding='utf-8')

    # canonical analysis md
    can_lines = []
    can_lines.append('# Canonical Drupal Skill Analysis\n')
    can_lines.append(f"- Canonical skills (dedup by SKILL.md hash): **{len(canonical_analysis)}**\n")
    for c in sorted(canonical_analysis, key=lambda x: (-int(x['installs']), x['canonical_id'])):
        can_lines.append(f"## `{c['canonical_id']}`")
        can_lines.append(f"- Source: `{c['source']}` @ `{c['repo_sha'][:12]}`")
        can_lines.append(f"- Path: `{c['path']}`")
        can_lines.append(f"- Description: {c['description'] or 'n/a'}")
        can_lines.append(f"- Aliases: {', '.join('`'+a+'`' for a in c['aliases']) if c['aliases'] else 'none'}")
        sc = c['scores']
        can_lines.append(
            f"- Scores: trigger={sc['trigger_precision']}, drupal-depth={sc['drupal_depth']}, op-safety={sc['operational_safety']}, review={sc['review_usefulness']}, tooling={sc['tooling_realism']}, maintainability={sc['maintainability_signal']}"
        )
        can_lines.append('- Strengths:')
        for s in c['strengths']:
            can_lines.append(f"  - {s}")
        can_lines.append('- Weaknesses:')
        for w in c['weaknesses']:
            can_lines.append(f"  - {w}")
        can_lines.append('')
    (REP / 'drupal-skills-canonical-analysis.md').write_text('\n'.join(can_lines) + '\n', encoding='utf-8')

    # strengths/weaknesses concise report
    sw = []
    sw.append('# Drupal Skills Strengths and Weaknesses\n')
    sw.append('This report compares deduplicated canonical skills and highlights where they are strong vs weak for a Drupal-focused critic workflow.\n')
    sw.append('| Canonical Skill | Primary Focus | Key Strengths | Key Weaknesses |')
    sw.append('|---|---|---|---|')
    for c in sorted(canonical_analysis, key=lambda x: (-int(x['installs']), x['canonical_id'])):
        focus = (c['description'] or '').replace('|', '\\|')
        strengths = '; '.join(c['strengths']).replace('|', '\\|')
        weaknesses = '; '.join(c['weaknesses']).replace('|', '\\|')
        sw.append(f"| `{c['canonical_id']}` | {focus} | {strengths} | {weaknesses} |")
    (REP / 'drupal-skills-strengths-weaknesses.md').write_text('\n'.join(sw) + '\n', encoding='utf-8')

    summary = {
        'query': data.get('query'),
        'count': len(records),
        'unique_sources': len(sources),
        'mapped': sum(1 for r in records if r['mapped_skill_md_path']),
        'unresolved': unresolved,
        'canonical_count': len(canonical_analysis),
        'alias_count': sum(len(c['aliases']) for c in canonical_analysis),
    }
    write_json(REP / 'inventory-summary.json', summary)


if __name__ == '__main__':
    main()
