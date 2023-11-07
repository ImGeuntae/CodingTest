from collections import defaultdict as dd
from itertools import combinations as c
def solution(orders, course):
    answer = []
    for n in course:
        dic = dd(int)
        for o in orders:
            if len(o) < n:
                continue
            o = sorted(o)
            for m in c(o,n):
                dic[''.join(m)] += 1
        answer.extend([k for k,v in dic.items() if v != 1 and v == max(dic.values())])
    return sorted(answer)