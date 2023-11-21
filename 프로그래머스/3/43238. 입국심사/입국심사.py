def solution(n, times):
    m, M = 1, max(times)*n
    while m <= M:
        t = (M+m)//2
        s = sum([t//i for i in times])
        if s >= n:
            ans = t
            M = t-1
        else:
            m = t+1
    return ans