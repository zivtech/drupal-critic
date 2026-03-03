# Skill Routing Map

Use this map to decide which specialist Drupal skill(s) to load during review.
Source of truth for IDs/status/pins is [external-skills-manifest.yaml](external-skills-manifest.yaml).

## Core Review Skills
- `madsnorgaard/agent-resources/drupal-expert`
- `madsnorgaard/agent-resources/drupal-security`
- `bethamil/agent-skills/drupal-update`
- `mindrally/skills/drupal-development`

## Open Source Contributor and Issue Queue
- `scottfalconer/drupal-issue-queue/drupal-issue-queue`
- `scottfalconer/drupal-contribute-fix/drupal-contribute-fix`
- `kanopi/cms-cultivator/drupalorg-issue-helper`
- `kanopi/cms-cultivator/drupalorg-contribution-helper`

## Cache and Rendering Focus
- `sparkfabrik/sf-awesome-copilot/drupal-cache-contexts`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-tags`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-maxage`
- `sparkfabrik/sf-awesome-copilot/drupal-dynamic-cache`
- `sparkfabrik/sf-awesome-copilot/drupal-cache-debugging`
- `sparkfabrik/sf-awesome-copilot/drupal-lazy-builders`

## Canvas / Component Ecosystem
- `drupal-canvas/skills/canvas-component-definition`
- `drupal-canvas/skills/canvas-component-metadata`
- `drupal-canvas/skills/canvas-component-utils`
- `drupal-canvas/skills/canvas-data-fetching`
- `drupal-canvas/skills/canvas-styling-conventions`
- `drupal-canvas/skills/canvas-component-composability`
- `drupal-canvas/skills/canvas-component-upload`

## Tooling and Environment
- `grasmash/drupal-claude-skills/drupal-ddev`
- `omedia/drupal-skill/drupal-tooling`
- `madsnorgaard/drupal-agent-resources/ddev-expert`

## Routing Rules
- Default: load one core review skill plus one specialist skill.
- Max loaded external skills per run: 3.
- Avoid overlapping core skills unless scope is explicitly broad.
- If two options overlap, prefer higher `priority` and `active` status from the manifest.
