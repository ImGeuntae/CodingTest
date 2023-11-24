def solution(n, roads, sources, destination):
    T = {k: [] for k in range(1,n+1)}
    for a,b in roads:
        T[a].append(b)
        T[b].append(a)
    D,m,q,step = dict(),[destination],[],0
    while m:
        for i in m:
            if i not in D:
                D[i] = step
                q.extend(T[i])
        step += 1
        m,q = q,[]
    return [D[x] if x in D else -1 for x in sources]