import os 
import csv
budget_csv = os.path.join("Resources", "budget_data.csv")
with open(budget_csv, 'r') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
def print_calculations(bank_data):
    months = int(bank_data[0])
    pl = int(bank_data[1])
    print(months)