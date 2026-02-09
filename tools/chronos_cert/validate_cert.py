#!/usr/bin/env python3
import json
import sys
from jsonschema import validate

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def main():
    if len(sys.argv) != 3:
        print("usage: validate_cert.py CERT.json SCHEMA.json")
        sys.exit(1)

    cert_path = sys.argv[1]
    schema_path = sys.argv[2]

    cert = load_json(cert_path)
    schema = load_json(schema_path)

    validate(instance=cert, schema=schema)

    print("PASS schema validation")

if __name__ == "__main__":
    main()
