"""
Parameter Utilities Module
-------------------------
This module provides utility functions for working with Python-based parameter/configuration files.
It supports extracting parameter names, loading parameters into dataclasses or the global workspace,
checking parameter loading status, and saving global variable values back to a parameters file.

Functions:
  get_param_names(filepath):
    Parse a Python file and return a list of variable names assigned at the top level.

  load_parameters_as_dataclass(param_file, dataclass):
    Load parameters from a Python file and instantiate a dataclass with matching fields.

  load_parameters_to_global(param_file, global_dict=None):
    Load parameters from a Python file and set them as variables in the specified global dictionary (default: globals()).

  check_globals_loaded(param_file, global_dict=None):
    Check if each key-value pair in the parameters file is present and matches in the global dictionary.
    Also prints any variables in the global dictionary that are set to None.

  save_globals_to_params(param_names, filepath):
    Save the values of global variables (matching param_names) to a Python file as assignments.
"""
import ast
import runpy
from dataclasses import dataclass

def get_param_names(filepath):
  """
  Parse a Python file and return a list of variable names assigned at the top level.

  Args:
    filepath (str): Path to the Python parameters file.

  Returns:
    List[str]: List of variable names assigned in the file.
  """
  
  with open(filepath) as f:
    tree = ast.parse(f.read())
  return [node.targets[0].id for node in tree.body if isinstance(node, ast.Assign)]

def load_parameters_as_dataclass(param_file: str, dataclass: dataclass) -> dataclass:
  """
  Load parameters from a Python file and instantiate a dataclass with matching fields.

  Args:
      param_file (str): Path to the Python parameters file.
      dataclass (type): The dataclass type to instantiate.

  Returns:
      dataclass: An instance of the dataclass populated with parameter values.
  """
  params = runpy.run_path(param_file)
  params_clean = {k: v for k, v in params.items() if k in dataclass.__annotations__}
  missing = [k for k in dataclass.__annotations__ if k not in params_clean]
  if missing:
    raise ValueError(f"Missing parameters in param_file: {missing}")
  return dataclass(**params_clean)


def load_parameters_to_global(param_file: str, global_dict=None):
  """
  Load parameters from a Python file and set them as variables in the specified global dictionary.

  Args:
      param_file (str): Path to the Python parameters file.
      global_dict (dict, optional): Dictionary to set variables in (default: globals()).
  """
  params = runpy.run_path(param_file)
  if global_dict is None:
    global_dict = globals()
  for k, v in params.items():
    if not k.startswith("__"):
      global_dict[k] = v


def check_globals_loaded(param_file, global_dict=None):
  """
  Check if each key-value pair in the parameters file is present and matches in the global dictionary.
  Also prints any variables in the global dictionary that are set to None.

  Args:
      param_file (str): Path to the Python parameters file.
      global_dict (dict, optional): Dictionary to check (default: globals()).
  """
  from rich import print
  import runpy

  params = runpy.run_path(param_file)
  missing = []
  mismatched = []
  none_vars = []
  if global_dict is None:
    global_dict = globals()

  for k, v in params.items():
    if not k.startswith("__"):
      if k not in global_dict:
        missing.append(k)
      elif global_dict[k] != v:
        mismatched.append((k, global_dict[k], v))

  # Check for variables set to None in global_dict
  # We are 'initializing' variables as None in the notebook before loading parameters
  # While this is not required, it helps prevent linting errors from Ruff
  # We want to see if any of these variables remain None after loading parameters
  for k in global_dict:
    if global_dict[k] is None:
      none_vars.append(k)

  # Print results
  if missing:
    print("Missing variables in globals:", missing)
  if mismatched:
    print("Variables with mismatched values:")
    for k, gval, pval in mismatched:
      print(f"  {k}: globals={gval!r}, params={pval!r}")
  if none_vars:
    print("Variables set to None in globals:", none_vars)
  if not missing and not mismatched and not none_vars:
    print("All parameters loaded correctly into globals. No variables are set to None.")

def save_globals_to_params(param_names, filepath):
  """
  Save the values of global variables (matching param_names) to a Python file as assignments.

  Args:
      param_names (List[str]): List of variable names to save.
      filepath (str): Path to the output Python parameters file.
  """
  with open(filepath, "w") as f:
    for name in param_names:
      value = globals().get(name)
      if value is not None:
        if isinstance(value, str):
          f.write(f'{name} = "{value}"\n')
        else:
          f.write(f"{name} = {repr(value)}\n")