# Audience Activation Matrix

Core audiences are always active:
- Security
- New-hire
- Ops

Additional audiences are context-driven.

## Open Source Contributor
Activate when:
- Contrib/core behavior is overridden in custom code.
- A bugfix targets leveraged third-party Drupal code.
- The change introduces long-term patch maintenance burden.

Must-check prompts:
- Should this become an upstream patch or issue queue contribution?
- Is custom code duplicating behavior that belongs upstream?

## Site Builder (Drupal Admin UI)
Activate when:
- Changes touch content types, views, display modes, workflows, moderation, permissions, menus, media, or admin config pages.

Must-check prompts:
- Can site builders manage this in UI without developer-only steps?
- Are config dependencies understandable and stable?

## Content Editor/Marketer
Activate when:
- Changes affect editorial workflow, content authoring UX, content model, metadata/SEO, campaign pages, or publishing cadence.

Must-check prompts:
- Does this increase editorial friction?
- Are metadata/SEO and governance needs covered?

## Output Convention
When active, include one line per audience in `Multi-Perspective Notes`:
- `- Open-source contributor: ...`
- `- Site-builder: ...`
- `- Content editor/marketer: ...`
