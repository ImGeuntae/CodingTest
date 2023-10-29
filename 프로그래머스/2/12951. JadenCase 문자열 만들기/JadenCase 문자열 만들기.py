def solution(s):
    answer = ""
    for i in s:
        if i==" ":
            answer += i
        elif not answer or answer[-1]==" ":
            answer += i.upper()
        else:
            answer += i.lower()
    return answer