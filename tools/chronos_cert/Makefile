PYTHON=python3

CERT_TOY=tools/chronos_cert/examples/toy_uniform_bit_reveal/CERT.json
CERT_XOR=tools/chronos_cert/examples/xor_2bit_reveal/CERT.json
SCHEMA=tools/chronos_cert/cert_schema.json

VERIFY=tools/chronos_cert/chronos_cert_verify.py
VALIDATE=tools/chronos_cert/validate_cert.py

all: schema verify

schema:
	$(PYTHON) $(VALIDATE) $(CERT_TOY) $(SCHEMA)
	$(PYTHON) $(VALIDATE) $(CERT_XOR) $(SCHEMA)

verify:
	$(PYTHON) $(VERIFY) $(CERT_TOY)
	$(PYTHON) $(VERIFY) $(CERT_XOR)

test: schema verify
	@echo all chronos certificate checks passed

