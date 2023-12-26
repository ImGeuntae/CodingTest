import sys
input = sys.stdin.readline
N,M = map(int,input().split())
D = dict()
for _ in range(N):
    s,p = input().split()
    D[s] = p
for _ in range(M):
    print(D[input().strip()])