def solution(ingredient):
    L = []
    answer = 0
    for i in ingredient:
        L.append(i)
        if L[-4:]==[1,2,3,1]:
            answer += 1
            del L[-4:]
    return answer