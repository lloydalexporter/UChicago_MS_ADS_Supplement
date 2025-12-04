#!/bin/env python3

#!> Import libraries
import csv
from time import sleep
from pprint import pprint
print("Import Libraries - Done!")


# *** CONSTANTS
CSV_FILE_PATH = "people-2000000.csv"  # https://github.com/datablist/sample-csv-files
CSV_FILE_PATH = "people-100.csv"      # https://github.com/datablist/sample-csv-files




def process_csv(raw_data, headers):
  
  processed_data = []
  
  for row in raw_data:
    for i in range(len(headers)):
      

def read_csv():  
  
  with open(CSV_FILE_PATH, newline='', encoding='utf-8') as csvfile:
    raw_data = list(csv.reader(csvfile))
  
  return raw_data




def main():

  raw_data = read_csv()
  headers = raw_data.pop(0)
  
  processed_data = process_csv(raw_data, headers)
  
  
  
  
if __name__ == "__main__":
  main()