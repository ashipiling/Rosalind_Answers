DNA = input('请输入DNA序列：')
DNA = DNA.upper()
rev = ''

for i in DNA:
    if i == 'A':
        rev = 'T' + rev
    elif i == 'C':
        rev = 'G' + rev
    elif i == 'G':
        rev = 'C' + rev
    elif i == 'T':
        rev = 'A' + rev
print(rev)