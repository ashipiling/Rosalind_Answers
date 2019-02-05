import math
def countingDC(list):
    out = [0] * len(list)
    for i in range(len(list)):
      prop = list[i]
      prob = math.sqrt(prop)
      out[i] = prop + 2*prob*(1-prob)
    return out

if __name__ == '__main__':
    input = [0.1, 0.25, 0.5]
    out = countingDC(input)
    for i in out:
        print(round(i, 3), end=' ')
