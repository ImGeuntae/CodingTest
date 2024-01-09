from collections import deque
M,N = map(int,input().split())
T,Q,z = [],deque(),0
for i in range(N):
    T += [input().split()]
    for j in range(M):
        if T[i][j] == '1':
            Q += [(i,j)]
            T[i][j] = 0
        elif T[i][j] == '0':
            z += 1
while Q:
    x,y = Q.popleft()
    for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=a<N and 0<=b<M and T[a][b]=='0':
            T[a][b] = T[x][y] + 1
            z -= 1
            Q += [(a,b)]
print(-1 if z else T[x][y])