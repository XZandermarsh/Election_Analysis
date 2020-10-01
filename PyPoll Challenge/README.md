# Election_Analysis

## Overview of Election Audit
* During this module, we were asked to perform a basic election audit analysis, tallying the total votes from a raw data set for three candidates, and to provide the votes for each candidate and the corresponding percentage of total votes.

Election-Audit Results: Using a bulleted list, address the following election outcomes. Use images or examples of your code as support where necessary.

### How many votes were cast in this congressional election?
* 369,711 votes were recorded in the source raw .csv file provided.

### Provide a breakdown of the number of votes and the percentage of total votes for each county in the precinct.
* County Votes:
  * Jefferson: 10.5% (38,855)
  * Denver: 82.8% (306,055)
  * Arapahoe: 6.7% (24,801)
 
### Which county had the largest number of votes?
* Denver County had the most votes in this election, with 306,055.

### Provide a breakdown of the number of votes and the percentage of the total votes each candidate received.
* Candidate Votes:
  * Charles Casper Stockham: 23.0% (85,213)
  * Diana DeGette: 73.8% (272,892)
  * Raymon Anthony Doane: 3.1% (11,606)
  
### Which candidate won the election, what was their vote count, and what was their percentage of the total votes?
* Diana DeGette won the election with 272,892 votes, representing 73.8% of the total votes.

### Election-Audit Summary: In a summary statement, provide a business proposal to the election commission on how this script can be used—with some modifications—for any election.
* The core concept of this script can be easily modified for any election. The only aspects of the script in current state that are specific to this election are the input and output file names. The rest of the script could be universally applied once the input/output files are variable with user input.

### Give at least two examples of how this script can be modified to be used for other elections.
* The first change that could be made to the script would be the input file, or "file_to_load."

* In the original code, we specified a particular .csv file as input. To make the script universal for any election, we could modify it to request the input file location and name from the user, as shown below:

  * file_to_load = input('Please provide the full path\\filename of the input file: ')

  * This will then request the user inputs the source file location/name to be read into the script, allowing it to be used for any election data file.
  
* The second change is now critical, because we do not want the same output file to be overwritten for each analysis. Therefore, we can request the user give a filename for the analysis .txt file, as shown below:
  
  * file_to_save = input('Please provide the full path\\filename of the output file: ')
  
 




 
