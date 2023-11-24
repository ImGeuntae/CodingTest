import heapq
def solution(n, k, enemy):
    heap = enemy[:k]
    heapq.heapify(heap)
    for i in range(k,len(enemy)):
        n -= heapq.heappushpop(heap,enemy[i])
        if n<0:
            return i
    return len(enemy)