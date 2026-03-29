#!/usr/bin/env python3
import json, sys

def canon(obj) -> str:
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def main():
    data = json.load(sys.stdin)
    sys.stdout.write(canon(data))

if __name__ == "__main__":
    main()
