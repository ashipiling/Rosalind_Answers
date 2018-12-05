from CONS_ConsensusProfile import fasta_to_list_without_name
from itertools import product
import sys

#file = open('test.fasta')
file = open(sys.argv[1])
DNAlist = fasta_to_list_without_name(file)

permutation = product(['A','C','T','G'],repeat= 4)
dict = {}
for i in permutation:
    s = str(i)[1:-1].replace("'","").replace(', ','')
    dict[s] = 0

for i in range(len(DNAlist[0])-3):
    if DNAlist[0][i:i+4] in dict:
        dict[DNAlist[0][i:i + 4]] += 1

print(str(dict.values())[13:-2].replace(',',''))