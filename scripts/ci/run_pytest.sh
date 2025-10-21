#!/bin/bash
# This script runs pytest

set -o pipefail
cd "$(git rev-parse --show-toplevel)"

echo -e "\n\n[CI: scripts/ci/run_pytest.sh] \n\n"
echo -e "\033[34mRunning pytest...\n\033[0m"

# Activate the virtual environment if pytest is not found, creating a venv if necessary
if ! command -v pytest &> /dev/null
then
  source .venv/bin/activate || uv sync && source .venv/bin/activate
fi

# Run pytest with detailed output
# -v: verbose, -s: show print statements
pytest -v -s

exit 0
