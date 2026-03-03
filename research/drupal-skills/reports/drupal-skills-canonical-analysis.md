# Canonical Drupal Skill Analysis

- Canonical skills (dedup by SKILL.md hash): **36**

## `madsnorgaard/agent-resources/drupal-expert`
- Source: `madsnorgaard/agent-resources` @ `9cb92d8e129f`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/madsnorgaard__agent-resources__drupal-expert/SKILL.md`
- Description: Drupal 10/11 development expertise. Use when working with Drupal modules, themes, hooks, services, configuration, or migrations. Triggers on mentions of Drupal, Drush, Twig, modules, themes, or Drupal API.
- Aliases: `madsnorgaard/drupal-agent-resources/drupal-expert`
- Scores: trigger=2, drupal-depth=5, op-safety=4, review=3, tooling=4, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Includes operational/safety guardrails (security, validation, rollback, or access controls).
  - Tooling guidance is concrete and executable in real Drupal environments.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `madsnorgaard/agent-resources/drupal-security`
- Source: `madsnorgaard/agent-resources` @ `9cb92d8e129f`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/madsnorgaard__agent-resources__drupal-security/SKILL.md`
- Description: Drupal security expertise. Auto-activates when writing forms, controllers, queries, or handling user input. Prevents XSS, SQL injection, and access bypass vulnerabilities.
- Aliases: `madsnorgaard/drupal-agent-resources/drupal-security`
- Scores: trigger=2, drupal-depth=3, op-safety=4, review=3, tooling=2, maintainability=2
- Strengths:
  - Includes operational/safety guardrails (security, validation, rollback, or access controls).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `mindrally/skills/drupal-development`
- Source: `mindrally/skills` @ `47f47c12e62f`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/mindrally__skills__drupal-development/SKILL.md`
- Description: Expert guidance for Drupal 10 module development with PHP 8+, SOLID principles, and Drupal coding standards
- Aliases: none
- Scores: trigger=1, drupal-depth=3, op-safety=3, review=1, tooling=2, maintainability=2
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `bethamil/agent-skills/drupal-update`
- Source: `bethamil/agent-skills` @ `e7ffea4e0005`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/bethamil__agent-skills__drupal-update/SKILL.md`
- Description: Automate Drupal module updates in DDEV environments with safety snapshots, composer update, drush updb, config export, and changelog generation. Handles security updates, patch versions, minor versions, and major version upgrades with compatibility checking. Use when updating Drupal modules, checking for module updates, running composer update, upgrading dependencies, checking outdated packages, or when user mentions DDEV, drush, composer outdated, or module security updates.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=3, review=4, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Useful for rigorous review workflows (checklists/evidence/audit framing).
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Tooling instructions are sparse or not specific enough for repeatable execution.

## `madsnorgaard/agent-resources/drupal-migration`
- Source: `madsnorgaard/agent-resources` @ `9cb92d8e129f`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/madsnorgaard__agent-resources__drupal-migration/SKILL.md`
- Description: Drupal migration expertise. Use when working with D7-to-D10 migrations, CSV imports, JSON API imports, or custom migration plugins.
- Aliases: `madsnorgaard/drupal-agent-resources/drupal-migration`, `neversight/learn-skills.dev/drupal-migration`
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=1, tooling=3, maintainability=3
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `drupal-canvas/skills/canvas-component-metadata`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-component-metadata/SKILL.md`
- Description: Define valid component.yml metadata for Canvas components, including props,
- Aliases: none
- Scores: trigger=2, drupal-depth=2, op-safety=1, review=1, tooling=1, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `drupal-canvas/skills/canvas-component-definition`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-component-definition/SKILL.md`
- Description: Start here for any React component task to enforce the canonical Canvas
- Aliases: none
- Scores: trigger=2, drupal-depth=2, op-safety=2, review=2, tooling=2, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `drupal-canvas/skills/canvas-component-composability`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-component-composability/SKILL.md`
- Description: Design Canvas-ready React components with slots and decomposition-first
- Aliases: none
- Scores: trigger=2, drupal-depth=1, op-safety=1, review=1, tooling=1, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `drupal-canvas/skills/canvas-component-upload`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-component-upload/SKILL.md`
- Description: Upload validated components to Drupal Canvas and recover from common upload
- Aliases: none
- Scores: trigger=1, drupal-depth=2, op-safety=2, review=2, tooling=2, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `drupal-canvas/skills/canvas-component-utils`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-component-utils/SKILL.md`
- Description: Use utility components to render formatted text and media correctly. Use when
- Aliases: none
- Scores: trigger=2, drupal-depth=2, op-safety=2, review=1, tooling=1, maintainability=2
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `drupal-canvas/skills/canvas-data-fetching`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-data-fetching/SKILL.md`
- Description: Fetch and render Drupal content in Canvas components with JSON:API and SWR
- Aliases: none
- Scores: trigger=2, drupal-depth=3, op-safety=1, review=2, tooling=2, maintainability=4
- Strengths:
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `drupal-canvas/skills/canvas-styling-conventions`
- Source: `drupal-canvas/skills` @ `ed912ea2210b`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/drupal-canvas__skills__canvas-styling-conventions/SKILL.md`
- Description: Style Canvas components with Tailwind CSS 4 theme tokens and approved utility
- Aliases: none
- Scores: trigger=2, drupal-depth=2, op-safety=2, review=1, tooling=1, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `kanopi/cms-cultivator/drupalorg-issue-helper`
- Source: `kanopi/cms-cultivator` @ `f539b9044d91`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/kanopi__cms-cultivator__drupalorg-issue-helper/SKILL.md`
- Description: Quick help with drupal.org issue templates, formatting, contributing patches, and best practices. Invoke when user asks "how do I write a bug report?", "drupal.org issue template", "issue formatting", "I have a patch", "contribute back", "submit my fix", "I fixed a bug in a module", or needs help structuring issue descriptions or contributing code to drupal.org projects.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=3, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `omedia/drupal-skill/drupal-frontend`
- Source: `omedia/drupal-skill` @ `4a19d4ea80f2`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/omedia__drupal-skill__drupal-frontend/SKILL.md`
- Description: Drupal Front End Specialist skill for theme development, Twig templates, and rendering system (Drupal 8-11+). Use when working with Drupal themes, Twig syntax, preprocessing, CSS/JS libraries, or template suggestions.
- Aliases: none
- Scores: trigger=2, drupal-depth=5, op-safety=2, review=2, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `grasmash/drupal-claude-skills/drupal-at-your-fingertips`
- Source: `grasmash/drupal-claude-skills` @ `d5690e0aa1e3`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/grasmash__drupal-claude-skills__drupal-at-your-fingertips/SKILL.md`
- Description: Comprehensive Drupal patterns from "Drupal at Your Fingertips" by Selwyn Polit. Covers 50+ topics including services, hooks, forms, entities, caching, testing, and more.
- Aliases: none
- Scores: trigger=1, drupal-depth=4, op-safety=2, review=1, tooling=3, maintainability=3
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `grasmash/drupal-claude-skills/drupal-config-mgmt`
- Source: `grasmash/drupal-claude-skills` @ `d5690e0aa1e3`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/grasmash__drupal-claude-skills__drupal-config-mgmt/SKILL.md`
- Description: Safe patterns for inspecting and syncing Drupal configuration across environments without accidentally importing changes.
- Aliases: none
- Scores: trigger=1, drupal-depth=3, op-safety=1, review=2, tooling=3, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `grasmash/drupal-claude-skills/drupal-ddev`
- Source: `grasmash/drupal-claude-skills` @ `d5690e0aa1e3`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/grasmash__drupal-claude-skills__drupal-ddev/SKILL.md`
- Description: DDEV local development environment patterns for Drupal, including configuration, commands, database management, debugging tools, and performance optimization.
- Aliases: none
- Scores: trigger=1, drupal-depth=4, op-safety=2, review=2, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `kanopi/cms-cultivator/drupalorg-contribution-helper`
- Source: `kanopi/cms-cultivator` @ `f539b9044d91`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/kanopi__cms-cultivator__drupalorg-contribution-helper/SKILL.md`
- Description: Quick help with drupal.org contribution workflows including git commands, branch naming, issue fork setup, and merge request creation. Invoke when user asks "how do I contribute to drupal.org?", "drupal.org git workflow", "issue fork", "drupal merge request", or needs help with git.drupalcode.org commands.
- Aliases: none
- Scores: trigger=2, drupal-depth=2, op-safety=2, review=2, tooling=3, maintainability=4
- Strengths:
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `sparkfabrik/sf-awesome-copilot/drupal-lazy-builders`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__drupal-lazy-builders/SKILL.md`
- Description: Drupal lazy builders and placeholder implementation. Use when asked about #lazy_builder render array property, TrustedCallbackInterface, auto-placeholdering, BigPipe integration, personalized content caching, or how to make user-specific content cacheable.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=1, tooling=2, maintainability=2
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `factorial-io/skills/drupal-recipe-content`
- Source: `factorial-io/skills` @ `9548fc639992`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/factorial-io__skills__drupal-recipe-content/SKILL.md`
- Description: Create Drupal recipes that import content entities (taxonomy terms, nodes, media, menu links) with multilingual translations. Use this skill whenever the user wants to create a Drupal recipe with default content, import taxonomy terms or other content entities into Drupal via recipes, set up multilingual/translated content in a recipe, or export existing content for use in a recipe. Also trigger when the user mentions "default content in recipes", "recipe with translations", or "content export for recipe".
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=1, review=1, tooling=3, maintainability=3
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `omedia/drupal-skill/drupal-backend`
- Source: `omedia/drupal-skill` @ `4a19d4ea80f2`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/omedia__drupal-skill__drupal-backend/SKILL.md`
- Description: Drupal Back End Specialist skill for custom module development, hooks, APIs, and PHP programming (Drupal 8-11+). Use when building custom modules, implementing hooks, working with entities, forms, plugins, or services.
- Aliases: none
- Scores: trigger=2, drupal-depth=5, op-safety=3, review=2, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `ronaldtebrake/drupal-coding-standards-skill/drupal-coding-standards`
- Source: `ronaldtebrake/drupal-coding-standards-skill` @ `3e91251cf81a`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/ronaldtebrake__drupal-coding-standards-skill__drupal-coding-standards/SKILL.md`
- Description: Review code according to Drupal's official coding standards. Provides AI agents with comprehensive guidelines for PHP, JavaScript, CSS, Twig, YAML, SQL, and markup files in Drupal projects. Uses dynamic context discovery to load only relevant standards based on file type being reviewed.
- Aliases: none
- Scores: trigger=1, drupal-depth=3, op-safety=1, review=2, tooling=2, maintainability=2
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `scottfalconer/drupal-issue-queue/drupal-issue-queue`
- Source: `scottfalconer/drupal-issue-queue` @ `7be7938d85ca`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/scottfalconer__drupal-issue-queue__drupal-issue-queue/SKILL.md`
- Description: Search Drupal.org issue queues and summarize individual issues via the Drupal.org api-d7 endpoints. Use for triage or debugging errors by checking for existing issues before patching, filtering by status/priority/category/version/component/tag, summarizing issue threads, or extracting recent patches/files into JSON or Markdown while respecting Drupal.org API constraints (single-threaded, cached, rate-limited, read-only).
- Aliases: none
- Scores: trigger=1, drupal-depth=2, op-safety=1, review=1, tooling=2, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `sparkfabrik/sf-awesome-copilot/drupal-cache-contexts`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__drupal-cache-contexts/SKILL.md`
- Description: Drupal cache contexts implementation guide. Use when asked about request-based cache variations, user.roles vs user context, URL contexts, language contexts, custom cache contexts, or cache context hierarchy. Helps prevent cache explosion from overly broad contexts.
- Aliases: none
- Scores: trigger=2, drupal-depth=3, op-safety=2, review=1, tooling=2, maintainability=2
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `grasmash/drupal-claude-skills/drupal-contrib-mgmt`
- Source: `grasmash/drupal-claude-skills` @ `d5690e0aa1e3`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/grasmash__drupal-claude-skills__drupal-contrib-mgmt/SKILL.md`
- Description: Comprehensive guide for managing Drupal contributed modules via Composer, including updates, patches, version compatibility, and Drupal 11 upgrades. Use when updating modules or resolving dependency issues.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=3, tooling=4, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Tooling guidance is concrete and executable in real Drupal environments.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `grasmash/drupal-claude-skills/ivangrynenko-cursorrules-drupal`
- Source: `grasmash/drupal-claude-skills` @ `d5690e0aa1e3`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/grasmash__drupal-claude-skills__ivangrynenko-cursorrules-drupal/SKILL.md`
- Description: Drupal development and security patterns from Ivan Grynenko's cursor rules. Covers OWASP Top 10, authentication, access control, injection prevention, cryptography, configuration, database standards, file permissions, and more.
- Aliases: none
- Scores: trigger=1, drupal-depth=2, op-safety=4, review=1, tooling=2, maintainability=3
- Strengths:
  - Includes operational/safety guardrails (security, validation, rollback, or access controls).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `madsnorgaard/drupal-agent-resources/ddev-expert`
- Source: `madsnorgaard/drupal-agent-resources` @ `9cb92d8e129f`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/madsnorgaard__drupal-agent-resources__ddev-expert/SKILL.md`
- Description: DDEV local development expertise. Use when working with DDEV projects, containers, configuration, or troubleshooting DDEV environments.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=3, review=1, tooling=4, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Tooling guidance is concrete and executable in real Drupal environments.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `scottfalconer/drupal-contribute-fix/drupal-contribute-fix`
- Source: `scottfalconer/drupal-contribute-fix` @ `801cee9b6ebe`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/scottfalconer__drupal-contribute-fix__drupal-contribute-fix/SKILL.md`
- Description: **Use this skill for ANY Drupal contrib/core bug - even "local fixes".**
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=3, tooling=4, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Tooling guidance is concrete and executable in real Drupal environments.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `scottfalconer/drupal-intent-testing/drupal-intent-testing`
- Source: `scottfalconer/drupal-intent-testing` @ `f5f3cb166268`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/scottfalconer__drupal-intent-testing__drupal-intent-testing/SKILL.md`
- Description: This skill is for **“does this do what we meant?”** testing — the semi-random, UI-first verification you’d do manually, but with an agent driving a real browser.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=3, review=3, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `madsnorgaard/drupal-agent-resources/docker-local`
- Source: `madsnorgaard/drupal-agent-resources` @ `9cb92d8e129f`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/madsnorgaard__drupal-agent-resources__docker-local/SKILL.md`
- Description: Custom Docker Compose local development patterns. Use when working with Docker-based local environments, container configuration, or troubleshooting Docker setups.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=1, tooling=4, maintainability=2
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Tooling guidance is concrete and executable in real Drupal environments.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `omedia/drupal-skill/drupal-tooling`
- Source: `omedia/drupal-skill` @ `4a19d4ea80f2`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/omedia__drupal-skill__drupal-tooling/SKILL.md`
- Description: Drupal development tooling skill for DDEV local environments and Drush command-line operations (Drupal 8-11+). Use when working with Docker-based development environments, Drush commands, deployment workflows, or site management tasks.
- Aliases: none
- Scores: trigger=2, drupal-depth=5, op-safety=4, review=1, tooling=4, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Includes operational/safety guardrails (security, validation, rollback, or access controls).
  - Tooling guidance is concrete and executable in real Drupal environments.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `sparkfabrik/sf-awesome-copilot/drupal-cache-debugging`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__drupal-cache-debugging/SKILL.md`
- Description: Drupal cache debugging techniques and troubleshooting workflows. Use when asked about X-Drupal-Cache headers interpretation, finding max-age 0 sources, WebProfiler usage, cache hit/miss analysis, stale content debugging, or performance profiling cache-related issues.
- Aliases: none
- Scores: trigger=2, drupal-depth=5, op-safety=3, review=2, tooling=3, maintainability=4
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
  - Good structure for long-term maintainability (steps/examples/references/scripts).
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `sparkfabrik/sf-awesome-copilot/drupal-cache-maxage`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__drupal-cache-maxage/SKILL.md`
- Description: Drupal cache max-age configuration and behavior. Use when asked about time-based cache expiration, Cache::PERMANENT, max-age 0 issues, why Page Cache ignores max-age, or when content appears stale despite time expiration. Critical for understanding caching layer differences.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=2, tooling=3, maintainability=2
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `sparkfabrik/sf-awesome-copilot/drupal-cache-tags`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__drupal-cache-tags/SKILL.md`
- Description: Drupal cache tags implementation guide. Use when asked about cache tag naming conventions, entity tags, list tags, custom tags, tag invalidation strategies, or debugging tag-based cache invalidation issues. Covers node:ID, config:name, entity_list patterns.
- Aliases: none
- Scores: trigger=2, drupal-depth=4, op-safety=2, review=1, tooling=3, maintainability=3
- Strengths:
  - Strong Drupal-specific coverage with concrete platform concepts and terminology.
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Operational and failure-mode coverage is thin for risky changes.
  - Weak review rigor; mostly procedural guidance without deep critique structure.

## `sparkfabrik/sf-awesome-copilot/drupal-dynamic-cache`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__drupal-dynamic-cache/SKILL.md`
- Description: Dynamic Page Cache and BigPipe module behavior in Drupal. Use when asked about authenticated user caching, auto-placeholdering, lazy builders, BigPipe streaming, X-Drupal-Dynamic-Cache header, or why content shows UNCACHEABLE status. Covers interaction between caching layers.
- Aliases: none
- Scores: trigger=2, drupal-depth=3, op-safety=1, review=2, tooling=2, maintainability=2
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

## `sparkfabrik/sf-awesome-copilot/sparkfabrik-drupal-containers`
- Source: `sparkfabrik/sf-awesome-copilot` @ `05c1602a3249`
- Path: `/Users/AlexUA/drupal-critic/research/drupal-skills/extracted/sparkfabrik__sf-awesome-copilot__sparkfabrik-drupal-containers/SKILL.md`
- Description: SparkFabrik Drupal project container context. Use when running commands in local development environment, accessing Drupal from containers, or using fs-cli and make commands.
- Aliases: none
- Scores: trigger=2, drupal-depth=3, op-safety=2, review=1, tooling=3, maintainability=3
- Strengths:
- Weaknesses:
  - Trigger guidance is broad or implicit, which can cause under/over-triggering.
  - Limited Drupal depth; guidance may be too generic for complex Drupal work.
  - Operational and failure-mode coverage is thin for risky changes.

