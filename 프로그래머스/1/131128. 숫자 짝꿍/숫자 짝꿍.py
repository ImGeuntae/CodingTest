def solution(X, Y):
    Xdict,Ydict = dict.fromkeys(range(10),0),dict.fromkeys(range(10),0)
    for i in X:
        Xdict[int(i)] += 1
    for j in Y:
        Ydict[int(j)] += 1
    answer = ""
    for k in range(9,-1,-1):
        answer += str(k)*min(Xdict[k],Ydict[k])
    if not answer:
        return "-1"
    elif answer[0]=="0":
        return "0"
    else:
        return answer
    