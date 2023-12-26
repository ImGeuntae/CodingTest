import sys
import heapq
input()
h = []
for i in sys.stdin:
    if (i:=int(i)):
        heapq.heappush(h,i)
    else:
        print(heapq.heappop(h) if h else 0)