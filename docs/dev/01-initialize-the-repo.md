# Initialization of the repository

## Setup UV
```bash
# Initialize a uv project
uv init --lib --package \
    --no-pin-python \
    --no-workspace \
    --managed-python \
    --build-backend hatch
```

```bash
# Initialize the python venv
uv venv --python 3.10 --project .
```
Edit the `pyproject.toml` file to include the following:

```toml
[project]
name = "faxlab-tools"
version = "0.1.0"
description = "A python library of tools useful for reproducible research, built upon the FacsimiLab philosophy."
readme = "README.md"
authors = [
    { name = "Pranav Kumar Mishra", email = "62562712+pranavmishra90@users.noreply.github.com" }
]
requires-python = ">=3.10"
dependencies = []

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.hatch.build.targets.wheel]
packages = ["src/faxlab-tools"]

```

```bash
# Add development dependencies
uv add --dev \
      python-semantic-release \
      pre-commit \
      ruff \
      datalad
```

## Initialize pre-commit

```bash
# Initialize pre-commit
pre-commit install
```
