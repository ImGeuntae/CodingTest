import heapq
def solution(n, k, enemy):
    if len(enemy) < k:
        return len(enemy)
    ans,heap = k,enemy[:k]
    heapq.heapify(heap)
    for i in enemy[k:]:
        n -= heapq.heappushpop(heap,enemy[ans])
        if n<0:
            break
        else:
            ans += 1
    return ans