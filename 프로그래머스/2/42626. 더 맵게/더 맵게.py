from heapq import heappush, heappop, heapify
def solution(scoville, K):
    heapify(scoville)
    answer = 0
    while scoville[0] < K and len(scoville) > 1:
        heappush(scoville, heappop(scoville) + heappop(scoville)*2)
        answer += 1
    return answer if scoville[0] >= K else -1