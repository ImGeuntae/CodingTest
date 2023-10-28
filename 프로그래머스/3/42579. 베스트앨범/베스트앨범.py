def solution(genres, plays):
    g_dict = dict.fromkeys(genres)
    for i in g_dict:
        g_dict[i] = {}
    for idx, (g,p) in enumerate(zip(genres, plays)):
        g_dict[g][idx] = p
    g_list = sorted(g_dict, key=lambda x : sum((g_dict[x]).values()), reverse=True)
    L = [sorted(g_dict[i],key=lambda x : g_dict[i][x], reverse=True)[:min(2,len(g_dict[i]))] for i in g_list]
    return [N for M in L for N in M]
        
