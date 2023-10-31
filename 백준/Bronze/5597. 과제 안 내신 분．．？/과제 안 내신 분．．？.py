L = [i+1 for i in range(30)]
for x in range(28):
    L.remove(int(input()))
print(sorted(L)[0], sorted(L)[1])