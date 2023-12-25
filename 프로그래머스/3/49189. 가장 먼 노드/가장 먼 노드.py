from collections import deque
def solution(n, edge):
    D = [[] for _ in range(n+1)]
    for a,b in edge:
        D[a].append(b)
        D[b].append(a)
    queue,F = deque([1]), [(x==1)-1 for x in range(n+1)]
    while queue:
        q = queue.popleft()
        for x in D[q]:
            if F[x] == -1:
                F[x] = F[q] + 1
                queue.append(x)
    return F.count(max(F))