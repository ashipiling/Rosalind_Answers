RNA = input('请输入RNA序列：').upper()

codon_table = {}
prot = ''
codon = open('Codon.txt')
for line in codon.readlines():
    line = line.strip().split(' ')
    codon_table[line[0]] = line[1]

for i in range(int(len(RNA)/3)):
    if codon_table[RNA[3*i:3*i+3]] != 'Stop':
        prot += codon_table[RNA[3*i:3*i+3]]

print(prot)

