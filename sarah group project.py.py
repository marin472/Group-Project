# -*- coding: utf-8 -*-
"""
Created on Wed May 17 16:40:40 2023

@author: sarah




"""



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


