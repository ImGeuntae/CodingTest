def solution(progresses, speeds):
    l = []
    for i in range(len(progresses)):
        num = (100 - progresses[i])/speeds[i]
        if int(num) != num:
            num = int(num)+1
        l.append(num)
    answer = []
    day = l[0]
    count = 1
    for j in range(1,len(l)):
        if l[j] > day:
            day = l[j]
            answer.append(count)
            count = 0
        count += 1
    answer.append(count)
    return answer