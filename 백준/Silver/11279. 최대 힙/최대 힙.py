import heapq
import sys
input()
h = []
for i in sys.stdin:
    if (x:=int(i)):
        heapq.heappush(h,-x)
    elif h:
        print(-heapq.heappop(h))
    else:
        print(0)