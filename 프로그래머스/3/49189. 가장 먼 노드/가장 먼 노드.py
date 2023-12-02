from collections import deque
def solution(n, edge):
    D = {k: [] for k in range(1,n+1)}    
    for a,b in edge:
        D[a].append(b)
        D[b].append(a)
    queue,F = deque([1]), [-1 if x else 0 for x in range(n)]
    while queue:
        q = queue.popleft()
        for x in D[q]:
            if F[x-1] == -1:
                F[x-1] = F[q-1] + 1
                queue.append(x)
    return F.count(max(F))