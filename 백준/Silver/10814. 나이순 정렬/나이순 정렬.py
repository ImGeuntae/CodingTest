L = [input() for _ in range(int(input()))]
for i in sorted(L,key=lambda x:int(x.split()[0])):
    print(i)