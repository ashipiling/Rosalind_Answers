from itertools import permutations
n = input('请输入一个小于等于6的正整数：')

list = [i for i in range(1,n+1)]+[-i for i in range(1,n+1)]

p = permutations(list,n)
out_string = ''
num = 0
for i in p:
    if i[0] != i[1]*-1:
        out_string += str(i)[1:-1].replace(',','')+'\n'
        num += 1

print(num)
print(out_string)