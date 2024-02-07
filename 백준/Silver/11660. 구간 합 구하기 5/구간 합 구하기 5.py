import sys
input = sys.stdin.readline
N,M = map(int,input().split())
T = [[0]*(N+1)]
for _ in range(N):
    s = 0
    T += [[0]+[(s:=b+s)+a for a,b in zip(T[-1][1:],list(map(int,input().split())))]]
for _ in range(M):
    a,b,c,d = map(int,input().split())
    print(T[c][d] - T[c][b-1] - T[a-1][d] + T[a-1][b-1])