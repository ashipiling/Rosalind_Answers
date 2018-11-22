def DNA_to_RNA(DNAstring):
    DNAstring = DNAstring.upper()
    return DNAstring.replace('T','U')

DNA = input('请输入DNA序列：')
print(DNA_to_RNA(DNA))