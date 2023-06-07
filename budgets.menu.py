# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 16:27:04 2023

@author: User
"""

import csv

def budgets_menu():
    print("\n===== Budgets Menu =====")
    
    with open('income.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        total_income = 0
        for row in reader:
            for item in row:
                try:
                    total_income += int(item)
                except ValueError:
                    pass
    
    with open('expenses.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        total_expenses = 0
        for row in reader:
            for item in row:
                try:
                    total_expenses += int(item)
                except ValueError:
                    pass
    
    total_balance = total_income - total_expenses
    print("Your balance = ", total_balance)

budgets_menu()