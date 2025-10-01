# FacsimiLab Tools (`faxlab-tools`): 

A python package aiding translational research using the FacimiLab philosophy for reproducible research.

[![Continuous Integration](https://github.com/FacsimiLab/faxlab-tools/actions/workflows/ci.yml/badge.svg)](https://github.com/FacsimiLab/faxlab-tools/actions/workflows/ci.yml)

## Using the editable install

To install the package in editable mode for development, run:

```bash
# Enter your python environment:
# For example:
source .venv/bin/activate

# Then install the package in editable mode:
git clone https://github.com/FacsimiLab/faxlab-tools.git
uv pip install -e faxlab-tools
```

**Alpha Version Warning**: this project is in early alpha and will be undergoing significant API changes. While semantic versioning is being used, breaking changes will not incremented as major version changes. Features and functions are being migrated by the author from a personal codebase containing many python functions into a more structured package.


## Development

To set up the development environment, run:
```bash
# Clone the repository
git clone https://github.com/FacsimiLab/faxlab-tools.git
cd faxlab-tools

# Create the virtual environment
uv sync
source .venv/bin/activate

# Install pre-commit hooks
pre-commit install
```

## License

MIT License © 2025 Pranav Kumar Mishra. See [LICENSE.md](./LICENSE.md) for details.
