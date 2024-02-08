import sys
sys.setrecursionlimit(10**5)
N = int(input())
T = [[] for _ in range(N+1)]
for i in sys.stdin:
    a,b,c = map(int,i.split())
    T[a] += [(b,c)]
    T[b] += [(a,c)]
def dfs(n,c):
    for x,y in T[n]:
        if V[x] == -1:
            V[x] = c+y
            dfs(x,c+y)
V = [-1]*(N+1)
V[1] = 0
dfs(1,0)
a = V.index(max(V))
V = [-1]*(N+1)
V[a] = 0
dfs(a,0)
print(max(V))