from collections import deque
def solution(n, results):
    win, lose = [set() for _ in range(n+1)], [set() for _ in range(n+1)]
    for a,b in results:
        win[a].add(b)
        lose[b].add(a)
    for x in 2*list(range(1,n+1)):
        for w in win[x]:
            for ww in win[w]:
                lose[ww].add(x)
        for l in lose[x]:
            for ll in lose[l]:
                win[ll].add(x)
    ans = 0
    for w,l in zip(win,lose):
        if len(w) + len(l) == n-1:
            ans += 1
    return ans