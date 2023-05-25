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

