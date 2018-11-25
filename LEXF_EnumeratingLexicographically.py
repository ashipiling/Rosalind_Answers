from itertools import product

string = input().replace(' ', '').strip()
n = int(input())

for i in product(string, repeat=n):
    print(str(i)[1:-1].replace("'","").replace(', ',''))