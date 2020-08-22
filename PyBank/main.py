# PyBank

import os
import csv

#directory ... having trouble with this one showing up with "..", "Resources" etc
cvspath = "/Users/Sara/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

#store data and variables
dates = []
total_months = 1
profits = []
net_profits = 0
monthly_changes = []
changes = 0

with open(cvspath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)
  row = next(csvreader)

# loops
  for row in csvreader:
    #months
    total_months = total_months + 1
    # net total of profit/losses
    net_profits = net_profits +(int(row[1]))
    #avg of changes
    changes = net_profits / total_months
    changes = str(round(changes,2))
    # greatest increase in profits
    
    # greatest decrease in profits
    #



# print everything
print("Finanical Analysis")
print("------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profits}")
print(f"Average Change: ${changes}")
#print(f"Greatest Increase in Profits")
#print(f"Greatest Decrease in Profits")

# export to text file


