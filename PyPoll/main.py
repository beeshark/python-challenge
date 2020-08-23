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
indv_candidate = []
ccount = {}

with open(cvspath, newline="") as csvfile:
  csvreader = csv.reader(csvfile, delimiter=",")
  csv_header = next(csvreader)
  
  for row in csvreader:
    #votes cast
    vote_tally = vote_tally + 1

    #list of candidates who got votes
    indv_candidate = row[2]

    if indv_candidate in candidateList:
        candidateList.append(row[2])


    votesList.append(row[2])
  #for indv_candidate in candidateList:
     # ccount.append(votesList.count(indv_candidate))
     # vote_percent.append(round(votesList.count(indv_candidate)/vote_tally*100,2))


    #percentage of votes each candidate won

    #election winner based on pop vote
#winning_vote_count = max(votesList)
#winner = str(range(indv_candidate[votesList.index(winning_vote_count)], 2))
#string index out of range

    

#print here

print("Election Results")
print("----------------------------")
print(f"Total Votes: {vote_tally}")
#for i in range(len(indv_candidate)):
    #print(f"{indv_candidate[i]}: {vote_percent[i]}% ({ccount[i]})")
    #said list index oout of range. not sure how to fix
print("----------------------------")
#print(f"Winner: {winner}")
print("----------------------------")

#output to text file
with open('election_results.txt', 'w') as text:
  text.write("Election Results\n")
  text.write("----------------------------\n")
  text.write(f"Total Votes: {vote_tally}\n")
#for i in range(len(indv_candidate)):
    #print(f"{indv_candidate[i]}: {vote_percent[i]}% ({ccount[i]})")
  text.write("said list index and string index out of range. not sure how to fix\n")
  text.write("----------------------------\n")
  text.write("Winner:\n")
  text.write("----------------------------\n")
