from collections import deque
M,N = map(int,input().split())
T,Q = [],deque()
for i in range(N):
    T += [list(map(int,input().split()))]
    Q += [(i,j) for j in range(M) if T[i][j]==1]
while Q:
    x,y = Q.popleft()
    for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=a<N and 0<=b<M and T[a][b]==0:
            T[a][b] = T[x][y] + 1
            Q += [(a,b)]
print(-1 if any(1 for t in T if 0 in t) else T[x][y]-1)