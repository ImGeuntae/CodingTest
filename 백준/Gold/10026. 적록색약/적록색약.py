N = int(input())
P,ans = [[],[]],[0]*2
for _ in range(N):
    I = input()
    P[0] += [[*I]]
    P[1] += [[*I.replace('R','G')]]
for n in range(2):
    for i in range(N):
        for j in range(N):
            if (c:=P[n][i][j]):
                ans[n] += 1
                Q = [(i,j)]
                P[n][i][j] = ''
                while Q:
                    x,y = Q.pop(0)
                    for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                        if 0<=a<N and 0<=b<N and P[n][a][b]==c:
                            P[n][a][b] = ''
                            Q += [(a,b)]
print(*ans)