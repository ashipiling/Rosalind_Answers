n = int(input('请输入繁殖月数'))
k = int(input())

a,b = 0,1
for i in range(1,n):
    a,b = b,k*a+b
    print(a,b)
print(b)