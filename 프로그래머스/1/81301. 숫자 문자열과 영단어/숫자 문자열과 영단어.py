def solution(s):
    answer = number = ""
    eng = ["zero","one","two","three","four","five","six","seven","eight","nine"]
    for i in s:
        if i.isalpha():
            number += i
            if number in eng:
                answer += str(eng.index(number))
                number = ""
        else:
            answer += i
    return int(answer)