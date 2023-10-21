def solution(citations):
    citations.sort(reverse=True)
    for idx, i in enumerate(citations):
        if (i < (idx+1)):
            return idx
    return idx+1