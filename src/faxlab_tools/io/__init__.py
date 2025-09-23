import importlib
import pkgutil
from typing import TYPE_CHECKING

__all__ = []

# --- Runtime: dynamic import of submodules and their __all__ ---
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__):
  module = importlib.import_module(f"{__name__}.{module_name}")
  globals()[module_name] = module
  __all__.append(module_name)

  if hasattr(module, "__all__"):
    for symbol in module.__all__:
      globals()[symbol] = getattr(module, symbol)
    __all__.extend(module.__all__)

# --- Static analysis: explicit imports so type-checkers see them ---
if TYPE_CHECKING:
  from .sanitization import *  # noqa: F401,F403
  from .slicing import *  # noqa: F401,F403
