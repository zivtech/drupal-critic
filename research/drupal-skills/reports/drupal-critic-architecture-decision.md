# Drupal Critic Architecture Decision

## Date
2026-03-03

## Context
We inventoried live `skills.sh` Drupal results and found:
- 42 Drupal-query hits
- 15 source repositories
- 40 directly mappable `SKILL.md` files
- 36 canonical skills after dedup by content hash

Goal: choose how to produce a Drupal-specific version of harsh-critic without creating long-term maintenance drag.

## Options Considered

### Option A: Build a new standalone `drupal-critic` by copying Drupal skill content
Pros:
- One self-contained skill.
- No runtime dependency on external skill availability.

Cons:
- Fastest path to drift and stale guidance.
- Duplicates logic already maintained elsewhere.
- Requires manual sync whenever upstream Drupal skills change.

Decision impact: high maintenance cost, high staleness risk.

### Option B: Keep only `harsh-critic` and tell it to call Drupal skills ad hoc
Pros:
- Minimal new artifact creation.
- Reuses existing harsh-critic protocol.

Cons:
- Routing policy remains implicit and inconsistent.
- No Drupal-specific must-check contract.
- Harder to enforce consistent evidence + Drupal guardrails.

Decision impact: low upfront cost, medium execution inconsistency.

### Option C: Create `drupal-critic` as an orchestration layer (selected)
Pros:
- Keeps harsh-critic rigor while adding explicit Drupal checks.
- Reuses existing Drupal specialist skills instead of copying them.
- Centralizes routing policy and severity calibration.
- Minimizes drift because domain details stay in upstream specialist skills.

Cons:
- Depends on external skill availability for best results.
- Requires clear fallback behavior when specialists are absent.

Decision impact: best balance of rigor, reuse, and maintainability.

## Decision
Select **Option C**.

Implement `drupal-critic` as:
- A strict Drupal-focused review contract.
- A routing map to specialist Drupal skills.
- A fallback rubric that still functions if specialist skills are unavailable.

## Guardrails
- Load at most 2-3 specialist skills per review.
- Require evidence for CRITICAL/MAJOR findings.
- Keep speculative points in an unscored open-questions section.
- Enforce Drupal-specific must-check list every run.

## Follow-Up
- Re-run inventory snapshot periodically to catch new/removed skills.
- Update routing map based on install/popularity and overlap.
