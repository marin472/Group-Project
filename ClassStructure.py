
import csv
from datetime import datetime

 


class User:
    def __init__(self, name, income_sources):
        self.name = name
        self.income_sources = income_sources
        self.savings_goal = 0

 

    def set_savings_goal(self, goal):
        self.savings_goal = goal

 

    def add_income_source(self, source):
        self.income_sources.append(source)

 

    def get_total_income(self):
        total_income = 0
        for source in self.income_sources:
            total_income += source.get_income()
        return total_income

 

    def track_savings_progress(self):
        if self.savings_goal == 0:
            return 0
        savings_progress = (self.get_total_income() / self.savings_goal) * 100
        return savings_progress

 


class IncomeSource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

 

    def get_income(self):
        return self.amount

 


class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

 

    def get_amount(self):
        return self.amount

 


class Budget:
    def __init__(self, user, expenses):
        self.user = user
        self.expenses = expenses

 

    def calculate_total_expenses(self):
        total_expenses = 0
        for expense in self.expenses:
            total_expenses += expense.get_amount()
        return total_expenses

 

    def generate_budget_report(self):
        total_income = self.user.get_total_income()
        total_expenses = self.calculate_total_expenses()
        savings = total_income - total_expenses

 

        report = f"Budget Report\n\nTotal Income: ${total_income}\nTotal Expenses: ${total_expenses}\nSavings: ${savings}"

 

        return report

 


def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        data = []
        for row in reader:
            if 'Amount' in row:
                row['Amount'] = float(row['Amount'])
            data.append(row)
        return data

 

category_data = read_csv_file('categories.csv')
category_dict = {}
for row in category_data:
    category_dict[row['Description']] = row['Category']

 

transaction_data = read_csv_file('transactions.csv')
income_data = read_csv_file('incomes.csv')

 

# Create Expense and IncomeSource objects from transactions and incomes
expenses = []
for row in transaction_data:
    category = category_dict.get(row['Description'], '')
    expenses.append(Expense(row['Description'], row['Amount'], category))

 

income_sources = []
for row in income_data:
    income_sources.append(IncomeSource(row['Description'], row['Amount']))

 

# Create User and Budget objects
user = User("User Name", income_sources)
budget = Budget(user, expenses)

 


def console_interface():
    while True:
        print("\nSelect an option:")
        print("1. View Budget Report")
        print("2. View Savings Progress")
        print("3. Exit")
        user_input = input("\nEnter your choice: ")
        if user_input == "1":
            print(budget.generate_budget_report())
        elif user_input == "2":
            print(f"Savings Progress: {user.track_savings_progress()}%")
        elif user_input.upper() == "3" or user_input.upper() == "EXIT":
            break
        else:
            print("Invalid choice. Please try again.")

 

console_interface()


Merged code:
 
 
 
 import datetime
import csv


def read_input(prompt):
    return input(prompt)


def read_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def set_input_as(prompt, variable_name):
    value = read_input(prompt)
    exec(variable_name + " = '" + value + "'")


def add_one(variable_name):
    exec(variable_name + " += 1")


def define_expense(index):
    expense = {}
    expense["name"] = read_input("Input monthly expense title: ")
    expense["amount"] = read_float_input("Input monthly expense amount: ")
    return expense


def calculate_new_expense_with_inflation(expense, inflation_rate):
    expense["amount"] *= (1 + (inflation_rate / 100))


def calculate_total_income(income):
    total_income = sum(income.values())
    return total_income


def calculate_total_expenses(expenses):
    total_expenses = sum(expense["amount"] for expense in expenses)
    return total_expenses


def calculate_new_income_with_inflation(income, inflation_rate):
    for key in income:
        income[key] *= (1 + (inflation_rate / 100))


def display_expenses(expenses):
    print("List of expenses:")
    for index, expense in enumerate(expenses, 1):
        print(f"{index}. {expense['name']}: ${expense['amount']:.2f}")


def main():
    current_time = datetime.datetime.now()
    set_input_as("Input name: ", "username")
    balance = read_float_input("Input starting money: ")
    income = {}
    income["salary"] = read_float_input("Input monthly income: ")
    goal = {}
    goal["amount"] = read_float_input("Input saving goal: ")
    goal["name"] = read_input("Input a name for the saving goal: ")
    add_one("goal_number")
    goal_number = 1
    while True:
        another_goal = read_input("Set another goal? (Yes/No): ").lower()
        if another_goal == "yes":
            add_one("goal_number")
            goal_number += 1
            set_input_as(f"Input saving goal #{goal_number}: ", f"goal_{goal_number}")
            set_input_as(f"Input a name for the saving goal #{goal_number}: ", f"goal_{goal_number}_name")
        elif another_goal == "no":
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
    expenses = []
    expense_index = 1
    while True:
        expense = define_expense(expense_index)
        expenses.append(expense)
        add_one("expense_index")
        another_expense = read_input("Set another expense? (Yes/No): ").lower()
        if another_expense == "no":
            break
        elif another_expense != "yes":
            print("Invalid input. Please enter 'Yes' or 'No'.")
    inflation_rate = read_float_input("Input inflation rate percentage without sign: ")
    is_universal = read_input("Is the inflation rate universal? (Yes/No): ").lower()
    if is_universal == "no":
        display_expenses(expenses)
        affected_expenses = []
        while True:
            choice = read_input("Choose an expense to be affected by the inflation rate (enter the number): ")
            try:
                choice = int(choice)
                if choice < 1 or choice > len(expenses):
                    print("Invalid input. Please enter a valid expense number.")
                    continue
                affected_expenses.append(expenses[choice - 1])
                another_choice = read_input("Add another expense? (Yes/No): ").lower()
                if another_choice == "no":
                    break
                elif another_choice != "yes":
                    print("Invalid input. Please enter 'Yes' or 'No'.")
            except ValueError:
                print("Invalid input. Please enter a number.")
    else:
        affected_expenses = expenses
    # Add another inflation rate?
    while True:
        another_inflation_rate = read_input("Add another inflation rate? (Yes/No): ").lower()
        if another_inflation_rate == "yes":
            inflation_rate = read_float_input("Input inflation rate percentage without sign: ")
        elif another_inflation_rate == "no":
            break
        else:
            print("Invalid input. Please enter 'Yes' or 'No'.")
    define_monthly_income_and_expenses = True
    while define_monthly_income_and_expenses:
        define_monthly_income_and_expenses = False
        if current_time.month <= 3:
            define_monthly_income_and_expenses = True
            continue
        total_income = calculate_total_income(income)
        for expense in affected_expenses:
            calculate_new_expense_with_inflation(expense, inflation_rate)
        total_expenses = calculate_total_expenses(expenses)
        calculate_new_income_with_inflation(income, inflation_rate)
        current_time = current_time.replace(month=current_time.month+1)
        if current_time.month <= 3:
            define_monthly_income_and_expenses = True
    print("Final Results:")
    print("Username:", username)
    print("Starting Money:", balance)
    print("Monthly Income:", income)
    print("Saving Goal:", goal)
    print("Monthly Expenses:")
    for index, expense in enumerate(expenses, 1):
        print(f"{index}. {expense['name']}: ${expense['amount']:.2f}")
    print("Total Income:", total_income)
    print("Total Expenses:", total_expenses)
    print("New Monthly Income:", income)
    print("New Monthly Rent Expense with Inflation:", affected_expenses)


class User:
    def __init__(self, name, income_sources):
        self.name = name
        self.income_sources = income_sources
        self.savings_goal = 0

    def set_savings_goal(self, goal):
        self.savings_goal = goal

    def add_income_source(self, source):
        self.income_sources.append(source)

    def get_total_income(self):
        total_income = 0
        for source in self.income_sources:
            total_income += source.get_income()
        return total_income

    def track_savings_progress(self):
        if self.savings_goal == 0:
            return 0
        savings_progress = (self.get_total_income() / self.savings_goal) * 100
        return savings_progress


class IncomeSource:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

    def get_income(self):
        return self.amount


class Expense:
    def __init__(self, name, amount, category):
        self.name = name
        self.amount = amount
        self.category = category

    def get_amount(self):
        return self.amount


class Budget:
    def __init__(self, user, expenses):
        self.user = user
        self.expenses = expenses

    def calculate_total_expenses(self):
        total_expenses = 0
        for expense in self.expenses:
            total_expenses += expense.get_amount()
        return total_expenses

    def generate_budget_report(self):
        total_income = self.user.get_total_income()
        total_expenses = self.calculate_total_expenses()
        savings = total_income - total_expenses
        report = f"Budget Report\n\nTotal Income: ${total_income}\nTotal Expenses: ${total_expenses}\nSavings: ${savings}"
        return report


def read_csv_file(file_path):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        next(reader)
        data = []
        for row in reader:
            if 'Amount' in row:
                row['Amount'] = float(row['Amount'])
            data.append(row)
        return data


category_data = read_csv_file('categories.csv')
category_dict = {}
for row in category_data:
    category_dict[row['Description']] = row['Category']


transaction_data = read_csv_file('transactions.csv')
income_data = read_csv_file('incomes.csv')

expenses = []
for row in transaction_data:
    category = category_dict.get(row['Description'], '')
    expenses.append(Expense(row['Description'], row['Amount'], category))

income_sources = []
for row in income_data:
    income_sources.append(IncomeSource(row['Description'], row['Amount']))

user = User("User Name", income_sources)
budget = Budget(user, expenses)


def console_interface():
    while True:
        print("\nSelect an option:")
        print("1. View Budget Report")
        print("2. View Savings Progress")
        print("3. Exit")
        user_input = input("\nEnter your choice: ")
        if user_input == "1":
            print(budget.generate_budget_report())
        elif user_input == "2":
            print(f"Savings Progress: {user.track_savings_progress()}%")
        elif user_input.upper() == "3" or user_input.upper() == "EXIT":
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
    console_interface()

