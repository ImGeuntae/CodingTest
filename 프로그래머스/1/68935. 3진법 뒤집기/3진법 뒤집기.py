def solution(n):
    answer = ""
    while n>=1:
        n, m = divmod(n,3)
        answer += str(m)
    return int(answer,3)