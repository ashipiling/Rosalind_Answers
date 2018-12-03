def uncrossing(string):
    sum = 0
    dict1 = {'A': 1, 'C': 2, 'G': -2, 'U': -1}
    for i in string:
        sum += dict1[i]
    return sum

def mapping(string,dic):
    dict2 = {'A': 'U', 'C': 'G', 'G':'C', 'U': 'A'}
    list = []
    if len(string) <= 2:
        return 1
    elif string in dic:
        return dic[string]

    for i in range(len(string)):
        if dict2[string[0]] == string[i] and uncrossing(string[0:i + 1]) == 0:
            list.append(i)
    sum = 0
    for i in list:
        if mapping(string[1:i], dic) != None and  mapping(string[i+1: len(string)], dic)  != None:
            sum += mapping(string[1:i], dic) * mapping(string[i+1: len(string)], dic)
    dic[string] = sum
    return dic


if __name__ == '__main__':
    string_s = 'AUAUAUAUGC'
    dic = {}
    print(sorted(mapping(string_s,dic).values())[-1]%1000000)

