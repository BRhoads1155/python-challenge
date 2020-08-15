#set dependencies
import os
import csv

#set file path
pypoll_csv = os.path.join("Resources", "election_data.csv")

#create variables 
total_votes = 0
votes_per_candidate = []
candidates = []

#open csv and read in
with open(pypoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    #looping through 
    for row in csvreader:
        #track the total number of votes cast
        total_votes +=1
        #read in the candidate 
        read_candidate = (row[2])
        #if candidate already in list then locate the candidate by index # and increment the vote count by 1
        if read_candidate in candidates:
            candidate_index = candidates.index(read_candidate)
            votes_per_candidate[candidate_index] = votes_per_candidate[candidate_index] + 1
        else:
            #if candidate was not found in candidates list then append to list and add 1 to vote count
            candidates.append(read_candidate)
            votes_per_candidate.append(1)

#print statements
print("Election Results")
print("--------------------------")
print(f"Total Votes: {len(total_votes)}")

output_path = os.path.join("analysis", "analysis.txt")

with open(output_path, 'w') as txt:

    txt.write(f'Election Results')
    txt.write(f'-------------------------------')
    txt.write(f"Total Votes: {total_votes}")
    txt.write(f"Khan: )


