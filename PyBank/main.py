# PyBank

import os
import csv

#directory ... having trouble with this one showing up with "..", "Resources" etc.
cvspath = "/Users/Sara/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

#store data and variables
total_months = 0
net_profit = 0
monthly_profits = 0
monthly_changes = 0
avg_changes = 0

#store lists to organize more
datesList = []
monthly_changesList = []
profitsList = []

with open(cvspath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvreader)

# loops
  for row in csvreader:
    #
    total_months = total_months + 1
    datesList.append(row[0])

    #
    profitsList.append(row[1])
    net_profit = net_profit + (int(row[1]))

    #month to month changes
    monthly_changesList.append(monthly_changes)

    #monthly_change = this_month's profit - last_month's
    #then average that
    #avg_changes = net_profits / total_months
    #rounding out the decimal if needed = str(round(changes,2))

    #profit losses
    #loss = int(row[1]) - netp

    #some kind of mess
    #llll
    # greatest increase in profits
    # greatest decrease in profits
    



# print everything
print("Finanical Analysis")
print("------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${avg_changes}")
#print(f"Greatest Increase in Profits")
#print(f"Greatest Decrease in Profits")

# export to text file