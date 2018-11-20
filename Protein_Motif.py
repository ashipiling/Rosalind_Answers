import sys
import re

motif = 'N[^P][S|T][^P]'
fasta = open(sys.argv[1])
#fasta = open('proteintest.fasta')

Protein_list = [line.strip().upper() for line in fasta.readlines()]
i = 2
while i < len(Protein_list):
    if not Protein_list[i].startswith('>') and not Protein_list[i-1].startswith('>'):
        Protein_list[i-1] += Protein_list[i]
        Protein_list.pop(i)
        i -= 1
    i += 1

for i in range(0,len(Protein_list),2):
    result = re.finditer(motif, Protein_list[i+1])
    list = []
    for j in result:
        list.append(j.start()+1)
    if not list == []:
        print(Protein_list[i].split('|')[1]+'\n'+str(list)[1:-2].replace(',',''))
