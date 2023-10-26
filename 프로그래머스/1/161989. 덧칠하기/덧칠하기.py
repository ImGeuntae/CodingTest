def solution(n, m, section):
    painted = 0
    answer = 0
    for i in section:
        if i > painted:
            answer += 1
            painted = i+(m-1)
    return answer