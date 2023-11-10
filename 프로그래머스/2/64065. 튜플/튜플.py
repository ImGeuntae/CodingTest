def solution(s):
    L = [i.split(",") for i in s[2:-2].split("},{")]
    L.sort(key = lambda x:len(x))
    ans = []
    for i in L:
        ans.extend([int(n) for n in i if int(n) not in ans])
    return ans