from collections import deque
N,M = map(int,input().split())
C,Q,ans = [],deque(),0
for i in range(N):
    C += [[*input()]]
    Q += [(i,j) for j in range(M) if C[i][j]=='I']
while Q:
    x,y = Q.popleft()
    for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=a<N and 0<=b<M and (c:=C[a][b]) != 'X':
            if c == 'P':
                ans += 1
            C[a][b] = 'X'
            Q += [(a,b)]
print(ans if ans else 'TT')