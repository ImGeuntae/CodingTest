import sys
N,M = map(int,input().split())
T = [list(map(int,sys.stdin.readline().split()))+[0] for _ in range(N)]+[[0]*(N+1)]
for i in range(N):
    for j in range(N):
        T[i][j] = T[i][j]+T[i-1][j]+T[i][j-1]-T[i-1][j-1]
for i in sys.stdin:
    a,b,c,d = map(int,i.split())
    print(T[c-1][d-1]-T[c-1][b-2]-T[a-2][d-1]+T[a-2][b-2])