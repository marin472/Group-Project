import csv
from datetime import datetime

def read_csv_file(file_path, delimiter=';'):
    with open(file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file, delimiter=delimiter)
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

def getExpCat():
    category_data = read_csv_file('Categories.csv')
    category_dict = {}
    for row in category_data:
         print(row)
         try:
             
             category_dict[row['\ufeffDescription']] = row['Category']
         except:
             try:
                 category_dict[row['ï»¿Description']] = row['Category']
             except:
                 print('error reading your file')
        
     
    transaction_data = read_csv_file('Transactions.csv')
    transaction_list = []
    for row in transaction_data:
         print(row)
         try:
            
            transaction_list.append((datetime.strptime(row['\ufeffDate'], '%d/%m/%Y').date(), row['Description'], row['Amount']))
         except:
            try:
                transaction_list.append((datetime.strptime(row['ï»¿Date'], '%d/%m/%Y').date(), row['Description'], row['Amount']))
            except:
                print('error reading your file')
     
    for i in range(len(transaction_list)):
         category = category_dict.get(transaction_list[i][1], '')
         transaction_list[i] = transaction_list[i] + (category,)
    
    def sort_by_category(x):
         return x[3]
     
    transaction_list.sort(key=sort_by_category)
             
    current_category = ''
    for transaction in transaction_list:
                if transaction[3] != current_category:
                     print('\n====={}====='.format(transaction[3]))
                     current_category = transaction[3]
                print('{:<12s} {:<30s} {:>10.2f}'.format(transaction[0].strftime('%d/%m/%Y'), transaction[1], transaction[2]))
                
    category_totals = {}
    for transaction in transaction_list:
                 category_totals[transaction[3]] = category_totals.get(transaction[3], 0) + transaction[2]
    
    print('\nCategory Totals:')
    for category, total in category_totals.items():
                 print('{:<48s} {:.2f}'.format(category, total))
                 
def getSavGoal():
    savings_goal_list = []

    monthly_incomes = []
    with open('income.csv', 'r') as file:
        reader = csv.DictReader(file)

        dates = []
        amounts = []
        for row in reader:
            date_str = row['Date']
            amount = float(row['Amount(Euro)'])

            dates.append(date_str)
            amounts.append(amount)

        if len(amounts) <= 1:
            print("Not enough data to calculate monthly income.")
            return

        for i in range(1, len(amounts)):
            date1 = datetime.strptime(dates[i - 1], '%d/%m/%Y')
            date2 = datetime.strptime(dates[i], '%d/%m/%Y')

            months_diff = (date2.year - date1.year) * 12 + (date2.month - date1.month)
            income_per_month = amounts[i - 1] / months_diff
            monthly_incomes.append(income_per_month)

    if len(monthly_incomes) == 0:
        print("Not enough data to calculate monthly income.")
        return

    average_monthly_income = sum(monthly_incomes) / len(monthly_incomes)

    total_percentage = 0  
    while True:
        goal_description = input("Enter goal description (or 'done' to finish): ")
        if goal_description == 'done':
            break

        target_amount = float(input("Enter target amount (Euro): "))
        current_amount = float(input("Enter current amount (Euro): "))

        
        while True:
            percentage = float(input("Enter the percentage of your monthly income for this goal: "))
            if total_percentage + percentage <= 100:
                break
            print("Total percentage exceeds 100. Please enter a percentage within the available range.")

        total_percentage += percentage

        monthly_saving = average_monthly_income * (percentage / 100)
        savings_goal_list.append((goal_description, target_amount, current_amount, monthly_saving))

    for i, goal in enumerate(savings_goal_list, start=1):
        print('Goal {}:'.format(i))
        print('  Description: {}'.format(goal[0]))
        print('  Target Amount: {:.2f} Euro'.format(goal[1]))
        print('  Current Amount: {:.2f} Euro'.format(goal[2]))
        progress = (goal[2] / goal[1]) * 100
        print('  Progress: {:.2f}%'.format(progress))

        
        months_required = (goal[1] - goal[2]) / goal[3]

        
        months_required = max(months_required, 0)  
        whole_months = int(months_required)
        remaining_days = (months_required - whole_months) * 30  
        if remaining_days >= 15:
            whole_months += 1

        current_month = datetime.now().month
        target_month = current_month + whole_months
        target_year = datetime.now().year + (target_month // 12)
        target_month = target_month % 12 or 12
        target_date = datetime(target_year, target_month, 1).strftime('%B %Y')
        
        
        print('  Amount to save each month: {:.2f} Euro'.format(goal[3]))
        print('  Months required to reach the goal: {:.1f}'.format(months_required))
        print('  Estimated completion date: {}'.format(target_date))
        print()

                 


                 
