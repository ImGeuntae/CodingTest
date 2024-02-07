N,M,R = map(int,input().split())
I = list(map(int,input().split()))
G = [[0 if i==j else float("inf") for j in range(N)] for i in range(N)]
for _ in range(R):
    a,b,c = map(int,input().split())
    G[a-1][b-1] = G[b-1][a-1] = c
for j in range(N):
    for i in range(N):
        for k in range(N):
            G[i][k] = min(G[i][k],G[i][j]+G[j][k])
print(max(sum(I[j] for j in range(N) if G[i][j]<=M) for i in range(N)))