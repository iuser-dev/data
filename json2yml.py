#!/usr/bin/env python3

import sys, yaml, json

print(yaml.dump(json.loads(sys.stdin.read()), allow_unicode=True))
