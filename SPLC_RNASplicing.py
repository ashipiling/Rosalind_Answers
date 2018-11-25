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

def DNA_to_RNA(DNAstring):
    DNAstring = DNAstring.upper()
    return DNAstring.replace('T','U')

def Translation(CodonFile, RNA):
    prot = ''
    codon_table = {}
    for line in CodonFile.readlines():
        line = line.strip().split(' ')
        codon_table[line[0]] = line[1]

    for i in range(int(len(RNA) / 3)):
        if codon_table[RNA[3 * i:3 * i + 3]] != 'Stop':
            prot += codon_table[RNA[3 * i:3 * i + 3]]

    return prot

fasta = open(sys.argv[1])
#fasta = open('test.fasta')
codon = open('./PROT_RNA2Protein/Codon.txt')

DNA_list = fasta_to_list(fasta)
for i in range(1, int(len(DNA_list)/2)):
    DNA_list[1] = DNA_list[1].replace(DNA_list[i*2+1],'')

RNA = DNA_to_RNA(DNA_list[1])
protein = Translation(codon,RNA)

print(protein)



