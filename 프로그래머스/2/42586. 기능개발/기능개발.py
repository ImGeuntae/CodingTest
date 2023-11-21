def solution(progresses, speeds):
    day, answer = 0, []
    for i in range(len(progresses)):
        release = -((progresses[i]-100)//speeds[i])
        if release > day:
            day = release
            answer.append(1)
        else:
            answer[-1] += 1
    return answer
