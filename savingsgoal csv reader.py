# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 16:45:50 2023

@author: sarah
"""
import csv
from datetime import datetime, date

def get_expenses_per_month(start_date, end_date):
    start_date = datetime.combine(start_date, datetime.min.time()).date()
    end_date = datetime.combine(end_date, datetime.min.time()).date()

    total_expenses = 0
    with open('Transactions.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            try:
                date_str = row['Date']
                expense_date = datetime.strptime(date_str, '%d/%m/%Y').date()
                if start_date <= expense_date <= end_date:
                    amount = row['Amount(Euro)']
                    if amount and amount != '':
                        total_expenses += float(amount)
            except KeyError:
                continue
    return total_expenses

def fix_input_number(input_value):
    return float(input_value) if input_value is not None and input_value != '' else 0.0


def calculate_adjusted_months_required(goal, average_monthly_income, expenses_per_month):
    target_amount, current_amount, monthly_saving = goal

    if monthly_saving == 0:
        return float('inf')  # Goal not achievable with current income and expenses
    elif average_monthly_income == 0:
        return -1  # Goal cannot be reached with current income and expenses

    remaining_amount = target_amount - current_amount
    months_required = remaining_amount / monthly_saving

    return months_required


def getSavGoal():
    savings_goal_list = []

    monthly_incomes = []
    with open('income.csv', 'r') as file:
        reader = csv.DictReader(file)

        dates = []
        amounts = []
        for row in reader:
            date_str = row['Date']
            amount = fix_input_number(row['Amount(Euro)'])

            dates.append(date_str)
            amounts.append(amount)

        if len(amounts) <= 1:
            print("Not enough data to calculate monthly income.")
            return

        for i in range(1, len(amounts)):
            date1 = datetime.strptime(dates[i - 1], '%d/%m/%Y')
            date2 = datetime.strptime(dates[i], '%d/%m/%Y')

            months_diff = (date2.year - date1.year) * 12 + (date2.month - date1.month)
            
            if months_diff == 0:
                print("Error: Months difference is zero.")
                continue  # Skip the current iteration and move to the next one

            income_per_month = (amounts[i - 1] - get_expenses_per_month(date1, date2)) / months_diff
            monthly_incomes.append(income_per_month)

    if len(monthly_incomes) == 0:
        print("Not enough data to calculate monthly income.")
        return

   
    average_monthly_income = sum(monthly_incomes) / len(monthly_incomes)

    add_goal = True
    total_percentage = 0
    while add_goal:
        goal_description = input("Enter goal description: ")

        target_amount = fix_input_number(input("Enter target amount (Euro): "))

        current_amount = 0

        percentage_str = ""
        while True:
            if current_amount == 0:
                current_amount = fix_input_number(input("Enter current amount (Euro): "))
            else:
                current_amount = target_amount - fix_input_number(input("Enter remaining amount (Euro): "))

            percentage_str = input("Enter the percentage of your monthly income for this goal: ")
            try:
                percentage = float(percentage_str)
                if total_percentage + percentage <= 100:
                    break
                print("Total percentage exceeds 100. Please enter a percentage within the available range.")
            except ValueError:
                print("Invalid input. Please enter a valid percentage.")

        total_percentage += percentage

        if total_percentage == 100:
            print("You have allocated 100% of your monthly income.")
            choice = input("Do you want to change your goals? (y/n): ")
            if choice.lower() == 'y':
                total_percentage -= percentage
                continue

        if average_monthly_income == 0:
            monthly_saving = 0
        else:
            monthly_saving = average_monthly_income * (percentage / 100)

        goal = (target_amount, current_amount, monthly_saving)
        savings_goal_list.append(goal)

        add_another = input("Do you want to add another goal? (y/n): ")
        if add_another.lower() not in ['y', 'yes']:
            add_goal = False

    expenses_per_month = get_expenses_per_month(datetime.now().date(), datetime.max.date())

    for i, goal in enumerate(savings_goal_list, start=1):
        print('Goal {}:'.format(i))
        print('  Description: {}'.format(goal_description))
        print('  Target Amount: {:.2f} Euro'.format(target_amount))
        print('  Current Amount: {:.2f} Euro'.format(current_amount))
        progress = (current_amount / target_amount) * 100
        print('  Progress: {:.2f}%'.format(progress))

        adjusted_months_required = calculate_adjusted_months_required(goal, average_monthly_income, expenses_per_month)

        if adjusted_months_required == float('inf'):
            print('  Amount to save each month: {:.2f} Euro'.format(monthly_saving))
            print('  Months required to reach the goal: Goal not achievable with current income and expenses')
            print('  Estimated completion date: Not applicable')
        elif adjusted_months_required < 0:
            print('  Amount to save each month: {:.2f} Euro'.format(monthly_saving))
            print('  Months required to reach the goal: Goal cannot be reached with current income and expenses')
            print('  Estimated completion date: Not applicable')
        else:
            adjusted_months_required += expenses_per_month / average_monthly_income
            whole_months = int(adjusted_months_required)
            remaining_days = (adjusted_months_required - whole_months) * 30

            if remaining_days >= 15:
                whole_months += 1

            current_month = datetime.now().month
            target_month = current_month + whole_months
            target_year = datetime.now().year + (target_month // 12)
            target_month = target_month % 12 or 12
            target_date = datetime(target_year, target_month, 1).strftime('%B %Y')

            print('  Amount to save each month: {:.2f} Euro'.format(monthly_saving))
            print('  Months required to reach the goal: {:.1f}'.format(adjusted_months_required))
            print('  Estimated completion date: {}'.format(target_date))

getSavGoal()
























