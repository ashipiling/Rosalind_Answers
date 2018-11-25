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

DNA_list = fasta_to_list(fasta)

site_list = []
for i in range(2,7):
    for j in range(len(DNA_list[1])-i+1):
        if DNA_list[1][j:j+i] == rev(DNA_list[1][j+i : j+i+i]):
            site_list.append((j+1, i+i))

for i in sorted(site_list):
    print(str(i)[1:-1].replace(',',''))