from collections import deque
import sys
d = deque()
input()
for c in sys.stdin:
    c = c.strip()
    if c[1] == 'u':
        *_,n = c.split()
        d.append(n)
    elif c[0] == 's':
        print(len(d))
    elif c[0] == 'e':
        print(1*(len(d)==0))
    elif len(d)==0:
        print(-1)
    elif c[0] == 'p':
        print(d.popleft())
    elif c[0] == 'f':
        print(d[0])
    else:
        print(d[-1])