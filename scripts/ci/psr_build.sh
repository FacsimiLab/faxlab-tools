#!/bin/bash

set -o pipefail


# This script is run by python-semantic-release (PSR) as part of its build process.
echo -e "\n\n[CI: scripts/ci/psr_build.sh] \n"
echo -e "\033[34mStarting PSR build process \n\n \033[0m"

cd "$(git rev-parse --show-toplevel)"

# Run upstream scripts prior to building
bash scripts/ci/pre-commit-check.sh
bash scripts/ci/clean_dist_builds.sh

# The package name is passed as the first argument to this script by PSR (default: faxlab-tools)
PACKAGE_NAME=${1:-faxlab-tools}
NEW_VERSION=${2}

# Update the package version in uv.lock
echo -e "Python semantic release has determined the new version to be: $NEW_VERSION"

echo -e "Updating the uv lock package: $PACKAGE_NAME"
uv lock --upgrade-package "$PACKAGE_NAME"
git add uv.lock

echo -e "Starting `uv build`"

# Build the package
uv build

echo -e "\033[0;32mPSR build process completed successfully.\033[0m"
exit 0
