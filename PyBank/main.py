import os 
import csv
print(os.getcwd())
budget_csv = os.path.join("Resources", "budget_data.csv")
#calculate the total number of months in the dataset
def print_calculations(bank_data):
    #assign values to variables
    months = int(bank_data[0])
    pl = int(bank_data[1])

    print(months)
    print(pl)

#read in the csv file
with open(budget_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    header = next(csvreader)

print(print_calculations)

data_output = os.path.join("analysis", "budget_data.csv")

with open(data_output, "w") as csvfile:
    writer = csv.writer(csvfile)
    
