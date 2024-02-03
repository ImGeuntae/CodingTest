import sys
import heapq
N,M = int(input()),int(input())
G = [[] for _ in range(N)]
for i in sys.stdin:
    a,b,c = map(int,i.split())
    G[a-1] += [(c,b-1)]
for n in range(N):
    dist = [float("inf")]*N
    dist[n] = 0
    Q = [(0,n)]
    while Q:
        C,B = heapq.heappop(Q)
        if dist[B] >= C:
            for c,b in G[B]:
                x = c + C
                if dist[b] > x:
                    dist[b] = x
                    heapq.heappush(Q,(x,b))
    print(*[d if type(d) is int else 0 for d in dist])