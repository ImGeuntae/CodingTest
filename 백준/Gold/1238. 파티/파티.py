import heapq
N,M,X = map(int,input().split())
R = [{k: [] for k in range(1,N+1)} for _ in range(2)]
for _ in range(M):
    a,b,c = map(int,input().split())
    R[0][a] += [(b,c)]
    R[1][b] += [(a,c)]
dist = [[0 if n in (0,X) else float("INF") for n in range(N+1)] for _ in range(2)]
for x in range(2):
    Q = []
    heapq.heappush(Q,(0,X))
    while Q:
        time,node = heapq.heappop(Q)
        if dist[x][node] >= time:
            for i in R[x][node]:
                cost = time + i[1]
                if cost < dist[x][i[0]]:
                    dist[x][i[0]] = cost
                    heapq.heappush(Q,(cost,i[0]))
print(max(sum(s) for s in zip(*dist)))