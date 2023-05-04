# -*- coding: utf-8 -*-
"""
Created on Thu May  4 16:11:08 2023

@author: sarah
"""


import csv

def read_csv_file(file_path):
    with open(file_path, r ) as file:
    csv_reader = csv.reader(file)
    
   # Initialize an empty array to store the data
        data = []
        
        # Loop through each row in the CSV file
        for row in reader:
            # Append the row to the data array
            data.append(row)
        
        # Check if any rows were read
        if len(data) > 0:
            # If there is data, return the array
            return data
        else:
            # If there is no data, return None
            return output
        
    

    