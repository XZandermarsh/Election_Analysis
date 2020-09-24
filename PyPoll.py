# The data we need to retrieve

# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate received
# 4. The total number of votes each candidate received
# 5. The winner of the election based on popular vote.

# Import the datetime class from the datetime module
import datetime as dt
import os
import random
import csv

now = dt.datetime.now()

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load, 'r') as election_data:

    # Read and analyze data

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    # print(headers)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)

# Close the file.
election_data.close()
