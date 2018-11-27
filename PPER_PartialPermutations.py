n = input()
k = input()

product = 1
for i in range(int(n)-int(k)+1, int(n)+1):
    product = i * product
    if product > 1000000:
        product = product % 1000000

print(product)