#set dependencies
import os
import csv

#set file path
pypoll_csv = os.path.join("Resources", "election_data.csv")

#create empty lists 
total_votes = []
Khan = []
Correy = []
Li = []
OTooley = []

#open csv and read in
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
#looping through 
    for row in csvreader:
    #track the total number of votes cast
        total_votes.append(row[0])
    #track each candidate who recieved votes
    for i in range(row[2] == "Khan"):
        Khan.append(len(row[2]))
        print(Khan)
