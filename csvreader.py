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
                 category_dict[row['\ï»¿Description']] = row['Category']
             except:
                 print('error reading your file')
        
     
    transaction_data = read_csv_file('Transactions.csv')
    transaction_list = []
    for row in transaction_data:
         print(row)
         try:
            
            transaction_list.append((row['\ufeffDate'], row['Description'], row['Amount']))
         except:
            try:
                transaction_list.append((row['\ï»¿Date'], row['Description'], row['Amount']))
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
                     print('====={}====='.format(transaction[3]))
                     current_category = transaction[3]
                 print('{}   {}   {:.2f}'.format(datetime.strftime(transaction[0], '%d/%m/%Y'), transaction[1], transaction[2]))
             
    category_totals = {}
    for transaction in transaction_list:
                 category_totals[transaction[3]] = category_totals.get(transaction[3], 0) + transaction[2]
                 
    for category, total in category_totals.items():
                 print('{}: {:.2f}'.format(category, total))
