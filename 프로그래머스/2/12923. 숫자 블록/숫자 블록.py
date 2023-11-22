def solution(begin, end):
    answer = []
    for i in range(begin,end+1):
        ans = 1
        for x in range(2,int(i**0.5)+1):
            if i%x == 0:
                if i//x <= 1e7:
                    answer.append(i//x)
                    break
                else:
                    ans = x
        else:
            answer.append(1*(i!=1)*ans)
    return answer