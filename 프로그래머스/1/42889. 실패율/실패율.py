def solution(N, stages):
    clear = dict.fromkeys(range(1,N+1),0)
    for i in stages:
        if i <= N:
            clear[i] += 1
    s = len(stages)
    for j in range(1,N+1):
        if s:
            s, clear[j] = s-clear[j], clear[j]/s
        else:
            clear[j] = 0
    return sorted(clear, key=lambda x : clear[x], reverse=True)
