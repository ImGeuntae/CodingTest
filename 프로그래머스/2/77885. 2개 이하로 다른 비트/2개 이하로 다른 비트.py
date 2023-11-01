def solution(numbers):
    answer = []
    for i in numbers:
        x = "0"+str(format(i, 'b'))
        if x[-1]=="0":
            answer.append(i+1)
        else:
            idx = x.rfind("01")
            answer.append(int(x[:idx]+"10"+x[idx+2:],2))
    return answer