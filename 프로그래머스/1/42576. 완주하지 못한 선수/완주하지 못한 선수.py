def solution(participant, completion):
    h = sum([hash(i) for i in participant]) - sum([hash(j) for j in completion])
    return [k for k in participant if hash(k)==h][0]





# hash 미사용

def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant)-1 or participant[i] != completion[i]:
            return participant[i]

# 메모리: 26.2 MB, 시간: 72.88 ms
