
import os
import csv

## Variables
total_votes = 0
Khan_votes = 0
Correy_votes = 0
Li_votes = 0
Otooley_votes = 0

## Reading File
csvpath = os.path.join("..", "PyPoll", "Resources", "election_data.csv")

with open(csvpath, newline='') as csvfile:

    ## Delimiter
    csvreader = csv.reader(csvfile, delimiter=',')
    
    ## Reading Header
    csv_header = next(csvfile)

    ## Reading Rows After Header
    for row in csvreader:
        
        ## Calculating Number Of Votes
        total_votes += 1
        
        ## Calculating Number Of Votes for each Candidate
        if (row[2] == "Khan"):
            Khan_votes += 1
        elif (row[2] == "Correy"):
            Correy_votes += 1
        elif (row[2] == "Li"):
            Li_votes += 1
        else:
            Otooley_votes += 1
            
    ## Calculatig Percentage Of Votes for Each Candidate
    Kahn_percent = Khan_votes / total_votes
    Correy_percent = Correy_votes / total_votes
    Li_percent = Li_votes / total_votes
    Otooley_percent = Otooley_votes / total_votes
    
    ## Calculating the Winner...
    winner = max(Khan_votes, Correy_votes, Li_votes, Otooley_votes)

    if winner == Khan_votes:
        winner_name = "Khan"
    elif winner == Correy_votes:
        winner_name = "Correy"
    elif winner == Li_votes:
        winner_name = "Li"
    else:
        winner_name = "OTooley" 

## Printing...
print(f"Election Results")
print(f"---------------------------")
print(f"Total Votes: {total_votes}")
print(f"---------------------------")
print(f"Kahn: {Kahn_percent:.3%}({Khan_votes})")
print(f"Correy: {Correy_percent:.3%}({Correy_votes})")
print(f"Li: {Li_percent:.3%}({Li_votes})")
print(f"OTooley: {Otooley_percent:.3%}({Otooley_votes})")
print(f"---------------------------")
print(f"Winner: {winner_name}")
print(f"---------------------------")

## Exporting a text file
output_file = os.path.join("..", "PyPoll", "analysis", "Results.text")

with open(output_file, 'w',) as txtfile:

## Writing Results
    txtfile.write(f"Election Results\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Total Votes: {total_votes}\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Kahn: {Kahn_percent:.3%}({Khan_votes})\n")
    txtfile.write(f"Correy: {Correy_percent:.3%}({Correy_votes})\n")
    txtfile.write(f"Li: {Li_percent:.3%}({Li_votes})\n")
    txtfile.write(f"O'Tooley: {Otooley_percent:.3%}({Otooley_votes})\n")
    txtfile.write(f"---------------------------\n")
    txtfile.write(f"Winner: {winner_name}\n")
    txtfile.write(f"---------------------------\n")