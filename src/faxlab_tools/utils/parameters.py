"""
Utility functions for extracting parameter names from a Python configuration file and saving global variable values back to the file.

Functions:
  get_param_names(filepath):
    Parse a Python file and return a list of variable names assigned at the top level.
  save_globals_to_params(param_names, filepath):
    Save the values of global variables (matching param_names) to a Python file as assignments.
"""
import ast

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


