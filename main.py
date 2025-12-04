#!/bin/env python3

#!> Import libraries
import csv
import pandas as pd
from time import sleep
from pprint import pprint
print("Import Libraries - Done!")


# *** CONSTANTS
CSV_FILE_PATH = "weather.csv" # Path to the input CSV file




def process_csv(raw_data, headers):
  
  processed_data = []
  
  for row in raw_data:
    for i in range(len(headers)):
      pass


def main():

  raw_data = pd.read_csv(CSV_FILE_PATH)
  headers = raw_data.columns.tolist()  
  print(headers)
  
  
  #processed_data = process_csv(raw_data, headers)
  
  
  
  
if __name__ == "__main__":
  main()