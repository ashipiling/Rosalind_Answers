import re

DNA = input('请输一条DNA string: ').upper()
substring = input('请输入一条substring: ').upper()
list = []

iter = re.finditer(substring , DNA)
for i in iter:
    print(i.start()+1)
#re的find存在bug，不能寻找叠加的motif！


for i in range(len(DNA)-len(substring)+1):
    if DNA[i:i+len(substring)] == substring:
        list.append(i+1)
print(list)
#输出改成list方便用