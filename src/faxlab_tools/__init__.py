# Expose submodules for dot notation
from . import core
from . import figures
from . import tables
from . import io
from . import utils

# Expose __version__ at the package level
from .__version__ import __version__

__all__ = ["core", "figures", "tables", "transcriptomics", "io", "utils"]
