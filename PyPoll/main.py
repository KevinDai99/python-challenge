### Importing Dependencies 
import os
import csv 

### csvpath location
csvpath = os.path.join("Resources", "election_data.csv")

### Variables for Storage
Candidate = []# This is to store total months
Total_Ballot = [] # This is to store max and min volumes

### opening CSV file
with open(csvpath) as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None) #skip the headers

    for row in reader:
        Candidate.append(row[2])
        Total_Ballot.append(row[0])

### Unique Candidates
Unique_Candidate = set(Candidate)
Unique_Candidate = list(Unique_Candidate)
Unique_Candidate = sorted(Unique_Candidate) # Sort Unique Candidates in list to be called in alphabetical order

### Create Dictionary to Hold Value Count of ballots by politician 

ballot_count = {}

for politician in Candidate:
    if politician in ballot_count:
        ballot_count[politician] += 1
    else:
        ballot_count[politician] = 1

### Sort Dictionary so we know who won
sorted_by_ballot = sorted(ballot_count.items(), key = lambda x: x[1], reverse=True) ### Now that the list is sorted, we can recall the winner by index 

### Calculating Percent of Total and isolating total ballot 
Charles_Percent = round(ballot_count["Charles Casper Stockham"]/len(Total_Ballot) * 100,3)
Diana_Percent = round(ballot_count["Diana DeGette"]/len(Total_Ballot) * 100,3)
Raymon_Percent = round(ballot_count["Raymon Anthony Doane"]/len(Total_Ballot) * 100, 3)

Charles = ballot_count["Charles Casper Stockham"]
Diana = ballot_count["Diana DeGette"]
Raymon = ballot_count["Raymon Anthony Doane"]

### Printing Election Results

print("Election Results")
print("-----------------------------------")
print("Total Votes: " + str(len(Total_Ballot)))
print("-----------------------------------")
print(str(Unique_Candidate[0]) + ": " + str(Charles_Percent) + "% " + "(" + str(Charles) + ")")
print(str(Unique_Candidate[1]) + ": " + str(Diana_Percent) + "% " +  "(" + str(Diana) + ")")
print(str(Unique_Candidate[2]) + ": " + str(Raymon_Percent) + "% " + "(" + str(Raymon) + ")")
print("-----------------------------------")
print("Winner: " + str(sorted_by_ballot[0][0]))


### Export to TXT File
txtlocation = os.path.join("analysis", "analysis.txt")

with open(txtlocation, "a") as txtfile:
    print("Election Results",file=txtfile)
    print("-----------------------------------", file = txtfile)
    print("Total Votes: " + str(len(Total_Ballot)), file = txtfile)
    print("-----------------------------------")
    print(str(Unique_Candidate[0]) + ": " + str(Charles_Percent) + "% " + "(" + str(Charles) + ")", file = txtfile)
    print(str(Unique_Candidate[1]) + ": " + str(Diana_Percent) + "% " + "(" + str(Diana) + ")", file = txtfile)
    print(str(Unique_Candidate[2]) + ": " + str(Raymon_Percent) + "% " + "(" + str(Raymon) + ")", file = txtfile)
    print("-----------------------------------", file = txtfile)
    print("Winner: " + str(sorted_by_ballot[0][0]), file = txtfile)
    print("-----------------------------------", file = txtfile)
    txtfile.close()