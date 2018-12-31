def LIS(list):
    n = len(list)
    end = 1
    length = 1
    p = [0 for i in range(n)]
    l = [1 for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            if int(list[j]) < int(list[i]):
                if l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    p[i] = j
        if max(l) == l[i]:
            length = l[i]
            end = i
    result = [0 for i in range(length)]
    add = length - 1
    while add >= 0:
        result[add] = list[end]
        end = p[end]
        add = add - 1
    return result

def LDS(list):
    n = len(list)
    end = 1
    length = 1
    p = [0 for i in range(n)]
    l = [1 for j in range(n)]
    for i in range(n):
        for j in range(0, i):
            if int(list[j]) > int(list[i]):
                if l[i] < l[j] + 1:
                    l[i] = l[j] + 1
                    p[i] = j
        if max(l) == l[i]:
            length = l[i]
            end = i
    result = [0 for i in range(length)]
    add = length - 1
    while add >= 0:
        result[add] = list[end]
        end = p[end]
        add = add - 1
    return result

if __name__ == '__main__':
    array = ['2','4','3','5','10','9','8','6','1','7']
    result_i = LIS(array)
    print(str(result_i)[1:-1].replace(',','').replace("'",''))
    result_d = LDS(array)
    print(str(result_d)[1:-1].replace(',', '').replace("'", ''))