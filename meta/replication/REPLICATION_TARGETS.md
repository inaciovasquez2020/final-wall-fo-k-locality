External replication metric

Trial object
Trial := (repo, ref, platform, command, expected)

Metric
TPR := (1/K) * Σ pass_i

Targets
Linux runners
TPR ≥ 0.90 across GitHub hosted plus at least one independent self-hosted run
Mac runner
TPR ≥ 0.75 including macOS
Runtime
Median wall time ≤ 10 minutes for referee workflow

Required commands for a trial
python3 tools/tu/tu_seymour_verify.py tools/tu/testdata/network_minimal_CERT.json
python3 tools/tv_cert/generate_tv_finite_cert.py 8 /tmp/tv_finite_n8_CERT.json
python3 tools/tv_cert/verify_tv_finite_cert.py /tmp/tv_finite_n8_CERT.json
python3 tools/tv_step_cert/generate_tv_step_cert.py 10 /tmp/tv_step_n10_CERT.json
python3 tools/tv_step_cert/verify_tv_step_cert.py /tmp/tv_step_n10_CERT.json
lake build

Logging format
Append one JSON line per run to meta/replication/TPR_LOG.jsonl
