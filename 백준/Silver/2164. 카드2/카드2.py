from collections import deque
d = deque(range(1,int(input())+1))
while len(d)>1:
    d.popleft()
    d.append(d.popleft())
print(d[0])