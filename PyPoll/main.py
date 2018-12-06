import os
import csv


voterid=[]
county=[]
candidates=[]
unique=[]


#set the path where the raw data is stored

path=os.path.join('Resources','election_data.csv')

#read the raw data

with open(path) as raw_data:

    reader=csv.reader(raw_data)

    header=next(reader)

    #set the dataframe

    for row in reader:

        voterid.append(row[0])
        county.append(row[1])
        candidates.append(row[2])

# unique candidates list whith list comprenhensions
[unique.append(i) for i in candidates if not unique.count(i)]

#calculate the total votes
totalvotes=len(voterid)

#calculate the total votes and the percent of votes for each candidate

votes=[candidates.count(candidate) for candidate in unique]
pct_votes=[candidates.count(candidate)/totalvotes for candidate in unique]

#Print the results in terminal

print('-----------------Electoral Results------------------------------')

print('\n')

print(f'Total Voters: {totalvotes:,}')

print('\n')

print('------------------Votes by Candidate----------------------------')

print('\n')

for i in range(len(unique)):

    print(f'Candidate:{unique[i]}, votes: {pct_votes[i]*100:.2f}% ({votes[i]:,})')

print('\n')

print('---------------------Final result--------------------------------')

print(f'Winner:{unique[pct_votes.index(max(pct_votes))]}')

print('\n')

# Print the results in .txt

report=open("Elections_Report.txt","w")

report.write('-----------------Electoral Results------------------------------\n')

report.write('\n')

report.write(f'Total Voters: {totalvotes:,}\n')

report.write('\n')

report.write('------------------Votes by Candidate----------------------------\n')

report.write('\n')

for i in range(len(unique)):

    report.write(f'Candidate:{unique[i]}, votes: {pct_votes[i]*100:.2f}% ({votes[i]:,})\n')

report.write('\n')

report.write('---------------------Final result--------------------------------\n')

report.write(f'Winner:{unique[pct_votes.index(max(pct_votes))]}\n')

report.write('\n')

report.close()













