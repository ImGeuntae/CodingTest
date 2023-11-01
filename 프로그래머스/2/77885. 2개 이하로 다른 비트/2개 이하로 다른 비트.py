def solution(numbers):
    answer = []
    for i in numbers:
        if i%2:
            x = "0"+str(format(i, 'b'))
            idx = x.rfind("01")
            answer.append(int(x[:idx]+"10"+x[idx+2:],2))
        else:
            answer.append(i+1)
    return answer