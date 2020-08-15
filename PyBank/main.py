#declare dependencies
import os 
import csv

#declare we are loading budget_csv
budget_csv = os.path.join("Resources", "budget_data.csv")

#set variable lists to where data is going to go
total_months = []
total_profit_loss = []
monthly_profit_change = []

#open csv and read in
with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#loop through the rows in reader
    for row in csvreader:

    #track the total months
        total_months.append(row[0])

    #track the total net change
        total_profit_loss.append(int(row[1]))
        
    #loop through profits/losses and add the difference between two months to the monthly profit change list
    for i in range(len(total_profit_loss)-1):
        monthly_profit_change.append(total_profit_loss[i+1]-total_profit_loss[i])

#calculate the min and max of monthly profit change
max_increase = max(monthly_profit_change)
max_decrease = min(monthly_profit_change)

#index max and min to their respective month 
max_monthly_increase = monthly_profit_change.index(max(monthly_profit_change)) + 1
max_monthly_decrease = monthly_profit_change.index(min(monthly_profit_change)) + 1

#print statements
print("Financial Analysis")
print("--------------------------")
print(f"Total Months: {len(total_months)}")
print(f"Total: ${sum(total_profit_loss)}")
print(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
print(f"Greatest Increase in Profits: {total_months[max_monthly_increase]} (${(str(max_increase))})")
print(f"Greatest Decrease in Profits: {total_months[max_monthly_decrease]} (${(str(max_decrease))})")

#set path to where analysis will be
output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as txt:
    txt.write(f'Financial Analysis\n')
    txt.write(f"----------------------------------------------\n")
    txt.write(f"Total Months: {len(total_months)}\n")
    txt.write(f"Total: ${sum(total_profit_loss)}\n")
    txt.write(f"Average Change: ${round(sum(monthly_profit_change)/len(monthly_profit_change),2)}\n")
    txt.write(f"Greatest Increase in Profits: (${(str(max_increase))})\n")
    txt.write(f"Greatest Decrease in Profits: (${(str(max_decrease))})\n")
