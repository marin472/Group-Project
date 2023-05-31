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
    savings_goal_data = read_csv_file('Savings Goal.csv', delimiter=',')
    savings_goal_list = []
    
    for row in savings_goal_data:
        print(row)
        goal_name = row['Goal description']
        target_amount = float(row['Target Amount(Euro)'].replace(',', ''))
        current_amount = float(row['Current Amount(Euro)'].replace(',', ''))
        savings_goal_list.append((goal_name, target_amount, current_amount))
       
    for i, goal in enumerate(savings_goal_list, start=1):
        print('Goal {}:'.format(i))
        print('  Name: {}'.format(goal[0]))
        print('  Target Amount: {:.2f} Euro'.format(goal[1]))
        print('  Current Amount: {:.2f} Euro'.format(goal[2]))
        progress = (goal[2] / goal[1]) * 100
        print('  Progress: {:.2f}%'.format(progress))
        print()
     
getExpCat()          
getSavGoal()
                 
