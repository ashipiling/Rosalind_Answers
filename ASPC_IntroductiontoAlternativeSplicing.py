from itertools import combinations
n,m = 6,3
list = [i for i in range(n)]

num = 0
for i in range(m,n+1):
    c = combinations(list,i)
    for j in c:
        num +=1
        if num > 1000000:
            num = num % 1000000

print(num)