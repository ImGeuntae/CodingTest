import sys
N,M = int(input()),int(input())
G = [[0 if i==j else float("inf") for i in range(N)] for j in range(N)]
for i in sys.stdin:
    a,b,c = map(int,i.split())
    G[a-1][b-1] = min(G[a-1][b-1],c)
for j in range(N):
    for i in range(N):
        for k in range(N):
            G[i][k] = min(G[i][k],G[i][j]+G[j][k])
for g in G:
    print(*[n if type(n) is int else 0 for n in g])