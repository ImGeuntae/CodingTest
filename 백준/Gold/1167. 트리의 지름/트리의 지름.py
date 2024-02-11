import sys
sys.setrecursionlimit(10**5)
N = int(input())
T = [[] for _ in range(N+1)]
for i in sys.stdin:
    a,*b,_ = map(int,i.split())
    for x,y in zip(b[::2],b[1::2]):
        T[a] += [(x,y)]
def dfs(n,d):
    for x,y in T[n]:
        if V[x] == -1:
            V[x] = d+y
            dfs(x,d+y)
V = [-1]*(N+1)
V[1] = 0
dfs(1,0)
a = V.index(max(V))
V = [-1]*(N+1)
V[a] = 0
dfs(a,0)
print(max(V))