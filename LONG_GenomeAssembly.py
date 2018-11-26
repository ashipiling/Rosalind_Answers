from CONS_ConsensusProfile import fasta_to_list_without_name
import re

def GenomeAssembly(list):
    assembly_string = ''
    l1 = []
    l2 = []
    for i in range(len(list)):
        for j in range(len(list)):
            if i != j:
                result = re.search(list[i][0:int(len(list[i]) / 2)], list[j])
                if result != None:
                    l1.append([[j, result.start()], [i, -1]])

    for i in l1:
        for j in l1:
            if i != j:
                if l2 == []:
                    l2.append(j[0])
                    l2.append(j[1])
                elif l2[0][0] == j[-1][0]:
                    l2.insert(0, j[0])
                elif l2[-1][0] == j[0][0]:

                    l2[-1] = j[0]
                    l2.append(j[-1])
    for i in l2:
        assembly_string += list[i[0]][0:i[1]]
    assembly_string += list[l2[-1][0]][-1]
    return assembly_string

if __name__ == '__main__':
    fasta = open('test.fasta')
    DNAlist = fasta_to_list_without_name(fasta)
    print(GenomeAssembly(DNAlist))
