###Unit 10 group project task

import csv
from datetime import datetime

# define csv reader function
def read_csv(file_path):
    data = []
    with open(file_path, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data

# read category csv into a dictionary
categories_csv = read_csv('categories.csv')
categories = {}
for row in categories_csv:
    categories[row[0]] = row[1]

# read transaction csv into a list of tuples
transactions_csv = read_csv('transactions.csv')
transactions = []
for row in transactions_csv:
    transaction = list(row)
    transaction[1] = datetime.strptime(transaction[1], '%m/%d/%Y')
    transaction[2] = float(transaction[2])
    transaction.append(categories[transaction[3]])
    transactions.append(transaction)

# add a new transaction record with dummy data
new_transaction = ['John Doe', datetime.today(), 25.0, 'Electronics']
new_transaction.append(categories[new_transaction[3]])
transactions.append(new_transaction)

# sort transactions by category in ascending order
transactions.sort(key=lambda x: x[4])

# print transactions grouped by category
category = ''
for transaction in transactions:
    if transaction[4] != category:
        category = transaction[4]
        print('=====' + category + '=====')
    print(transaction[1].strftime('%m/%d/%Y') + ' ' + transaction[0] + ' ' + str(transaction[2]))
    
# calculate total amount for each category
totals = {}
for transaction in transactions:
    if transaction[4] not in totals:
        totals[transaction[4]] = 0.0
    totals[transaction[4]] += transaction[2]

# print total amount for each category
for category, total in totals.items():
    print(category + ' total: ' + str(total))


###Menu for the console interface
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



###Unit 11 group project task
import csv

filename = 'expenses.csv'

# Sample transaction data
transactions = [
    ['2023-05-01', '2023-05-02', '2023-05-03' ],
    ['Groceries', 'Transportation', 'Dinner'],
    ['50.25', '15.50', '35.75']
]

# Function to read expense data from a file
def read_expense_data(filename):
    expenses = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            date = row[0]
            description = row[1]
            amount = float(row[2])
            try:
               amount = (amount)
            except ValueError:
               print(f"Invalid amount value: {amount}. Skipping entry.")
               continue

            expenses.append({'date': date, 'description': description, 'amount': amount})

   
            
    return expenses

# Function to categorize expenses and income
def categorize_transactions(transactions):
    categories = ['2023-05-01', '2023-05-02', '2023-05-03' ],
    ['Groceries', 'Transportation', 'Dinner'],
    ['50.25', '15.50', '35.75']
    categorized_transactions = []
    for transaction in transactions:
        print(f"Transaction: {transaction['description']}")
        for i, category in enumerate(categories):
            print(f"{i+1}. {category}")
        while True:
            try:
                choice = int(input("Select a category (1-4): "))
                if choice < 1 or choice > 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid choice. Try again.")
        transaction['category'] = categories[choice - 1]
        categorized_transactions.append(transaction)
    return categorized_transactions

# Function to generate reports on income and expenses
def generate_reports(transactions):
    total_income = 0
    total_expenses = 0
    print("Transaction Report:")
    print("Date\t\tDescription\t\tAmount\t\tCategory")
    print("-------------------------------------------------")
    for transaction in transactions:
        date = transaction['date']
        description = transaction['description']
        amount = transaction['amount']
        category = transaction['category']
        print(f"{date}\t{description}\t\t{amount}\t\t{category}")
        if amount > 0:
            total_income += amount
        else:
            total_expenses += amount
    print("-------------------------------------------------")
    print(f"Total Income: {total_income}")
    print(f"Total Expenses: {total_expenses}")

# Main program
def main():
    # Read expense data from a file
    filename = 'expenses.csv'
    expenses = read_expense_data(filename)

    # Categorize expenses and income
    categorized_expenses = categorize_transactions(expenses)

    # Generate reports
    generate_reports(categorized_expenses)

# Run the program
if __name__ == '__main__':
    main()
