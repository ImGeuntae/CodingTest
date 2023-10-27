def solution(survey, choices):
    result = dict.fromkeys(("R","T","C","F","J","M","A","N"),0)
    for i, j in zip(survey, choices):
        s = 4-j
        if s>=0:
            C = i[0]
        elif s<0:
            C = i[1]
        result[C] += abs(s)
    answer = ""
    if result["T"] > result["R"]:
        answer += "T"
    else:
        answer += "R"
    if result["F"] > result["C"]:
        answer += "F"
    else:
        answer += "C"
    if result["M"] > result["J"]:
        answer += "M"
    else:
        answer += "J"
    if result["N"] > result["A"]:
        answer += "N"
    else:
        answer += "A"
    return answer
    