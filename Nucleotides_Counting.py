DNA = input('请输入DNA序列：')
DNA = DNA.upper()
count = ['A', 'C', 'G', 'T']

for i in count:
    print(i,":", DNA.count(i))