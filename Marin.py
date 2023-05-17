import csv

filename = 'expenses.csv'

# Sample transaction data
transactions = [
    ['2023-05-01', 'Groceries', 50.25],
    ['2023-05-02', 'Transportation', 15.50],
    ['2023-05-03', 'Dinner', 35.75]
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
            amount = (row[2])
            try:
               amount = (amount)
            except ValueError:
               print(f"Invalid amount value: {amount}. Skipping entry.")
               continue

            expenses.append({'date': date, 'description': description, 'amount': amount})

   
            
    return expenses

# Function to categorize expenses and income
def categorize_transactions(transactions):
    categories = ['Housing', 'Transportation', 'Job 1', 'Job 2']
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
