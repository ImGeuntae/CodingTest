def solution(picks, minerals):
    minerals = minerals[:5*sum(picks)]
    L = []
    while minerals:
        s = 0
        for i in minerals[:min(5,len(minerals))]:
            if i == "diamond":
                s += 100
            elif i == "iron":
                s += 10
            else:
                s += 1
        L.append(s)
        del minerals[0:min(5,len(minerals))]
    answer = 0
    for j in sorted(L, reverse=True):
        if picks[0]:
            answer += ((j//100) + (j%100)//10 + ((j%100)%10))
            picks[0] -= 1
        elif picks[1]:
            answer += ((j//100)*5 + (j%100)//10 + ((j%100)%10))
            picks[1] -= 1
        else:
            answer += (((j//100)*25) + (((j%100)//10)*5) + ((j%100)%10))
    return answer