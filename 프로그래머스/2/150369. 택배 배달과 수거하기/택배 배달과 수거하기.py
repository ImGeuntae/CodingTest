from collections import deque
def solution(cap, n, deliveries, pickups):
    d = p = ans = 0
    D,P = deque(), deque()
    for idx, (a,b) in enumerate(zip(deliveries[::-1],pickups[::-1])):
        d -= a
        p -= b
        while d < 0:
            D.append(n-idx)
            d += cap
        while p < 0:
            P.append(n-idx)
            p += cap
    for _ in range(min(len(D),len(P))):
        ans += max(D.popleft(),P.popleft())
    return 2*(ans+sum(D)+sum(P))