import sys

def fasta_to_list(file):
    list = [line.strip().upper() for line in file.readlines()]
    i = 2
    while i < len(list):
        if not list[i].startswith('>') and not list[i-1].startswith('>'):
            list[i-1] += list[i]
            list.pop(i)
            i -= 1
        i += 1
    return list

if __name__ == '__main__':
    fasta = open(sys.argv[1])
    #fasta = open('test.fasta')
    DNA_list = fasta_to_list(fasta)
    print(DNA_list)
    k = 7

    dict = {}
    for i in range(0, len(DNA_list), 2):
        dict[DNA_list[i].replace('>', '')] = DNA_list[i + 1]
    for key_i in dict.keys():
        for key_j in dict.keys():
            if key_i != key_j:
                if dict[key_i][-k:] == dict[key_j][0:k]:
                    print(key_i, key_j)
