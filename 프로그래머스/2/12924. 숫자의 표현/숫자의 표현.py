def solution(n):
    div, answer = 2, 1
    while div*(div+1) <= 2*n :
        if div%2 == 0 and n%div == (div)/2:
            answer += 1
        elif div%2 == 1 and n%div == 0:
            answer += 1
        div += 1
    return answer