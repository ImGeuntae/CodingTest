from collections import deque, defaultdict
N,M,V = map(int,input().split())
node = defaultdict(list)
for _ in range(M):
    a,b = map(int,input().split())
    node[a].append(b)
    node[b].append(a)

visited, queue = list(),deque()
queue.append(V)
while queue:
    n = queue.popleft()
    if n not in visited:
        visited.append(n)
        queue.extendleft(sorted(node[n],reverse=True))
print(*visited)

visited, queue = list(),deque()
queue.append(V)
while queue:
    n = queue.popleft()
    if n not in visited:
        visited.append(n)
        queue.extend(sorted(node[n]))
print(*visited)