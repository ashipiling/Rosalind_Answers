import sys
from collections import defaultdict

fasta_file = sys.argv[1]
#支持NCBI下载的多序列fasta文件

fasta = open(fasta_file)
dict = defaultdict(float)
ID = ''
list = [0,0,0,0]
for line in fasta.readlines():
    if line.startswith('>'):
        if not ID == '':
            dict[ID] = float((list[1]+list[2])/(list[0]+list[1]+list[2]+list[3]))
        ID = line.strip('>').split()[0]
        list = [0,0,0,0]
    if not line.startswith('>'):
        list[0] += line.count('A')
        list[1] += line.count('C')
        list[2] += line.count('T')
        list[3] += line.count('G')
dict[ID] = float((list[1]+list[2])/(list[0]+list[1]+list[2]+list[3]))
dict1 = sorted(dict)
print(dict1[0]+'\n'+str(dict[dict1[0]]))
