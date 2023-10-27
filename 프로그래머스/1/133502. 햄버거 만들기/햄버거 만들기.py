def solution(ingredient):
    L = []
    answer = 0
    for i in ingredient:
        L.append(i)
        if len(L)>=4 and L[-4:]==[1,2,3,1]:
            answer += 1
            del L[-4:]
    return answer