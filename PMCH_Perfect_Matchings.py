import math
s = 'AGGAGAACGCCGCAUAGAUCGUACGCCUUCAUCGGGGCUCGUCUUCUGUGCUCACUUAUGAUGGCGAUAAACAAUA'

num_a = 0
num_c = 0
for i in s:
    if i == 'A':
        num_a += 1
    elif i == 'C':
        num_c += 1
f_a = math.factorial(num_a)
f_c = math.factorial(num_c)
print(f_a * f_c)