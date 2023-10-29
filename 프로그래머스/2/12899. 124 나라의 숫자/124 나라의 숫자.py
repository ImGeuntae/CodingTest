def solution(n):
    m = 1
    while (n > 3**m):
        n -= 3**m
        m += 1
    n -= 1
    result = []
    for i in range(m):
        result.append(n%3)
        n //= 3
    answer = ""
    for j in reversed(result):
        answer += str(2**j)
    return answer
    