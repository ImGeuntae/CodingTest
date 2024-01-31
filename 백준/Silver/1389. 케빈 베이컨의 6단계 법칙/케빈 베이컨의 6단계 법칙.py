N,M = map(int,input().split())
K = [[N*(i!=n) for i in range(N)] for n in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    K[a-1][b-1] = K[b-1][a-1] = 1
for j in range(N):
    for i in range(N):
        for k in range(N):
            if K[i][j] + K[j][k] < K[i][k]:
                K[i][k] = K[i][j] + K[j][k]
print(sorted(range(N), key=lambda x:sum(K[x]))[0]+1)