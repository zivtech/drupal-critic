# Audience Activation Matrix

Core audiences are always active:
- Security
- New-hire
- Ops

Additional audiences are context-driven.

## Security
JTBD: When any code path handles user input, defines routes, manages permissions, or renders content, I want to evaluate security as a top priority, so I can catch exploitable vulnerabilities before they reach production.

Always active.

## New-hire
JTBD: When reviewing any code or plan, I want to assess readability and convention adherence from a newcomer's perspective, so I can ensure a junior developer can understand, maintain, and safely modify this code.

Always active.

## Ops
JTBD: When the review touches deployment sequences, infrastructure configuration, error handling, or monitoring, I want to evaluate operational safety, so I can verify rollback paths, logging, and failure modes are production-ready.

Always active.

## Open Source Contributor
JTBD: When custom code overrides, patches, or reimplements contrib/core functionality, I want to evaluate upstream contribution viability, so I can determine whether the fix belongs in the issue queue rather than custom code.

Activate when:
- Contrib/core behavior is overridden in custom code.
- A bugfix targets leveraged third-party Drupal code.
- The change introduces long-term patch maintenance burden.

Must-check prompts:
- Should this become an upstream patch or issue queue contribution?
- Is custom code duplicating behavior that belongs upstream?

## Site Builder (Drupal Admin UI)
JTBD: When changes touch admin UI, content types, views, workflows, permissions, or config entities, I want to evaluate from a site builder's perspective, so I can verify non-developers can manage these features through the Drupal admin interface without developer intervention.

Activate when:
- Changes touch content types, views, display modes, workflows, moderation, permissions, menus, media, or admin config pages.

Must-check prompts:
- Can site builders manage this in UI without developer-only steps?
- Are config dependencies understandable and stable?

## Content Editor/Marketer
JTBD: When changes affect editorial workflow, content authoring UX, content model structure, metadata/SEO fields, or publishing cadence, I want to evaluate from an editor's perspective, so I can verify the changes don't increase editorial friction or break content governance.

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
