def solution(s):
    dic = dict()
    answer = list()
    for idx,i in enumerate(s):
        if i not in dic:
            answer.append(-1)
        else:
            answer.append(idx - dic[i])
        dic[i] = idx
    return answer