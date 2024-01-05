move = [(1,0),(-1,0),(0,1),(0,-1)]
N,M = map(int,input().split())
m = [['0']*(M+2) for _ in range(N+2)]
for i in range(1,N+1):
    m[i][1:-1] = list(input())
m[0][1] = x = y = 0
L = [(1,1)]
while x!=N or y!=M:
    x,y = L.pop(0)
    if m[x][y] == '1':
        m[x][y] = min(m[x+a][y+b] for a,b in move if isinstance(m[x+a][y+b],int))+1
        L.extend((x+a,y+b) for a,b in move if m[x+a][y+b] == '1')
print(m[N][M])