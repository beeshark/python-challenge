# PyBank

import os
import csv

cvspath = os.path.join("Resurces", "budget_data.csv")
#
with open(cvspath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

#store data and variables
profits = []
net_profits = 0
dates = []
total_months = 0
monthly_changes = []
changes = 0


