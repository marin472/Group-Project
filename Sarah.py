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
        # -*- coding: utf-8 -*-
"""
Created on Wed May  3 15:57:03 2023

@author: User
"""

import csv


data = [['John', 25, 'Engineer'], ['Jane', 30, 'Manager'], ['Bob', 40, 'Salesperson']]


with open('output.csv', 'w', newline='') as csvfile:
    
    writer = csv.writer(csvfile)

    
    row = 0
    while True:
        
        if row < len(data):
         
            writer.writerow(data[row])
            
            row += 1
          
        else:            
            break
    

    
