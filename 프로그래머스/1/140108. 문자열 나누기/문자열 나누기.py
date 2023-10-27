def solution(s):
    answer = 0
    s = list(s)
    while s:
        count = [0,0]
        for i in range(len(s)):
            if s[i] == s[0]:
                count[0] += 1
            else:
                count[1] += 1
            if (count[0] == count[1]) or (i == len(s)-1):
                answer += 1
                del s[:i+1]
                break
    return answer