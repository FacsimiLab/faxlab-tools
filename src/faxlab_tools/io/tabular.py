__all__ = ["csv_to_dict"]

import csv

def csv_to_dict(path):
  """
  Create a python dictionary from a CSV file
  """
  # Open the CSV file and read its contents
  with open(path, "r") as file:
    reader = csv.reader(file)

    # Create a dictionary to hold the data
    my_dict = {}

    # Loop through each row of the CSV and add its data to the dictionary
    for row in reader:
      # print(row) #Uncomment this row for debugging
      key = row[0]
      value = row[1]
      my_dict[key] = value

    return my_dict

def h5_to_melted_df(h5_path, verbosity=False):
  """
  Reads an HDF5 file, adds a column with the key name to each DataFrame, and concatenates all DataFrames into one.
  """
  import pandas as pd
  import h5py
  from rich import print
  from tqdm.notebook import tqdm  # noqa

  dfs = []
  with h5py.File(h5_path, "r") as h5file:
    keys = list(h5file.keys())

  pbar = tqdm(keys, desc="Processing HDF5 keys")
  for key in pbar:
    pbar.set_description(f"Processing {key}")
    df = pd.read_hdf(h5_path, key=key)
    df.insert(0, "key", key)
    dfs.append(df)
  melted_df = pd.concat(dfs, ignore_index=True)
  # Convert the 'key' column to categorical type after creating the melted DataFrame
  melted_df["key"] = melted_df["key"].astype("category")
  if verbosity:
    print(f"Melted DataFrame shape: {melted_df.shape}")
    print(melted_df.info())
  return melted_df
