def solution(s):
    answer = ""
    idx = 0
    for x in s:
        if x == " ":
            idx = 0
            answer += " "
        else:
            if idx%2:
                answer += x.lower()
            else:
                answer += x.upper()
            idx += 1
    return answer