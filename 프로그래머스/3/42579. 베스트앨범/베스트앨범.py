from collections import defaultdict as dd
def solution(genres, plays):
    D = dd(dict)
    for idx, (g,p) in enumerate(zip(genres, plays)):
        D[g][idx] = p
    G = sorted(D, key=lambda x : sum((D[x]).values()), reverse=True)
    L = [sorted(D[i],key=lambda x : D[i][x], reverse=True)[:min(2,len(D[i]))] for i in G]
    return [N for M in L for N in M]