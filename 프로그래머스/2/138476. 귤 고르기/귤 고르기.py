def solution(k, tangerine):
    dic = dict.fromkeys(tangerine,0)
    for i in tangerine:
        dic[i] += 1
    L = sorted(dic,key=lambda x:dic[x])
    for _ in range(len(tangerine)-k):
        dic[L[0]] -= 1
        if dic[L[0]] == 0:
            L.pop(0)
    return len(L)