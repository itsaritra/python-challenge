import os
import csv

polldata_csv = os.path.join('..', 'election_data.csv')

def percentage (part, whole):
    return 100 * float(part)/float(whole)

with open (polldata_csv, 'r') as polldatafile:
    csvreader = csv.reader(polldatafile, delimiter = ',')

    csv_header = next(polldatafile)
    voter_total = 0
    Khan_vote_count = 0
    Correy_vote_count = 0
    Li_vote_count = 0
    Tooley_vote_count = 0
    max_votecount = 0


    for row in csv.reader(polldatafile):
        voter = int(row[0])
        county = row[1]
        candidate_name = row[2]

        voter_total +=1

        if candidate_name == "Khan":
            Khan_vote_count += 1
        if candidate_name == "Coorey":
            Correy_vote_count += 1
        if candidate_name == "Li":
            Li_vote_count += 1
        if candidate_name == "O'Tooley":
            Tooley_vote_count += 1

    candidate_dict = {"Khan": Khan_vote_count,"Correy": Correy_vote_count,"Li" :Li_vote_count,
                         "O'Tooley": Tooley_vote_count}
    for candidate, value in candidate_dict.items():
	    if value > max_votecount:
	        max_votecount = value
	        winner = candidate
with open("Output.txt", "w") as text_file:


    
    print(f'Election results', file=text_file)
    print(f'------------------', file=text_file)
    print(f'Total number of votes casted: {voter_total}', file=text_file)
    print(f'------------------', file=text_file)
    print(f'Khan: {percentage(Khan_vote_count, voter_total):.3f}%  ({Khan_vote_count})', file=text_file)
    print(f'Correy: {percentage(Correy_vote_count, voter_total):.3f}%  ({Correy_vote_count})', file=text_file)
    print(f'Li: {percentage(Li_vote_count, voter_total):.3f}%  ({Li_vote_count})', file=text_file)
    print(f"O'Tooley: {percentage(Tooley_vote_count, voter_total):.3f}%  ({Tooley_vote_count})", file=text_file)
    print(f'--------------------------------', file=text_file)
    print(f'Winner: {winner}', file=text_file)
    print(f'--------------------------------', file=text_file)


