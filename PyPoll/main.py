# %%
# import necessary modules
import os
import csv


# %%
# define file path
csvpath = os.path.join("PyPoll", "Resources", "election_data.csv")

# %%
 # variables
total_votes = 0
candidates = []
candidates_votes = []
candidates_percent = []

# %%
# open file
with open(csvpath, 'r') as csvfile:
    # initialize csvreader
    csvreader = csv.reader(csvfile, delimiter=',')

    # gather header (column names)
    header = next(csvreader)

    for row in csvreader:
        # vote counter
        total_votes += 1

        # list of candidates
        if row[2] not in candidates:
            candidates.append(row[2])
            candidates_votes.append(1)
        # votes per candidate
        else:
            candidates_votes[candidates.index(row[2])] +=1

    winner_votes = candidates_votes[0]

    # votes per candidate (percent)
    for votes in range(len(candidates_votes)):
        percent = round(candidates_votes[votes] / total_votes * 100, 3)
        candidates_percent.append(percent)

        # find winner
        if winner_votes < candidates_votes[votes]:
            winner_votes = candidates_votes[votes]
    
    winner = candidates[candidates_votes.index(winner_votes)]

# print(candidates)
# print(candidates_votes)
# print(candidates_percent)
# print(winner)



# %%
# print results
results = ["Election Results",
           "-------------------------",
           f'Total Votes: {total_votes}',
           "-------------------------"
        ]

for people in candidates:
    people_index = candidates.index(people)
    results.append(f'{candidates[people_index]}: {candidates_percent[people_index]}% ({candidates_votes[people_index]})')
    
results.append("-------------------------")
results.append(f'Winner: {winner}')
results.append("-------------------------")

for line in results:
    print(line)

# %%
# set output file path
output_path = os.path.join("PyPoll", "Analysis", "election_analysis.txt")

# %%
# write to output file
with open(output_path, 'w') as f:
    for line in results:
        f.write(f'{line} \n')

# %%



