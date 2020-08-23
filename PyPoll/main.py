# PyPoll

import os
import csv

#directory ... having trouble with this one showing up with "..", "Resources" etc.
cvspath = "/Users/Sara/Documents/GitHub/python-challenge/PyPoll/Resources/election_data.csv"

# store values and lists
vote_tally = 0
votesList = []
vote_percent = []
candidateList =[]
indv_candidates = []

with open(cvspath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvreader)

for row in csvreader:
    #votes
    vote_tally
