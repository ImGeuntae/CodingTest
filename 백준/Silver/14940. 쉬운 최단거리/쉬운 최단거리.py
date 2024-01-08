N,M = map(int,input().split())
F = []
for i in range(N):
    I = input().split()
    if '2' in I:
        s = (i,I.index('2'))
    F += [I]
Q = [s]
F[s[0]][s[1]] = 0
while Q:
    x,y = Q.pop(0)
    for a,b in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
        if 0<=a<N and 0<=b<M and F[a][b]=='1':
            F[a][b] = F[x][y] + 1
            Q += [(a,b)]
for f in F:
    print(*(-1 if x=='1' else x for x in f))