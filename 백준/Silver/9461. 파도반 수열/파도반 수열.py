for _ in range(int(input())):
    L = [0,0,1,0,1]
    for _ in range(int(input())-1):
        L.append(L.pop(0)+L[-1])
    print(L[-1])