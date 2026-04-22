# Final Wall FO^k Locality Quickstart

This is the shortest path from clone to a first successful local repository check.

## Requirements

- `git`
- `bash`
- `python3`

## 1. Clone

```bash
git clone https://github.com/inaciovasquez2020/final-wall-fo-k-locality.git
cd final-wall-fo-k-locality
```

## 2. Check tools

```bash
python3 --version
git --version
```

## 3. Run repository checks

```bash
[ -f scripts/verify_repo.py ] && python3 scripts/verify_repo.py
[ -d tests ] && python3 -m pytest -q
```

## 4. Review the main frozen surfaces

- `README.md`
- `STATUS.md`
- `FREEZE.md`
- `ARCHIVE.md`
- `notes/INFUSED_CONDITIONAL_SOLUTION_2026_04.md`

## 5. Next steps

- detailed setup: `docs/SETUP_GUIDE.md`
- contribution policy: `CONTRIBUTING.md`
