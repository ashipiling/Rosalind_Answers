import sys

def DNA_to_RNA(DNAstring):
    DNAstring = DNAstring.upper()
    return DNAstring.replace('T','U')

def fasta_to_list(fasta):
    list = [line.strip().upper() for line in fasta.readlines()]
    i = 2
    while i < len(list):
        if not list[i].startswith('>') and not list[i-1].startswith('>'):
            list[i-1] += list[i]
            list.pop(i)
            i -= 1
        i += 1
    return list

def Reverse(string):
    rev = ''
    for i in string:
        if i == 'A':
            rev = 'T' + rev
        elif i == 'C':
            rev = 'G' + rev
        elif i == 'G':
            rev = 'C' + rev
        elif i == 'T':
            rev = 'A' + rev
    return rev

codon_table = {}
codon = open('Codon.txt')
for line in codon.readlines():
    line = line.strip().split(' ')
    codon_table[line[0]] = line[1]

fasta = open(sys.argv[1])
#fasta = open('test.fasta')
Protein_list = fasta_to_list(fasta)
RNA = []
RNA.append(DNA_to_RNA(Protein_list[1]))
RNA.append(DNA_to_RNA(Reverse(Protein_list[1])))

prot =''
pro_list = []
for i in range(2):
    for j in range(len(RNA[i])-2):
        if RNA[i][j:j+3] == 'AUG':
            for k in range(int(len(RNA[i])-j / 3)):
                try:

                    if j + 3*k == len(RNA[i])-3 and codon_table[RNA[i][j+ 3 * k : j + 3 * k + 3]] != 'Stop':
                        prot = ''
                    elif codon_table[RNA[i][j+ 3 * k : j + 3 * k + 3]] != 'Stop':
                        prot += codon_table[RNA[i][j+ 3 * k: j +3 * k + 3]]
                    else:
                        pro_list.append(prot)
                        prot = ''

                        break
                except KeyError:
                    break

for i in set(pro_list):
    print(i)
