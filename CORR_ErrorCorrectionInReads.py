from REVC_DNAReverse import DNAReverse
from CONS_ConsensusProfile import fasta_to_list_without_name
import sys

#file = open('test.fasta')
file = open(sys.argv[1])
DNAlist = fasta_to_list_without_name(file)

def align(s1,s2):
    num = 0
    for i in range(len(s1)):
        if s1[i] != s2[i] :
            num += 1
    if num <= 1:
        return True

list1 = []
dict = {}
for i in range(len(DNAlist)):
    for j in range(i+1, len(DNAlist)):
        if DNAlist[i] == DNAReverse(DNAlist[j]):
            list1.append(i)
            list1.append(j)
        elif DNAlist[i] == DNAlist[j]:
            dict[i] = j
for i in range(len(DNAlist)):
    if not i in list1 and not i in dict.keys() and not i in dict.values():
        for j in list1:
            if align(DNAlist[i],DNAlist[j]):
                print(DNAlist[i]+'->'+DNAlist[j])
        for k in dict:
            if align(DNAlist[i], DNAReverse(DNAlist[k])):
                print(DNAlist[i]+'->'+DNAReverse(DNAlist[k]))
