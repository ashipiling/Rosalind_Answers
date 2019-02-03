from operator import mul
from fractions import Fraction
from functools import reduce

def combination(n, k):
    return int(reduce(mul,(Fraction(n-i,i+1) for i in range(k)),1))
def wrightFisher( N, m, g, k ):
    pRec = 1.0 - (m/(2.0*N))
    p = [combination(2*N,i)*((pRec)**i)*(1.0-pRec)**(2*N-i) for i in range(1,2*N+1)]
    for gen in range(2,g+1):
        tempList = []
        for j in range(1,2*N+1):
            tempTerm = [combination(2*N, j)*((x/(2.0*N))**j)*(1.0-(x/(2.0*N)))**(2*N-j) for x in range(1,2*N+1)]
            tempList.append(sum([tempTerm[i]*p[i] for i in range(len(tempTerm))]))
        p = tempList
    return sum(p[k-1:])

if __name__ == '__main__':
    N = 6
    m = 10
    g = 6
    k = 7
    print(wrightFisher(N, m, g, k))