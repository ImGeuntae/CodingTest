import sys
from collections import deque
input = sys.stdin.readline
N,M = map(int,input().split())
G = [list(input()) for _ in range(N)]
n,D = 0,[]
for i in range(N):
    for j in range(M):
        if G[i][j]=='0':
            Q = deque([(i,j)])
            G[i][j] = n
            k = 1
            while Q:
                a,b = Q.popleft()
                for x,y in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
                    if 0<=x<N and 0<=y<M and G[x][y]=='0':
                        G[x][y] = n
                        k += 1
                        Q += [(x,y)]
            D += [k]
            n += 1
A = [['0']*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if G[i][j]=='1':
            A[i][j] = str((1 + sum(D[k] for k in {G[x][y] for x,y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)] if 0<=x<N and 0<=y<M and G[x][y]!='1'}))%10)
for a in A:
    print(''.join(a))