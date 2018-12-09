def maxMatch(string):
    dict = {'A':0, 'C':0, 'G':0, 'U':0}
    for i in string:
        dict[i] += 1
    max_AU = max(dict['A'],dict['U'])
    min_AU = min(dict['A'],dict['U'])
    max_GC = max(dict['G'],dict['C'])
    min_GC = min(dict['G'],dict['C'])
    pro_AU = 1
    pro_GC = 1
    for i in range(max_AU-min_AU+1, max_AU+1):
        pro_AU *= i
    for i in range(max_GC-min_GC+1, max_GC+1):
        pro_GC *= i
    return pro_AU * pro_GC

if __name__ == '__main__':
    RNA_s = 'AAGCUUUAAUACGACACCUGAAAGCUGAGUCUGAGGGAAUGACAUUAAACUUUAUUCGCACUACGCCCGGGGGUCGCGGAAUGUUUCCG'
    print(maxMatch(RNA_s))

