# PyPoll

# Import necessary modules
import csv
import os

# Files to load and output
file_to_load = os.path.join(".","Resources","election_data.csv") #Input File Path
file_to_output = os.path.join(".","analysis","election_analysis.txt") #Output File Path

# Initialize variables to track the election data
total_vote = 0
Charles_vote_count = 0
Diana_vote_count = 0
Raymon_vote_count = 0
Charles_vote_percentage = 0
Diana_vote_percentage =0
Raymon_vote_percentage = 0

# List to store candidate names
candidates =[]

# Open the CSV file and process it
with open(file_to_load) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csvheaders = next(csvreader) # Skip the header row
    
    # Loop through each row of the dataset and process it
    for x in csvreader:
        total_vote = total_vote + 1 # Calculating total number of votes
        
        if x[2] not in candidates:
            candidates.append(x[2]) # Storing unique candidate names to candidates[]
        
        # Counting and storing number of votes for each candidates
        if x[2] == "Charles Casper Stockham":
            Charles_vote_count = Charles_vote_count + 1
        elif x[2] == "Diana DeGette":
            Diana_vote_count = Diana_vote_count + 1
        elif x[2] == "Raymon Anthony Doane":
            Raymon_vote_count = Raymon_vote_count + 1

    # Looking for the Winner candidate, by comparing the vote share
    if Charles_vote_count > Diana_vote_count:
        if Charles_vote_count > Raymon_vote_count:
            Winner = "Charles Casper Stockham"
    elif Diana_vote_count > Raymon_vote_count:
        winner = "Diana DeGette"
    else:
        winner = "Raymon Anthony Doane"
        
    # Calculating each candidate vote percentage
    Charles_vote_percentage = round((Charles_vote_count/total_vote)*100,3)
    Diana_vote_percentage = round((Diana_vote_count/total_vote)*100,3)
    Raymon_vote_percentage = round((Raymon_vote_count/total_vote)*100,3)
    
# Open a text file to save the output
with open(file_to_output, "w") as txt_file:
     
    # Printing the output to the text file
    txt_file.write("\nElection Results\n\n")
    txt_file.write("-"*40)
    txt_file.write(f"\n\nTotal Votes: {total_vote}\n\n")
    txt_file.write("-"*40)
    txt_file.write(f"\n\nCharles Casper Stockham : {Charles_vote_percentage}% ({Charles_vote_count})\n\n")
    txt_file.write(f"Diana DeGette : {Diana_vote_percentage}% ({Diana_vote_count})\n\n")
    txt_file.write(f"Raymon Anthony Doane : {Raymon_vote_percentage}% ({Raymon_vote_count})\n\n")
    txt_file.write("-"*40)
    txt_file.write(f"\n\nWinner : {winner}\n\n")
    txt_file.write("-"*40)

# Printing to Terminal
    print("\nElection Results")
    print("-"*40)
    print(f"\nTotal Votes: {total_vote}\n")
    print("-"*40)
    print(f"\nCharles Casper Stockham : {Charles_vote_percentage}% ({Charles_vote_count})\n")
    print(f"Diana DeGette : {Diana_vote_percentage}% ({Diana_vote_count})\n")
    print(f"Raymon Anthony Doane : {Raymon_vote_percentage}% ({Raymon_vote_count})\n")
    print("-"*40)
    print(f"\nWinner : {winner}\n")
    print("-"*40)

# Resetting the variables so that the results will be same every time it runs
total_vote = 0
Charles_vote_count = 0
Diana_vote_count = 0
Raymon_vote_count = 0
candidates =[]


