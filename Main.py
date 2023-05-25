# -*- coding: utf-8 -*-
"""
Created on Wed May  3 16:56:23 2023

@author: sarah
"""

import csvreader

def show_menu():
    print("\n===== Budget Management System =====")
    print("1. Expenses")
    print("2. Savings Goals")
    print("3. Budgets")
    print("4. Exit")


def expenses_menu():
    print("\n===== Expenses Menu =====")
    # Add your expenses-related options here
    csvreader.read_csv_file("Categories.csv")

def savings_goals_menu():
    print("\n===== Savings Goals Menu =====")
    # Add your savings goals-related options here
    csvreader.read_csv_file("Savings Goal.csv")

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

