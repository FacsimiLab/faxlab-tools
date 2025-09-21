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
