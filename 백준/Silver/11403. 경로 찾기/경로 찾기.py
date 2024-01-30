N = int(input())
G = [input().split() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if G[i][j] == '1':
            for k in range(N):
                if G[k][i] == '1':
                    G[k][j] = '1'
for g in G:
    print(*g)