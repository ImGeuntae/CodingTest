from collections import deque
N,K = map(int,input().split())
d = deque(range(1,N+1))
print("<",end='')
while len(d)>1:
    for _ in range(K-1):
        d.append(d.popleft())
    print(d.popleft(),end=', ')
print(d.pop(), end='>')