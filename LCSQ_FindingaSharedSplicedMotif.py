from CONS_ConsensusProfile import fasta_to_list_without_name
import sys

def sort_DNA(dnalist,dict):
    sort_list = [0 for i in range(len(dnalist[1]))]

    for i in range(len(dnalist[0])):
        for j in range(len(dnalist[1])):
            n = 0
            if dnalist[0][i] == dnalist[1][j]:
                n += 1
                if n > dict[dnalist[0][i]]:
                    sort_list[j] += max(sort_list) + 1
        dict[dnalist[0][i]] += 1
    return sort_list

def LIS_loc(list):
    n = len(list)
    end = 1
    length = 1
    p = [0 for i in range(n)]
    l = [1 for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            if int(list[j]) < int(list[i]):
                if l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    p[i] = j
        if max(l) == l[i]:
            length = l[i]
            end = i
    location = [0 for i in range(length)]
    add = length - 1
    location[add] = end
    add = add-1
    while add >= 0:
        location[add] = p[end]
        add = add - 1
        end = p[end]
    return location


if __name__ == '__main__':
    #file = open('test.fasta')
    dict = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    file = sys.argv[1]
    DNAlist = fasta_to_list_without_name(file)
    final_seq = ''
    for i in LIS_loc(sort_DNA(DNAlist,dict)):
        final_seq += DNAlist[0][i]
    print(final_seq)