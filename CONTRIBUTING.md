# Contributing to Final Wall FO^k Locality

This repository is terminal and frozen within its declared scope.

## Contribution classes

### 1. Documentation improvements

- clarify frozen or terminal wording
- improve onboarding text
- improve navigation across status and archive files
- fix broken or ambiguous references

### 2. Verification and archival hardening

- improve repository checks
- tighten documentation consistency
- strengthen archive and status surfaces

### 3. Semantic or scope changes

These require explicit justification.

- changing final-wall statements
- changing frozen or terminal status language
- changing conditional-note scope
- expanding authority claims

## Preferred workflow

```bash
git fetch origin --prune
git switch main
git pull --ff-only origin main
git switch -c your-branch-name
```

Run repository checks before commit:

```bash
[ -f scripts/verify_repo.py ] && python3 scripts/verify_repo.py
[ -d tests ] && python3 -m pytest -q
```

Then commit:

```bash
git add <files>
git commit -m "docs: improve onboarding surface"
git push -u origin your-branch-name
```

## Disallowed without explicit justification

- silent semantic changes
- weakening frozen or terminal language without synchronized status updates
- expanding scope or claim surfaces without updating repository status files
