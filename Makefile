.PHONY: tu-verify

tu-verify:
	@set -euo pipefail; \
	test -z "$$(git status --porcelain)" || (echo "ERROR: dirty working tree"; exit 1); \
	echo "[1/2] lake build"; \
	lake build; \
	echo "[1/2] TU tests"; \
	tools/tu/tests/run_all_tests.sh; \
	git diff --exit-code >/dev/null; \
	test -z "$$(git status --porcelain)" || (echo "ERROR: changes after pass 1"; git status --porcelain; exit 1); \
	echo "[2/2] lake build"; \
	lake build; \
	echo "[2/2] TU tests"; \
	tools/tu/tests/run_all_tests.sh; \
	git diff --exit-code >/dev/null; \
	test -z "$$(git status --porcelain)" || (echo "ERROR: changes after pass 2"; git status --porcelain; exit 1); \
	echo "OK: tu-verify deterministic"
