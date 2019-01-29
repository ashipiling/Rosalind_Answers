treefile = open('Tree.txt')
dataset = treefile.readlines()
num = int(dataset[0].replace("\n",''))
edges = []
for i in range(1,len(dataset)):
    edges.append(dataset[i].replace("\n",'').split())
print(num - len(edges)-1)
