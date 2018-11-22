import itertools

n = input('请输入小于等于7的整数：')
print(n)

list = [i for i in range(1,n+1)]
iter = itertools.permutations(list,n)
for i in iter:
    print(str(i)[1:-1].replace(',',''))