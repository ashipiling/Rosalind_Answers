def LIDS(array):
    list1 = [[1] for i in range(len(array))]
    list2 = [[1] for i in range(len(array))]

    for i in range(len(array) - 1):
        list1[i] = [array[i]]
        list2[i] = [array[i]]
        for j in range(i + 1, len(array)):
            if int(array[j]) > int(max(list1[i],key=lambda x:int(x))):
                list1[i].append(array[j])
            elif int(array[j]) < int(min(list2[i],key=lambda x:int(x))):
                list2[i].append(array[j])
    list = [sorted(list1,key = lambda x : len(x),reverse=True)[0],sorted(list2,key = lambda x : len(x),reverse=True)[0]]
    return list


#array = ['2','4','3','5','10','9','8','6','1','7']
n = input('输入数列长度n：')
array = input('输入不重复数字序列，两数字间用空格断开：').split(' ')

result = LIDS(array)
for i in result:
    print(str(i)[1:-1].replace(',', '').replace("'",""))
