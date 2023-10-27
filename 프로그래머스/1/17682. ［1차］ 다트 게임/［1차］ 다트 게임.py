def solution(dartResult):
    bonus = ["S","D","T"]
    answer = []
    number = ""
    for i in dartResult:
        if i.isdigit():
            number += i
        elif i.isalpha():
            n = (bonus.index(i))+1
            answer.append(int(number)**n)
            number = ""
        else:
            if i == "*":
                answer[-1] *= 2
                if len(answer) >= 2:
                    answer[-2] *= 2
            else:
                answer[-1] *= -1
    return sum(answer)