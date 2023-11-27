import heapq
def solution(n, k, enemy):
    E, heap = len(enemy), enemy[:k]
    heapq.heapify(heap)
    for i in range(k,E):
        n -= heapq.heappushpop(heap,enemy[i])
        if n<0:
            return i
    return E