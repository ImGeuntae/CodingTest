from collections import defaultdict
def solution(arr):
    D = defaultdict(int)
    for i in arr:
        if i != 1:
            n=2
            d = defaultdict(int)
            while (i!=1):
                if not i%n:
                    i //= n
                    d[n] += 1
                else:
                    n += 1
            for x in d:
                D[x] = max(D[x],d[x])
    answer = 1
    for a,b in D.items():
        answer *= int(a)**int(b)
    return answer