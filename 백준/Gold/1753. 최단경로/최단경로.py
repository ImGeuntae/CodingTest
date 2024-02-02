import heapq
import sys
input = sys.stdin.readline
V,E = map(int,input().split())
S = int(input()) - 1
G = [[] for _ in range(V)]
for _ in range(E):
    u,v,w = map(int,input().split())
    G[u-1] += [(w,v-1)]
dist = [float("INF")]*V
dist[S] = 0
Q = [(0,S)]
while Q:
    C,N = heapq.heappop(Q)
    if dist[N] >= C:
        for c,n in G[N]:
            x = C + c
            if x < dist[n]:
                dist[n] = x
                heapq.heappush(Q,(x,n))
print(*[d if type(d) is int else "INF" for d in dist])