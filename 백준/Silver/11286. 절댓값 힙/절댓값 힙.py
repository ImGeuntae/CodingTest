import sys
import heapq
input()
h = []
for i in sys.stdin:
    if (i:=int(i)):
        heapq.heappush(h,(abs(i),i))
    else:
        print(heapq.heappop(h)[1] if h else 0)