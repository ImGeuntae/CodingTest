import heapq
N,M,X = map(int,input().split())
R = [[[] for _ in range(N+1)] for _ in range(2)]
for _ in range(M):
    a,b,c = map(int,input().split())
    R[0][a] += [(b,c)]
    R[1][b] += [(a,c)]
D = [[0 if n in (0,X) else float("INF") for n in range(N+1)] for _ in range(2)]
for x in range(2):
    Q = []
    heapq.heappush(Q,(0,X))
    while Q:
        t,n = heapq.heappop(Q)
        if D[x][n] >= t:
            for i,j in R[x][n]:
                c = t + j
                if c < D[x][i]:
                    D[x][i] = c
                    heapq.heappush(Q,(c,i))
print(max(sum(s) for s in zip(*D)))