def solution(progresses, speeds):
    answer = []
    for i in range(len(progresses)):
        day = -((progresses[i]-100)//speeds[i])
        if (i == 0) or (day > release):
            release = day
            answer.append(1)
        else:
            answer[-1] += 1
    return answer
