def solution(name, yearning, photo):
    dic = {name: yearning for name, yearning in zip(name, yearning)}
    answer = []
    for i in photo:
        n = 0
        for j in i:
            n += int(dic.get(j,0))
        answer.append(n)
    return answer