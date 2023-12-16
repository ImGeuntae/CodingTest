from collections import deque
import sys
d = deque()
for _ in range(int(input())):
    c = sys.stdin.readline().strip()
    if c[-1].isdigit():
        c,n = c.split()
        if c[5] == 'f':
            d.appendleft(n)
        else:
            d.append(n)
    elif c[0] == 's':
        print(len(d))
    elif c[0] == 'e':
        print(1*(len(d)==0))
    elif len(d)==0:
        print(-1)
    elif c[0] == 'f':
        print(d[0])
    elif c[0] == 'b':
        print(d[-1])
    elif c[4] == 'f':
        print(d.popleft())
    else:
        print(d.pop())