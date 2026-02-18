import json
import sys

if len(sys.argv) != 2:
    print("Usage: python json2txt.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, "r") as f:
    data = json.load(f)

for key, value in data.items():
    print(f"{key}: {value}")
