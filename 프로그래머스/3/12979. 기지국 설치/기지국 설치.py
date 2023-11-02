def solution(n, stations, w):
    answer, p = 0, 1
    for x in stations:
        answer -= (p-x+w)//(2*w+1)
        p = x+w+1
    return answer-((p-1-n)//(2*w+1))