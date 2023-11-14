import heapq
n, heap, ans = int(input()), [], 0
for x in range(n):
    heapq.heappush(heap,int(input()))
for _ in range(n-1):
    n = heapq.heappop(heap) + heapq.heappop(heap)
    heapq.heappush(heap,n)
    ans += n
print(ans)