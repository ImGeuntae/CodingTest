def solution(N, stages):
    failure = dict()
    s = len(stages)
    for i in range(1,N+1):
        n = stages.count(i)
        if s:
            failure[i] = n/s
        else:
            failure[i] = 0
        s -= n
    return [x[0] for x in sorted(failure.items(),key=lambda x:(x[1],-x[0]),reverse=True)]