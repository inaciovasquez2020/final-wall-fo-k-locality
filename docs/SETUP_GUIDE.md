# Setup Guide

This guide is for contributors who want a reliable local environment for Final Wall FO^k Locality.

## Prerequisites

```bash
python3 --version
git --version
```

Recommended baseline:

- Python 3.10 or newer
- Git
- POSIX shell environment

## Clone

```bash
git clone https://github.com/inaciovasquez2020/final-wall-fo-k-locality.git
cd final-wall-fo-k-locality
```

## Optional virtual environment

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install --upgrade pip
```

## Verification

```bash
[ -f scripts/verify_repo.py ] && python3 scripts/verify_repo.py
[ -d tests ] && python3 -m pytest -q
```

## Recommended edit loop

```bash
git pull --ff-only origin main
[ -f scripts/verify_repo.py ] && python3 scripts/verify_repo.py
[ -d tests ] && python3 -m pytest -q
git status --short
```

## Related files

- `QUICKSTART.md`
- `CONTRIBUTING.md`
- `STATUS.md`
- `FREEZE.md`
- `ARCHIVE.md`
