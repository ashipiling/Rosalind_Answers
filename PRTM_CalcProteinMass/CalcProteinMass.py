protein_string = input('请输入蛋白序列：')
#protein_string = 'SKADYEK'

mass_table = {}
mass = open('monoisotopic_mass_table.txt')
for line in mass.readlines():
    line = line.strip().split(' ')
    mass_table[line[0]] = line[1]

sum = 0
for i in protein_string:
    sum += float(mass_table[i])

print(round(sum,3))