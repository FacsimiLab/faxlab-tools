__all__ = ["find_and_replace_df", "fix_column_dtype", "df_rename_sample_col_by_json"]

import numpy as np
import pandas as pd

from ..io.tabular import csv_to_dict


def find_and_replace_df(input_df, column_name, input_sample, replace_sample):
  """
  Perform a find and replace operation within a specified column of a pandas DataFrame.

  Args:
    input_df (pd.DataFrame): The input DataFrame.
    column_name (str): The name of the column to perform replacement in.
    input_sample: The value(s) to find and replace.
    replace_sample: The value(s) to replace with.

  Returns:
    pd.DataFrame: A copy of the DataFrame with replacements applied in the specified column.
  """
  output_df = input_df.copy()
  output_df[column_name] = output_df[column_name].replace(input_sample, replace_sample)
  return output_df


def fix_column_dtype(df, dtype_dict=None, csv_path=None, dates_only_list=[], datetime_list=[], coerce_numeric=True):
  """
  Change DataFrame column dtypes according to a Python dictionary or CSV file.

  Args:
    df (pd.DataFrame): The input DataFrame.
    dtype_dict (dict, optional): Dictionary mapping column names to dtypes. If None, loaded from csv_path.
    csv_path (str, optional): Path to CSV file containing dtype mapping. Used if dtype_dict is None.
    dates_only_list (list, optional): List of columns to convert to datetime (ISO8601 format).
    datetime_list (list, optional): List of columns to convert to datetime (HH:MM format).
    coerce_numeric (bool, optional): Whether to coerce numeric columns and handle empty strings as NaN.

  Returns:
    pd.DataFrame: DataFrame with adjusted column dtypes and cleaned values.
  """
  if dtype_dict is None and csv_path is not None:
    dtype_dict = csv_to_dict(csv_path)

  error_list = []

  for col in dates_only_list:
    if col in df.columns:
      try:
        df[col] = pd.to_datetime(df[col], format="ISO8601", errors="coerce")
      except ValueError as e:
        print(f"Error converting {col} to datetime: {e}")
        error_list.append(col)

  for col in datetime_list:
    if col in df.columns:
      try:
        df[col] = pd.to_datetime(df[col], format="%H:%M", errors="coerce")
      except ValueError as e:
        print(f"Error converting {col} to datetime: {e}")
        error_list.append(col)

  # List all of the columns in the dataframe
  columns = df.columns.tolist()

  df = df.convert_dtypes(convert_floating=True)

  for col in columns:
    # Debugging -------
    # If you are getting an error loading the dictionary file, uncomment the following print line.
    # print(f"Converting {col} to {dtype_dict[col]}")
    if col in dtype_dict:
      if coerce_numeric:
        if dtype_dict[col] in ["float", "int", "float64", "int64", "float32", "int32"]:
          df[col] = df[col].replace({"": np.nan})
          df[col] = pd.to_numeric(df[col], errors="coerce")

      try:
        df[col] = df[col].astype(dtype_dict[col])
      except KeyError as ke:
        print(f"KeyError changing dtype: {col} to {dtype_dict[col]}. Error: {ke}")
        error_list.append(col)
      except Exception as e:
        print(f"Error changing dtype: {col} to {dtype_dict[col]}. Error: {e}")
        try:
          df[col] = df[col].fillna(np.nan)
        except Exception as e2:
          print(f"Error changing dtype: {col} to {dtype_dict[col]}. Error: {e2}")
          error_list.append(col)
    else:
      print(f"No dtype specified for column: {col}")
      error_list.append(col)

  df_adjusted = df.replace(r"-99999999", "", regex=True)
  df_adjusted = df_adjusted.replace(-99999999, np.nan, regex=False)

  return df_adjusted


def df_rename_sample_col_by_json(df, samples_json, key_name="short_title"):
  import random  # noqa
  import re  # noqa

  if "logger" in globals():
    global logger
    rprint = logger.debug
  else:
    from rich import print as rprint

  rename_col = {}

  for key in samples_json.keys():
    rename_col[f"S{key}"] = samples_json[key]["short_title"]
    rename_col[f"{key}"] = samples_json[key]["short_title"]

  df_col = df.columns

  # Find and replace substrings in df_col using rename_col

  def replace_substrings(col, replace_dict):
    for search, replace in replace_dict.items():
      col = re.sub(re.escape(search), replace, col)
    return col

  df_col_renamed = [replace_substrings(col, rename_col) for col in df_col]

  df = df.rename(columns=dict(zip(df_col, df_col_renamed)))

  rprint(
    f"df columns renamed. Random set of col to confirm: {', '.join(sorted(random.sample(list(df.columns), 10)))}"
  )

  return df
