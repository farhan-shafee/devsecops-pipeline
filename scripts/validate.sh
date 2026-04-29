#!/usr/bin/env bash
set -euo pipefail

python -m py_compile src/example_app.py
python -m pytest -q
