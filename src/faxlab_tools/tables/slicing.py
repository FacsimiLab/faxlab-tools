__all__ = ["filter_columns_substring", "drop_columns_regex"]

import re
import pandas as pd

def filter_columns_substring(df: pd.DataFrame, substrings: list) -> list:
  """
  Return all column names containing any of the given substrings.

  Args:
      columns (list of str): List of column names.
      substrings (list of str): List of substrings to search for.

  Returns:
      list of str: Filtered column names containing any substring.
  """
  columns = df.columns.tolist()
  return [col for col in columns if any(sub in col for sub in substrings)]


def drop_columns_regex(df: pd.DataFrame, regex: str, verbosity=False):
  # Make a copy of the df to avoid SettingWithCopyWarning
  df = df.copy()

  # List all of the columns in the df
  columns = df.columns.tolist()

  deleted_columns = []

  for col in columns:
    if re.match(regex, col):  # regex
      deleted_columns.append(col)
      # Check if the column exists before attempting to drop it
      if col in df.columns:
        df = df.drop([col], axis=1)  # If regex matches, then remove the column

  if verbosity:
    print(f"The following columns have been deleted: {deleted_columns}")

  return df
