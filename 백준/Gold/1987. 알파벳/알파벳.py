N,M = map(int,input().split())
B = [list(input()) for _ in range(N)]
Q = set([(0,0,B[0][0])])
ans = 0
while Q:
    a,b,s = Q.pop()
    for x,y in [(a+1,b,),(a-1,b),(a,b+1),(a,b-1)]:
        if 0<=x<N and 0<=y<M and B[x][y] not in s:
            Q.add((x,y,s+B[x][y]))
        else:
            ans = max(ans,len(s))
print(ans)