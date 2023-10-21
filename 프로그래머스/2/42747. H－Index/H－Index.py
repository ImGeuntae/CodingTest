def solution(citations):
    citations.sort(reverse=True)
    answer = -1
    for idx, i in enumerate(citations):
        if (i < (idx+1)):
            answer = idx
            break
    if answer == -1:
        answer = idx+1
    return answer