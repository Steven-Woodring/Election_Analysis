"""
1) Get the voting data
2) Count the total number of votes cast
3) Create a complete list of candidates who received votes
4) Count the total number of votes each candidate won
5) Calculate the percentage of votes each candidate won
6) Determine the winner of the election based on popular vote
"""

# Add our dependencies.
# Import file using direct path
import csv
# Import file using indirect path
import os

# View all functions/methods in the module.
# print(dir(csv))
# print(dir(os))

# Assign a variable for the file to load and the path.
# file_to_load = 'Resources/election_results.csv'
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
# file_to_save = 'analysis/election_analysis.txt'
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# Initialize list of candidate options.
candidate_options = []

# Initialize empty dictionary to store candidates and their votes.
candidate_votes = {}

# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        
        # Add to the total vote count.
        total_votes += 1

        # Get the candidate name.
        candidate_name = row[2]

        # If this is a new candidate name...
        if candidate_name not in candidate_options:
            
            # Add the candidate name to the list of candidates.
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count in the dictionary.
            candidate_votes[candidate_name] = 0
        
        # Add a vote to the candidate's count.
        candidate_votes[candidate_name] += 1

    # Save the results to our text file.
    with open(file_to_save, "w") as txt_file:

        election_results = (
            f"\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes:,}\n"
            f"-------------------------\n")
        print(election_results, end = "")
        # Save the final vote count to the text file.
        txt_file.write(election_results)

        # Iterate through the candidate dictionary.
        for candidate_name in candidate_votes:

            # Retrieve vote count for the candidate.
            votes = candidate_votes[candidate_name]

            # Calculate the percentage of votes.
            vote_percentage = float(votes) / float(total_votes) * 100

            # Print the candidate name and percentage of votes.
            candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            # Print each candidate, their voter count, and percentage to the terminal.
            print(candidate_results)
            # Save the candidate results to our text file.
            txt_file.write(candidate_results)

            # Determine winning vote count and candidate.
            # Determine if the votes is greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):

                winning_count = votes

                winning_percentage = vote_percentage

                winning_candidate = candidate_name

        # Print the winning candidate's results
        winning_candidate_summary = (
            f"-------------------------\n"
            f"Winner: {winning_candidate}\n"
            f"Winning Vote Count: {winning_count:,}\n"
            f"Winning Percentage: {winning_percentage:.1f}%\n"
            f"-------------------------\n")
        print(winning_candidate_summary)
        # Save the winning candidate's name to the text file.
        txt_file.write(winning_candidate_summary)