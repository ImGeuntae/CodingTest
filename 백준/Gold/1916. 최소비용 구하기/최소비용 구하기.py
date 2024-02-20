import sys
import heapq
input = sys.stdin.readline
N = int(input())
B = [[] for _ in range(N+1)]
for _ in range(int(input())):
    a,b,c = map(int,input().split())
    B[a] += [(c,b)]
dist = [float('inf')]*(N+1)
s,e = map(int,input().split())
dist[s] = 0
H = [(0,s)]
while H:
    c,n = heapq.heappop(H)
    if dist[n] >= c:
        for x,y in B[n]:
            z = x+c
            if dist[y] > z:
                dist[y] = z
                heapq.heappush(H,(z,y))
print(dist[e])