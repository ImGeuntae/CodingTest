def solution(d, budget):
    d.sort()
    answer = 0
    while d and budget >= d[0]:
        budget -= d.pop(0)
        answer += 1
    return answer