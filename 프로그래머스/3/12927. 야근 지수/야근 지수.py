from collections import defaultdict
def solution(n, works):
    dic = defaultdict(int)
    for i in works:
        dic[i] += 1
    L = max(dic)
    while n>0 and L:
        if n > dic[L]:
            n -= dic[L]
            dic[L-1] += dic[L]
            del dic[L]
        else:
            dic[L] -= n
            dic[L-1] += n
            n = 0
        L -= 1
    return sum([n*(m**2) for m,n in dic.items()])