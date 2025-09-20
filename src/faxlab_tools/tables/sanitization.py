__all__ = ["find_and_replace_df", "fix_column_dtype"]

import deepcopy
import numpy as np
import pandas as pd

from faxlab_tools.utils import csv_to_dict


# In[ ]: Within a dataframe's column, perform a find and replace
# -----------------------------------------------------------------------
def find_and_replace_df(input_df, column_name, input_sample, replace_sample):
  df = deepcopy(input_df.loc[input_df[column_name] == input_sample])
  df[column_name] = replace_sample

  output_limited2 = input_df

  output_limited2.loc[df.index] = np.nan

  output_limited2 = output_limited2.combine_first(df)

  return output_limited2


# In[ ]: Change dataframe column dtypes according to a python dictionary
# -----------------------------------------------------------------------
# Function to fix the column dtype (updated July 2025)


def fix_column_dtype(df, dtype_dict=None, csv_path=None, dates_only_list=[], datetime_list=[], coerce_numeric=True):
  dtype_dict = csv_to_dict(csv_path)

  error_list = []

  for col in dates_only_list:
    if col in df.columns:
      try:
        df[col] = pd.to_datetime(df[col], format="ISO8601", errors="coerce")
        # print(f"Successfully converted {col} to datetime")
      except ValueError as e:
        print(f"Error converting {col} to datetime: {e}")
        error_list.append(col)

  for col in datetime_list:
    if col in df.columns:
      try:
        df[col] = pd.to_datetime(df[col], format="%H:%M", errors="coerce")
        # print(f"Successfully converted {col} to datetime")
      except ValueError as e:
        print(f"Error converting {col} to datetime: {e}")
        error_list.append(col)

    # List all of the columns in the dataframe
    columns = df.columns.tolist()

    df = df.convert_dtypes(convert_floating=True)

    for col in columns:
      # Debugging -------
      # If you are getting an error loading the dictionary file, uncommon the following print line. The last printed item is the problemmatic one in your dictionary of dtypes
      # print(f"Converting {col} to {dtype_dict[col]}")
      # -----------------
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

    df_adjusted = df.replace(r"-99", "", regex=True)
    df_adjusted = df_adjusted.replace(-99, np.nan, regex=False)

    result_df = pd.concat([df_adjusted], axis=1)

    return result_df
