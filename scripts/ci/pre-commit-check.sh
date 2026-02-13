#!/bin/bash
# This script is designed to perform the pre-commit checks before a build process is initiated by python-semantic-release (PSR).
# This helps prevent PSR from failing at the end due to pre-commit issues.

set -o pipefail
cd "$(git rev-parse --show-toplevel)"

echo -e "\n\n[CI: scripts/ci/pre-commit-check.sh] \n"
echo -e "\033[34mRunning pre-commit checks...\n\033[0m"

# Run pre-commit checks
pre-commit run --all-files
if [ $? -ne 0 ]; then
    echo -e "\033[0;31mPre-commit checks failed. Please fix the issues above before proceeding.\033[0m"
    exit 1
else
    echo -e "\033[0;32mPre-commit checks passed successfully.\033[0m"
    exit 0
fi
