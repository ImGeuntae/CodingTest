from collections import deque
def solution(stones, k):
    d = deque()
    ans = float("inf")
    for idx,i in enumerate(stones):
        while d and d[-1][0] < i:
            d.pop()
        d.append((i,idx))
        if d[0][1] == idx-k:
            d.popleft()
        if idx >= k-1 and ans > d[0][0]:
            ans = d[0][0]
    return ans
