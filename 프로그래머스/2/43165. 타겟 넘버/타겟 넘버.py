def solution(numbers, target):
    N = [0]
    for num in numbers:
        nn = []
        for n in N:
            nn.append(n + num)
            nn.append(n - num)
        N = nn
    return N.count(target)

###########################################

from collections import defaultdict as dd
def solution(numbers, target):
    N = [0]
    D = dd(int)
    D[0] = 1
    for num in numbers:
        s,d = set(), dd(int)
        for n in N:
            s.add(n+num)
            s.add(n-num)
            d[n+num] += D[n]
            d[n-num] += D[n]
        N,D = s,d
    return D[target]
