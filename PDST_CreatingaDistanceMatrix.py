from CONS_ConsensusProfile import fasta_to_list_without_name
import sys

def matrix(list):
    list1 = [[0 for j in list] for i in range(len(list))]
    for i in range(len(list)):
        for j in range(len(list)):
            list1[i][j] = hammingdistanceRatio(list[i],list[j])

    for i in list1:
        print(str(i)[1:-1].replace(',','').replace("'",''))

def hammingdistanceRatio(string1 , string2):
    length = len(string1)
    num = 0
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            num += 1
    Ratio = num/length
    return '{:.3f}'.format(Ratio)

if __name__ == '__main__':
    # file = open('test.fasta')
    file = sys.argv[1]
    DNAlist = fasta_to_list_without_name(file)
    matrix(DNAlist)