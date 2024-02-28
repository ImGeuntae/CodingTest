import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
def f(n):
    s = 0
    for x in G[n]:
        if A[x] == -1:
            A[x] = f(x)
        s = max(s,A[x])
    return T[n] + s
for _ in range(int(input())):
    N,K = map(int,input().split())
    T = [0] + list(map(int,input().split()))
    A = [-1]*(N+1)
    G = [[] for _ in range(N+1)]
    for _ in range(K):
        X,Y = map(int,input().split())
        G[Y] += [X]
    print(f(int(input())))