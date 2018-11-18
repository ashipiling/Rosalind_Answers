import sys
fasta = open(sys.argv[1])
#fasta = open('test.fasta')

k = 3
DNA_list = [line.strip().upper() for line in fasta.readlines()]
i = 2
while i < len(DNA_list):
    if not DNA_list[i].startswith('>') and not DNA_list[i-1].startswith('>'):
        DNA_list[i-1] += DNA_list[i]
        DNA_list.pop(i)
        i -= 1
    i += 1

dict = {}
for i in range(0,len(DNA_list),2):
    dict[DNA_list[i].replace('>','')] = DNA_list[i+1]

for key_i in dict.keys():
    for key_j in dict.keys():
        if key_i != key_j:
            if dict[key_i][-k:] == dict[key_j][0:k]:
                print(key_i,key_j)

fasta.close()