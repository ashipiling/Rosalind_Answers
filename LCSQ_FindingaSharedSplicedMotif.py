from CONS_ConsensusProfile import fasta_to_list_without_name
import sys

def sort_DNA(dnalist):
    sort_list = [0 for i in range(len(DNAlist[1]))]
    dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for i in range(len(DNAlist[0])):
        for j in range(len(DNAlist[1])):
            n = 0
            if DNAlist[0][i] == DNAlist[1][j]:
                n += 1
                if n > dict[DNAlist[0][i]]:
                    sort_list[j] += max(sort_list) + 1
        dict[DNAlist[0][i]] += 1
    return sort_list

def longestIncreasingSubseq(list):
    list1 = [[] for i in range(len(list))]
    list2 = [[] for i in range(len(list))]
    for i in range(len(list) - 1):
        list1[i] = [list[i]]
        list2[i].append(i)
        for j in range(i, len(list)):
            if int(list[j]) > int(max(list1[i], key=lambda x: int(x))):
                list2[i].append(j)
                list1[i].append(list[j])
    return sorted(list2, key = lambda x:len(x),reverse= True)[0]


if __name__ == '__main__':
    #file = open('test.fasta')
    file = sys.argv[1]
    DNAlist = fasta_to_list_without_name(file)
    final_seq = ''
    for i in longestIncreasingSubseq(sort_DNA(DNAlist)):
        final_seq += DNAlist[0][i]
    print(final_seq)
