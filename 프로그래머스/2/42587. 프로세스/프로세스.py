def solution(priorities, location):
    answer = 0
    search = sorted(priorities, reverse=True)
    while True:
        for i, priority in enumerate(priorities):
            s = search[answer]
            if priority == s:
                answer += 1
                if i == location:
                    return answer