def solution(arr):
    D = {}
    for i in arr:
        if i != 1:
            n=2
            d = {}
            while (i!=1):
                if not i%n:
                    i //= n
                    if n in d:
                        d[n] += 1
                    else:
                        d[n] = 1
                else:
                    n += 1
            
            for x in d:
                if x in D:
                    D[x] = max(D[x],d[x])
                else:
                    D[x] = d[x]
    answer = 1
    for a,b in D.items():
        answer *= int(a)**int(b)
    return answer