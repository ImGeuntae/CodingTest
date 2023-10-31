N,M = map(int,input().split())
B = ["0"]*N
for _ in range(M):
    i,j,k = map(int,input().split())
    for n in range(i-1,j):
        B[n] = str(k)
print(' '.join(B))