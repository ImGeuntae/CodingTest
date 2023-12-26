import sys
import heapq
input()
h = []
for i in sys.stdin:
    if (i:=int(i)):
        heapq.heappush(h,i)
    elif h:
        print(heapq.heappop(h))
    else:
        print(0)