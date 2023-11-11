def solution(scores):
    w = sum(scores[0])
    s = ans = 0
    for i in sorted(scores, key=lambda x:(-x[0],x[1])):
        if i[1] >= s:
            s = i[1]
            if sum(i) > w:
                ans += 1
        elif i == scores[0]:
            return -1
    return ans+1