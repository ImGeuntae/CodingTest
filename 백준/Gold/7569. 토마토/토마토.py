from collections import deque
M,N,H = map(int,input().split())
T = [[0]*N for _ in range(H)]
Q = deque()
for h in range(H):
    for n in range(N):
        T[h][n] = list(map(int,input().split()))
        Q += [(h,n,m) for m in range(M) if T[h][n][m]==1]
while Q:
    h,n,m = Q.popleft()
    for x,y,z in [(h+1,n,m),(h-1,n,m),(h,n+1,m),(h,n-1,m),(h,n,m+1),(h,n,m-1)]:
        if 0<=x<H and 0<=y<N and 0<=z<M and T[x][y][z]==0:
            T[x][y][z] = T[h][n][m] + 1
            Q += [(x,y,z)]
print(-1 if any(any(1 for N in H if 0 in N) for H in T) else T[h][n][m]-1)