from itertools import product

s = 'LQHCIFATPYM'
n = 3

for i in range(3):
    l = product(s, repeat = i+1)
    for j in l:
        print(str(j)[1:-1].replace("'",'').replace(', ','').replace(',',''))