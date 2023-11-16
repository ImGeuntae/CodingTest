def solution(keymap, targets):
    ans, D = list(), dict()
    for k in keymap:
        for idx, s in enumerate(k,start=1):
            if s not in D or idx < D[s]:
                D[s] = idx
    for t in targets:
        try:
            ans.append(sum([D[x] for x in t]))
        except:
            ans.append(-1)
    return ans