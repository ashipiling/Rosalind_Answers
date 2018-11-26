def DNAReverse(dnastring):
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

if __name__ == '__main__':
    DNA = input('请输入DNA序列：').upper()
    print(DNAReverse(DNA))