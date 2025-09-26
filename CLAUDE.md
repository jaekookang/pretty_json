# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a simple Python command-line tool for prettifying JSON and JSONL files. The main implementation is in `pretty_json.py`.

## Development Environment

- Uses base conda environment
- Python location: `/opt/anaconda3/bin/python`
- Python version: 3.12.7

## Project Structure

- `pretty_json.py` - Main Python script (fully implemented)
- `test/` - Test directory with sample files
- This tool is intended to be used from `~/bin` directory

## Intended Usage

The tool should support:
- `pretty_json test.jsonl` - outputs to terminal
- `pretty_json test.jsonl --output test_out.json` - outputs to file

## Development Notes

- The project is fully implemented and functional
- No symlink needed for the executable as it would conflict with the folder name
- PATH export is configured for ~/bin recursively
- To use as CLI command: rename `pretty_json.py` to `pretty_json` and make executable
- **Actual implementation**: Created symlink with `ln -s ~/bin/pretty_json_cmd/pretty_json.py ~/bin/pretty_json`