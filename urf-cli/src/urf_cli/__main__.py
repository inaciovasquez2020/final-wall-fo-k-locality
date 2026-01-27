import argparse, json
from pathlib import Path
import jsonschema
from importlib.resources import files

DEFAULT_SCHEMA = files("urf_cli.schema") / "urf-sg-v1.0.schema.json"

def cmd_verify(args):
    cert_path = Path(args.cert).resolve()
    schema_path = Path(args.schema).resolve() if args.schema else DEFAULT_SCHEMA

    cert = json.loads(cert_path.read_text())
    schema = json.loads(schema_path.read_text())

    jsonschema.validate(cert, schema)
    print("VALID")

def main():
    p = argparse.ArgumentParser(prog="urf")
    sub = p.add_subparsers(dest="cmd", required=True)

    v = sub.add_parser("verify")
    v.add_argument("cert")
    v.add_argument("--schema", default=None)
    v.set_defaults(func=cmd_verify)

    args = p.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()

