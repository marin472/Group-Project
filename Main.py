# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:56:23 2023

@author: sarah
"""

def show_menu():
    print("\n===== Budget Management System =====")
    print("1. Expenses")
    print("2. Savings Goals")
    print("3. Budgets")
    print("4. Exit")


def expenses_menu():
    print("\n===== Expenses Menu =====")
    # Add your expenses-related options here


def savings_goals_menu():
    print("\n===== Savings Goals Menu =====")
    # Add your savings goals-related options here


def budgets_menu():
    print("\n===== Budgets Menu =====")
    # Add your budgets-related options here


def main():
    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            expenses_menu()
        elif choice == "2":
            savings_goals_menu()
        elif choice == "3":
            budgets_menu()
        elif choice == "4":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

import csv
from datetime import datetime

def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        data = []
        for row in reader:
            for key, value in row.items():
                if key == 'Date':
                    row[key] = datetime.strptime(value, '%d/%m/%Y')
                elif key == 'Amount':
                    row[key] = float(value)
                else:
                    row[key] = value
            data.append(row)
        return data

category_data = read_csv_file('categories.csv')
category_dict = {}
for row in category_data:
    category_dict[row['Description']] = row['Category']

transaction_data = read_csv_file('transactions.csv')
transaction_list = []
for row in transaction_data:
    transaction_list.append((row['Date'], row['Description'], row['Amount']))

for i in range(len(transaction_list)):
    category = category_dict.get(transaction_list[i][1], '')
    transaction_list[i] = transaction_list[i] + (category,)

def sort_by_category(x):
    return x[3]

transaction_list.sort(key=sort_by_category)

current_category = ''
for transaction in transaction_list:
    if transaction[3] != current_category:
        print('====={}====='.format(transaction[3]))
        current_category = transaction[3]
    print('{}   {}   {:.2f}'.format(datetime.strftime(transaction[0], '%d/%m/%Y'), transaction[1], transaction[2]))

category_totals = {}
for transaction in transaction_list:
    category_totals[transaction[3]] = category_totals.get(transaction[3], 0) + transaction[2]
    
for category, total in category_totals.items():
    print('{}: {:.2f}'.format(category, total))