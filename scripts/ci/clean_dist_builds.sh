#!/bin/bash

cd "$(git rev-parse --show-toplevel)"

echo -e "\n\n[CI: scripts/ci/clean_dist_builds.sh] \n"

# Remove existing build artifacts
echo -e "\033[34mRemoving existing build artifacts:\n\033[0m"


# Find the files and store in a variable as a list
mkdir -p ./tmp

found_files=$(find dist/ -type f -not -name '.git*' -not -name '*.md')
if [[ -n "$found_files" ]]; then
  echo "$found_files" > tmp/files_to_remove.txt
else
  echo -e "\033[0;32mNo build artifacts found to remove.\033[0m"
  exit 0
fi

echo -e "\033[31mFiles to be removed: \n\033[0m"
cat tmp/files_to_remove.txt

sleep 5

# Read the file line by line and remove each file
while IFS= read -r file; do
    rm -f "$file"
done < tmp/files_to_remove.txt

rm ./tmp/files_to_remove.txt

echo -e "\033[0;32mBuild artifacts removed successfully.\033[0m"
