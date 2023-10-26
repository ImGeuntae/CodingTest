def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if i == len(participant)-1 or participant[i] != completion[i]:
            return participant[i]

# 메모리: 26.2 MB, 시간: 72.88 ms
