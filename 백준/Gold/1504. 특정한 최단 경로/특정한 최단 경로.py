import heapq
import sys
input = sys.stdin.readline
N,E = map(int,input().split())
G = [[] for _ in range(N+1)]
for _ in range(E):
    a,b,c = map(int,input().split())
    G[a] += [(c,b)]
    G[b] += [(c,a)]
V = list(map(int,input().split()))
ans = [0,0]
for i in (0,1):
    D = [float("inf")]*(N+1)
    D[V[i]] = 0
    H = [(0,V[i])]
    while H:
        x,y = heapq.heappop(H)
        if D[y] >= x:
            for a,b in G[y]:
                c = a + x
                if c < D[b]:
                    D[b] = c
                    heapq.heappush(H,(c,b))
    ans[i] += D[1]
    ans[i-1] += D[N]
print(x if type((x:=min(ans)+D[V[0]])) is int else -1)