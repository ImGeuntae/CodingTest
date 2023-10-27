def solution(clothes):
    dic = dict()
    for value,key in clothes:
        if key in dic:
            dic[key] += 1
        else:
            dic[key] = 2
    answer = 1
    for i in dic.values():
        answer *= i
    return answer-1