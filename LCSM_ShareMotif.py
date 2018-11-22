import sys
from collections import OrderedDict
#fasta = open(sys.argv[1])
fasta = open('proteintest.fasta')
DNA_list = [line.strip().upper() for line in fasta.readlines()]

i = 2
while i < len(DNA_list):
    if not DNA_list[i].startswith('>') and not DNA_list[i-1].startswith('>'):
        DNA_list[i-1] += DNA_list[i]
        DNA_list.pop(i)
        i -= 1
    else:
        DNA_list.pop(i)
    i += 1
DNA_list.pop(0)
DNA_list.sort(key=lambda x:len(x))

dict= OrderedDict()
for i in range(2,len(DNA_list[0])):
    for j in range(len(DNA_list[0])-i+1):
        motif = DNA_list[0][j:i+j]
        for k in range(1,len(DNA_list)):
            if motif in DNA_list[k]:
                dict[i] = motif

print(next(reversed(dict.values())))

fasta.close()

