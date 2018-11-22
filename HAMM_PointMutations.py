DNA1 = input('请输入第一条DNA序列：').upper()
DNA2 = input('请输入另一条DNA序列：').upper()

count = 0
if len(DNA1) ==len(DNA2):
    for i in range(len(DNA1)):
        if DNA1[i] != DNA2[i]:
            count += 1
    print(count)
else:
    print('请输入俩等长的序列')


