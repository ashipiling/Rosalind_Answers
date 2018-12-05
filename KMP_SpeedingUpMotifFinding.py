from CONS_ConsensusProfile import fasta_to_list_without_name
import sys

#file = open('test.fasta')
file = open(sys.argv[1])
DNAlist = fasta_to_list_without_name(file)

list = [0 for i in range(len(DNAlist[0]))]
for i in range(len(DNAlist[0])):
    for j in range(i,len(DNAlist[0])):
        if DNAlist[0][0:i+1] == DNAlist[0][j-i+1:j+2]:
            list[j+1] = i+1

print(str(list)[1:-1].replace(',',''))
