#!/bin/bash

# Directories

list_of_env=(
    "~/work/facsimilab/universe/tools"
    "~/work/facsimilab/rapids-transcriptomics"
    "~/work/prrx1/scRNA-seq"
)

# Update each environment
for env_dir in "${list_of_env[@]}"; do
    echo "Updating environment in $env_dir"
    cd "$env_dir" || { echo "Directory $env_dir not found! Skipping..."; continue; }

    uv sync

done

echo "Done"
