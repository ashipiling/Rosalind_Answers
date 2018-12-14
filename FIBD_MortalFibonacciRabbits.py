n = 93
m = 20
array = [0 for i in range(m-1)]
array.append(1)
for i in range(n-1):
    num = sum([array[i] for i in range(m-1)])
    for i in range(m-1):
        array[i] = array[i+1]
    array[m-1] = num

print(sum(array))