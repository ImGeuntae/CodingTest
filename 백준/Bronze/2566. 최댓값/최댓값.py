n = -1
for i in range(9):
    L = list(map(int,input().split()))
    if n < max(L):
        n,x,y = max(L),i+1,L.index(max(L))+1,
print(n)
print(x,y)