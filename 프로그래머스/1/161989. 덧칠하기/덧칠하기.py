def solution(n, m, section):
    wall = set()
    answer = 0
    for i in section:
        if i not in wall:
            answer += 1
            for j in range(m):
                wall.add(i+j)
    return answer