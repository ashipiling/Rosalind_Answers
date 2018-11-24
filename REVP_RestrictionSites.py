import sys
fasta = open(sys.argv[1])
#fasta = open('test.fasta')

def rev(dnastring):
    rev = ''
    for i in dnastring:
        if i == 'A':
            rev = 'T' + rev
        elif i == 'C':
            rev = 'G' + rev
        elif i == 'G':
            rev = 'C' + rev
        elif i == 'T':
            rev = 'A' + rev
    return rev
def fasta_to_dnalist(file):
    dna_list = [line.strip().upper() for line in file.readlines()]
    i = 2
    while i < len(dna_list):
        if not dna_list[i].startswith('>') and not dna_list[i-1].startswith('>'):
            dna_list[i-1] += dna_list[i]
            dna_list.pop(i)
            i -= 1
        i += 1
    return dna_list

DNA_list = fasta_to_dnalist(fasta)

site_list = []
for i in range(2,7):
    for j in range(len(DNA_list[1])-i+1):
        if DNA_list[1][j:j+i] == rev(DNA_list[1][j+i : j+i+i]):
            site_list.append((j+1, i+i))

for i in sorted(site_list):
    print(str(i)[1:-1].replace(',',''))