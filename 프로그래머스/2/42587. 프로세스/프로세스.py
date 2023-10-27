def solution(priorities, location):
    que = list(range(len(priorities)))
    answer = 1
    while True:
        n = priorities[0]
        if [x for x in priorities[1:] if x>n]:
            priorities.append(n)
            que.append(que[0])
            priorities.pop(0)
            que.pop(0)
        else:
            if que[0]==location:
                return answer
                break
            priorities.pop(0)
            que.pop(0)
            answer += 1