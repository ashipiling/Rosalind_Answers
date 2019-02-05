def pair(dict, string):
    if len(string) < 4:
        return 1
    if string in dict:
        return dict[string]
    else:
        dict[string] = pair(dict, string[1:])
        for i in range(4, len(string)):
            if string[i] in match[string[0]]:
                dict[string] += pair(dict, string[1:i]) * pair(dict, string[i + 1:])
    return dict[string]

if __name__ == '__main__':
    RNAseq = 'CCGUAUGGUAAGCAGGGCUUGCUCAACCACGCUAGGUGGAUUCCAGGGAUCUUCGAUAGCUGGUUUCUCCGGUGAUCUGAUUUCAUCACAGGGUGCUACCAACCGACCCAAACGCACACCUGUGUGUGGAGGGUCCCCAAUAAGGCCAAAUUAGACUACCCUAGUAAAACAGUAAGG'
    match = {'A': 'U', 'U': 'AG', 'C': 'G', 'G': 'CU'}
    dict = {}
    print(pair(dict,RNAseq))