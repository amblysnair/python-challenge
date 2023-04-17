import os
import csv

csvpath = os.path.join('', 'Resource', 'election_data.csv')

total_votes = 0

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
   
    csvreader = csv.reader(csvfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    
    charles_vote = 0
    diana_vote = 0
    raymon_vote = 0
    winner =0

    csv_header = next(csvreader)
 
    for row in csvreader:
         total_votes +=1
         if str(row[2])=='Charles Casper Stockham':
            charles_vote +=1
         elif str(row[2]) == 'Diana DeGette':
             diana_vote +=1
         elif str(row[2])== 'Raymon Anthony Doane':
             raymon_vote +=1


    if charles_vote > diana_vote:
        winner   = charles_vote
        winner_name = 'Charles Casper Stockham'
    else:
        winner = diana_vote
        winner_name = 'Diana DeGette'
    
    if winner < raymon_vote:
        winner_name = 'Raymon Anthony Doane'
        winner = raymon_vote





print("\n Election Results")
print("\n--------------------\n")

print(f"Total Votes : {total_votes} ")

print("\n--------------------\n")


print(f"Charles Casper Stockham : {round(charles_vote/total_votes*100,3)}% ({charles_vote})")

print(f"\nDiana DeGette : {round(diana_vote/total_votes*100,3)}% ({diana_vote})")

print(f"\nRaymon Anthony Done : {round(raymon_vote/total_votes*100,3)}% ({raymon_vote})")


print("\n--------------------------------")

print(f"\nWinner :  {winner_name}")


print("\n--------------------------------")