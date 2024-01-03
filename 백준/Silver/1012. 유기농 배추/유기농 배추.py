move = [(1,0),(-1,0),(0,1),(0,-1)]
for _ in range(int(input())):
    M,N,K = map(int,input().split())
    F = [[0]*M for _ in range(N)]
    for _ in range(K):
        x,y = map(int,input().split())
        F[y][x] = 1
    ans = 0
    for x in range(M):
        for y in range(N):
            if F[y][x]:
                ans += 1
                q = [(x,y)]
                while q:
                    a,b = q.pop(0)
                    if F[b][a]:
                        F[b][a] = 0
                        q.extend((a+m[0],b+m[1]) for m in move if 0<=a+m[0]<M and 0<=b+m[1]<N)
    print(ans)