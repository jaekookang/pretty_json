#!/usr/bin/env python3

import argparse
import json
import sys
import os

def read_jsonl(file_path):
    """Read JSONL file and return list of JSON objects."""
    objects = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line_num, line in enumerate(f, 1):
            line = line.strip()
            if line:
                try:
                    objects.append(json.loads(line))
                except json.JSONDecodeError as e:
                    print(f"Error parsing JSON on line {line_num}: {e}", file=sys.stderr)
                    sys.exit(1)
    return objects

def read_json(file_path):
    """Read JSON file and return the parsed object."""
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            return json.load(f)
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}", file=sys.stderr)
            sys.exit(1)

def prettify_json(data):
    """Pretty-print JSON data with proper indentation."""
    return json.dumps(data, ensure_ascii=False, indent=2)

def main():
    parser = argparse.ArgumentParser(description='Pretty-print JSON/JSONL files')
    parser.add_argument('input_file', help='Input JSON or JSONL file')
    parser.add_argument('--output', '-o', help='Output file (default: stdout)')

    args = parser.parse_args()

    # Check if input file exists
    if not os.path.exists(args.input_file):
        print(f"Error: File '{args.input_file}' not found", file=sys.stderr)
        sys.exit(1)

    # Determine file type and read accordingly
    if args.input_file.endswith('.jsonl'):
        data = read_jsonl(args.input_file)
    else:
        data = read_json(args.input_file)

    # Pretty-print the data
    pretty_output = prettify_json(data)

    # Output to file or stdout
    if args.output:
        try:
            with open(args.output, 'w', encoding='utf-8') as f:
                f.write(pretty_output)
                f.write('\n')
            print(f"Pretty JSON written to {args.output}")
        except IOError as e:
            print(f"Error writing to file '{args.output}': {e}", file=sys.stderr)
            sys.exit(1)
    else:
        print(pretty_output)

if __name__ == '__main__':
    main()
