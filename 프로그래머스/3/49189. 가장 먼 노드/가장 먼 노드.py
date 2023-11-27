def solution(n, edge):
    D = {k: [] for k in range(1,n+1)}    
    for a,b in edge:
        D[a].append(b)
        D[b].append(a)
    queue,F,d,tmp = [1], dict(), 0, []
    while queue:
        for q in queue:
            if q not in F:
                F[q] = d
                tmp.extend(D[q])
        queue,tmp = tmp,[]
        d += 1
    return sum([1 for x in range(2,n+1) if F[x] == max(F.values())])