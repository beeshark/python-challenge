# PyBank

import os
import csv

#directory ... having trouble with this one showing up with "..", "Resources" etc
cvspath = "/Users/Sara/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

#store data and variables
dates = []
total_months = 0
profits = []
net_profits = 0
monthly_changes = []
changes = 0

with open(cvspath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvfile)
  first_row = next(csvreader)


# month stuff
  for row in csvreader:
    total_months = total_months + 1
    
# net total of profit/losses
net_profits = net_profits +(int(row[1]))

# avg of the changes


# greatest increase in profits

# greatest decrease in profits


# print everything
print("Finanical Analysis")
print("------------------------------------------")
#print(f"Total Months: {}")
#print(f"Total: ${}")
#print(f"Average Change: ${}")
#print(f"Greatest Increase in Profits")
#print(f"Greatest Decrease in Profits")

# export to text file


