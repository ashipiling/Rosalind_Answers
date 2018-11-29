import math
string_s = 'AAGTGCTCAGGACAGTCGGTTGGTACGTTATGGTACAGTTCACGTGTAATCAAGGTGAAAGCCCTGTAGCGTGAGCTAGACACTG'
string_num = '0.098 0.155 0.197 0.254 0.285 0.343 0.417 0.462 0.477 0.555 0.612 0.648 0.693 0.744 0.792 0.892 0.918'

list_num = string_num.split(' ')
product = [1 for i in range(len(list_num))]
for i in range(len(list_num)):
    for j in range(len(string_s)):
        if string_s[j] == 'A':
            product[i] = product[i] * (1-float(list_num[i])) * 0.5
        elif string_s[j] == 'T':
            product[i] = product[i] * (1-float(list_num[i])) * 0.5
        elif string_s[j] == 'G':
            product[i] = product[i] * float(list_num[i]) * 0.5
        elif string_s[j] == 'C':
            product[i] = product[i] * float(list_num[i]) * 0.5

logproduct = []
for i in product:
    logproduct.append(round(math.log10(i),3))
print(str(logproduct)[1:-1].replace(',',''))