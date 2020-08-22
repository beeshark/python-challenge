# PyBank

import os
import csv

#directory ... having trouble with this one showing up with "..", "Resources" etc.
cvspath = "/Users/Sara/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

#store data and variables
total_months = 0
net_profit = 0
changes = 0
avg_changes = 0

#store lists to organize more
dates = []
monthly_changes = []
profits = []

with open(cvspath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)
  row = next(csvreader)

# loops
  for row in csvreader:
    #months
    dates.append(row[0])
    total_months = len(dates) + 1

    # net total of profit/losses
   # profits.append(row[1])
    #net_profit = net_profit + (int(row[1]))

    #month to month changes
    #changes
    #monthly_changes.append(changes)

    #avg of changes
    #changes = net_profits / total_months
    #changes = str(round(changes,2))

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


# the printed stuff looks different from the example given so im not sure if i did this right