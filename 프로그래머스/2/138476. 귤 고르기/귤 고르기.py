def solution(k, tangerine):
    dic = dict.fromkeys(tangerine,0)
    for i in tangerine:
        dic[i] += 1
    L = sorted(dic,key=lambda x:dic[x],reverse=True)
    j = 0
    while k>0:
        k -= dic[L[j]]
        j += 1
    return j