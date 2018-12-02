from CONS_ConsensusProfile import fasta_to_list_without_name
import sys

#file = open('test.fasta')
file  = sys.argv[1]
fasta = fasta_to_list_without_name(file)

list = []
count = 0
for i in range(len(fasta[1])):
    for j in range(len(fasta[0])):
        if fasta[1][i] == fasta[0][j] and j >= count:
            list.append(j+1)
            count = j
            break
print(list)

file.close()