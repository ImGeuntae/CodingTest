import sys
from collections import deque
N = int(input())
T = [[] for _ in range(N+1)]
ans = [0]*(N+1)
for i in sys.stdin:
    a,b = map(int,i.split())
    T[a] += [b]
    T[b] += [a]
Q = deque([1])
while Q:
    n = Q.popleft()
    for t in T[n]:
        if ans[t] == 0:
            ans[t] = n
            Q.append(t)
print(*ans[2:])