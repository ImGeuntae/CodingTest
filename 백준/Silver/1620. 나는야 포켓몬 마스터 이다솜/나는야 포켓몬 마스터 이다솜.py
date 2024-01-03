import sys
input = sys.stdin.readline
N,M = map(int,input().split())
D,L = {},[0]
for i in range(1,N+1):
    x = input().strip()
    D[x] = i
    L += [x]
for _ in range(M):
    x = input().strip()
    print(L[int(x)] if x.isdigit() else D[x])