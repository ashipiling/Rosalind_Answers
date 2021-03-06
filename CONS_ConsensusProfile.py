import sys

def fasta_to_list_without_name(file):
    i = 2
    DNA_list = [line.strip().upper() for line in file.readlines()]
    while i < len(DNA_list):
        if not DNA_list[i].startswith('>') and not DNA_list[i - 1].startswith('>'):
            DNA_list[i - 1] += DNA_list[i]
            DNA_list.pop(i)
            i -= 1
        else:
            DNA_list.pop(i)
        i += 1
    DNA_list.pop(0)
    return DNA_list

def consensus(list):
    profile = [[0 for i in range(len(list[0]))] for j in range(4)]
    for seq in list:
        for i in range(len(seq)):
            if seq[i] == 'A':
                profile[0][i] += 1
            elif seq[i] == 'C':
                profile[1][i] += 1
            elif seq[i] == 'G':
                profile[2][i] += 1
            elif seq[i] == 'T':
                profile[3][i] += 1

    profile_trans = []
    result = ''
    for j in range(len(list[0])):
        profile_trans.append([profile[i][j] for i in range(4)])
    for i in range(len(profile_trans)):
        num = profile_trans[i].index(max(profile_trans[i]))
        if num == 0:
            result += 'A'
        elif num == 1:
            result += 'C'
        elif num == 2:
            result += 'G'
        elif num == 3:
            result += 'T'

    print(result)
    print('A: ' + str(profile[0])[1:].replace(']', '').replace(',', ''))
    print('C: ' + str(profile[1])[1:].replace(']', '').replace(',', ''))
    print('G: ' + str(profile[2])[1:].replace(']', '').replace(',', ''))
    print('T: ' + str(profile[3])[1:].replace(']', '').replace(',', ''))

if __name__ == '__main__':
    fasta = open(sys.argv[1])
    DNA_list = fasta_to_list_without_name(fasta)
    consensus(DNA_list)
    fasta.close()