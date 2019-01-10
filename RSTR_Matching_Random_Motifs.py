def prob(s,gc):
    result = 1.0
    for i in s:
        if i == 'A':
            result = result*(1-gc)*0.5
        elif i == 'T':
            result = result * (1 - gc)*0.5
        elif i == 'G':
            result = result * gc*0.5
        elif i == 'C':
            result = result * gc*0.5
    return result

def match_random_motif(s,gc,N):
    match = 1-pow((1-prob(s,gc)),N)
    return match

if __name__ == '__main__':
    N = 81915
    x = 0.495783
    s = 'ACAACCGGTA'
    print(round(match_random_motif(s,x,N), 3))