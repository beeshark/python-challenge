# PyBank

import os
import csv

#directory ... having trouble with this one showing up with "..", "Resources" etc.
cvspath = "/Users/Sara/Documents/GitHub/python-challenge/PyBank/Resources/budget_data.csv"

#store data and variables
total_months = 0
net_profit = 0
monthly_profits = 0
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
    profit1 = int(row[1])
    monthly_changes = profit1 - monthly_profits

    monthly_changesList.append(monthly_changes)

    avg_changes = avg_changes + monthly_changes
    monthly_profits = profit1

    month_to_month = (avg_changes/total_months)

    #rounding out the decimal if needed 
    month_to_month = str(round(month_to_month,2))

    #some kind of mess
    #
    # greatest increase in profits
    # greatest decrease in profits
    incprof = max(monthly_changesList)
    decprof = min(monthly_changesList)

    incdate = datesList[monthly_changesList.index(incprof)]
    decdate = datesList[monthly_changesList.index(decprof)]


    



# print everything
print("Finanical Analysis")
print("------------------------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${net_profit}")
print(f"Average Change: ${month_to_month}")
print(f"Greatest Increase in Profits: {incdate} ${incprof}")
print(f"Greatest Decrease in Profits: {decdate} ${decprof}")

# export to text file
with open('financial_analysis.txt', 'w') as text:
  text.write("Finanical Analysis\n")
  text.write("------------------------------------------\n")
  text.write(f"Total Months: {total_months}\n")
  text.write(f"Total: ${net_profit}\n")
  text.write(f"Average Change: ${month_to_month}\n")
  text.write(f"Greatest Increase in Profits: {incdate} ${incprof}\n")
  text.write(f"Greatest Decrease in Profits: {decdate} ${decprof}\n")