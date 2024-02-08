import heapq
N,M,X = map(int,input().split())
R = [[[] for _ in range(N+1)] for _ in range(2)]
for _ in range(M):
    a,b,c = map(int,input().split())
    R[0][a] += [(b,c)]
    R[1][b] += [(a,c)]
D = [[float("INF")]*2 for _ in range(N+1)]
D[0] = D[X] = [0,0]
for x in range(2):
    Q = []
    heapq.heappush(Q,(0,X))
    while Q:
        t,n = heapq.heappop(Q)
        if D[n][x] >= t:
            for i,j in R[x][n]:
                c = t + j
                if c < D[i][x]:
                    D[i][x] = c
                    heapq.heappush(Q,(c,i))
print(max(sum(s) for s in D))