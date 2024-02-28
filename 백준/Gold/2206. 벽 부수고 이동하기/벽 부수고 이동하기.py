import sys
from collections import deque
N,M = map(int,input().split())
G = []
for i in sys.stdin:
    G += [list(i.rstrip())]
V = [[[0,0] for _ in range(M)] for _ in range(N)]
Q = deque([(0,0,1,1)])
V[0][0][1] = 1
while Q:
    a,b,c,d = Q.popleft()
    if a == N-1 and b == M-1:
        print(c)
        break
    for x,y in [(a+1,b),(a-1,b),(a,b+1),(a,b-1)]:
        if 0<=x<N and 0<=y<M:
            if d == 1:
                if G[x][y] == '0' and V[x][y][1] == 0:
                    Q.append((x,y,c+1,1))
                    V[x][y][1] = 1
                elif G[x][y] == '1' and V[x][y][0] == 0:
                    Q.append((x,y,c+1,0))
                    V[x][y][0] = 1
            elif d == 0:
                if G[x][y] == '0' and V[x][y][0] == 0:
                    Q.append((x,y,c+1,0))
                    V[x][y][0] = 1
else:
    print(-1)