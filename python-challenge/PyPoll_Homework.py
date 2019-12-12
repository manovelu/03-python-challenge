import os
import csv

# Path defined
csvpath = os.path.join('','PyPoll\Resources', 'election_data.csv')
with open(csvpath, newline ='') as fh_election_data:
    csvreader =  csv.reader(fh_election_data, delimiter=',')
#Header line read
    csv_header = next(csvreader)
    row_num = 0
    candidates = []
# This section fetches the list of candidates - distinct  names and prints the total votes cast
    for rows in csvreader:
#        print(str(row_num) + " --- " +rows[2])
        row_num = row_num + 1
        if rows[2] not in candidates:
            candidates.append(rows[2])
    print("---------------------------------------")
    print("Election Results")
    print("---------------------------------------")
    print("Total Votes:  " + str(row_num))
    print("---------------------------------------")

# creating the file handler
output_path = os.path.join("", "PyPoll\Resources", "Election_Results.csv")
# Open the file using to write the results
with open(output_path, 'w', newline='') as fh_election_results:

# opening the file to write the results and Initialize csv.writer
    csvwriter = csv.writer(fh_election_results)
    csvwriter.writerow(['---------------------------------------'])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["---------------------------------------"])
    csvwriter.writerow(["Total Votes:  " + str(row_num)])
    csvwriter.writerow(["---------------------------------------"])

# Derives number of candidates
#print(candidates)
#print(len(candidates))
number_of_candiadtes = len(candidates)

# sets vote count =0 for all candidates
vote_count = []
for x in range(0,number_of_candiadtes,1):
    vote_count.append(0)
#    print(vote_count[x])

# counts number of votes for each candidate. repons the file, creating the file handler
with open(csvpath, newline ='') as fh_election_data_2:
    csvreader1 =  csv.reader(fh_election_data_2, delimiter=',')
    for rows1 in csvreader1:
        for y in range (0, number_of_candiadtes,1):
          if rows1[2] == candidates[y]:
            vote_count[y] = vote_count[y] + 1

# prints and appends all candidate names and votes secured
with open(output_path, 'a', newline='') as fh_election_results:
    csvwriter = csv.writer(fh_election_results)
    for z in range(0,number_of_candiadtes,1):
        print(candidates[z] + ":  " + str( "{:1.3f}".format((vote_count[z]/row_num)*100 )) + str("%   (") +str(vote_count[z]) + str(")"))
        csvwriter.writerow([candidates[z] + ":  " + str( "{:10.3f}".format((vote_count[z]/row_num)*100 )) + str("%   (") +str(vote_count[z]) + str(")")])

# identifies the winner
Winner = "None"
Winner_count = 0
for s in range(0,number_of_candiadtes,1):
    if vote_count[s] > Winner_count:
        Winner = candidates[s]
        Winner_count = vote_count[s]

# prints  the winner
print("---------------------------------------")
print("Winner:  " + Winner)
print("---------------------------------------")

# appends the winner
with open(output_path, 'a', newline='') as fh_election_results:
    csvwriter = csv.writer(fh_election_results)
    csvwriter.writerow(["---------------------------------------"])
    csvwriter.writerow(["Winner:  " + Winner])
    csvwriter.writerow(["---------------------------------------"])