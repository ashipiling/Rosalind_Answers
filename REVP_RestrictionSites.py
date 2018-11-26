import sys
from REVC_DNAReverse import DNAReverse
from GRPH_OverlapGraphs import fasta_to_list

fasta = open(sys.argv[1])
#fasta = open('test.fasta')
DNA_list = fasta_to_list(fasta)

site_list = []
for i in range(2,7):
    for j in range(len(DNA_list[1])-i+1):
        if DNA_list[1][j:j+i] == DNAReverse(DNA_list[1][j+i : j+i+i]):
            site_list.append((j+1, i+i))

for i in sorted(site_list):
    print(str(i)[1:-1].replace(',',''))