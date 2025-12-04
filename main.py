#!/bin/env python3

#!> Import libraries
import csv
import pandas as pd
from time import sleep
from pprint import pprint
print("Import Libraries - Done!")


# *** CONSTANTS
CSV_FILE_PATH = "weather.csv" # Path to the input CSV file


def preview_table(data, num_rows=5):
  print(f'\n' * 3)
  pprint(data.head(num_rows))
  print(data.dtypes)


def process_csv(raw_data, headers):
  
  # Format the dates and separate into components
  raw_data["Date.Full"] = pd.to_datetime(raw_data["Date.Full"])
  raw_data["Date.Month"] = raw_data["Date.Full"].dt.month
  raw_data["Date.Day"] = raw_data["Date.Full"].dt.day
  raw_data["Date.Year"] = raw_data["Date.Full"].dt.year
  
  return raw_data


def main():

  # !> Ingest data from CSV 
  raw_data = pd.read_csv(CSV_FILE_PATH)
  headers = raw_data.columns.tolist()
  
  preview_table(raw_data)
  
  # !> Manager different data types
  processed_data = process_csv(raw_data, headers)
  
  preview_table(processed_data)
  
  
  
if __name__ == "__main__":
  main()