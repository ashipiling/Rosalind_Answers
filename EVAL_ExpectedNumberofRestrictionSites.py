def expectednumber(n , s,array):
    result = [0 for i in range(len(array))]
    for i in range(len(array)):
        gc = array[i]
        prob = 1.0
        for j in range(len(s)):
            if s[j] == 'A' or s[j]== 'T':
                prob = prob * (1-gc) * 0.5
            elif s[j] == 'C' or s[j] == 'G':
                prob = prob * gc * 0.5
        result[i] = prob * (n- len(s)+1)
    return result
if __name__ == '__main__':
    n = 885537
    string = 'TAGTGCCC'
    array = [0.000,0.065,0.131,0.210,0.273,0.287,0.343,0.406,0.492,0.547,0.561,0.660,0.673,0.749,0.808,0.885,0.940,1.000]
    res = expectednumber(n,string,array)
    for i in res:
        print(round(i,3), end=' ')
