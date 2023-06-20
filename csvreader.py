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
                 
def parse_percentage(percentage_str):
    percentage = percentage_str.strip('%').replace(',', '')
    return float(percentage)

def fix_division_by_zero(value):
    if value == 0:
        return 1
    return value

def fix_input_number(input_str):
    try:
        return float(input_str)
    except ValueError:
        return 0

def get_expenses_per_month(start_date, end_date):
    expenses = 0
    with open('Transactions.csv', 'r', encoding='utf-8-sig') as file:
        reader = csv.DictReader(file, delimiter=';')

        for row in reader:
            try:
                date_str = row['Date'].strip()
            except KeyError:
                try:
                    date_str = row['\ufeffDate'].strip()
                except KeyError:
                    try:
                        date_str = row['ï»¿Date'].strip()
                    except KeyError:
                        print('Error reading your file')
                        continue

            amount = float(row['Amount'])

            date = datetime.strptime(date_str, '%d/%m/%Y').date()

            start_datetime = datetime.combine(start_date, datetime.min.time())
            end_datetime = datetime.combine(end_date, datetime.min.time())

            if start_datetime <= datetime(date.year, date.month, date.day) <= end_datetime:
                expenses += amount

    return expenses
    

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




            
