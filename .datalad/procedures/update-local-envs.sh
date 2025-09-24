#!/bin/bash

# Directories

export VIRTUAL_ENV=

list_of_env=(
    "/home/pranav/work/facsimilab/universe/tools"
    "/home/pranav/work/facsimilab/rapids-transcriptomics"
    "/home/pranav/work/prrx1/scRNA-seq"
)

# Update each environment
for env_dir in "${list_of_env[@]}"; do
    echo "Updating environment in $env_dir"
    cd "$env_dir" || { echo "Directory $env_dir not found! Skipping..."; continue; }

    echo $(pwd)
    uv sync

done

echo "Done"
