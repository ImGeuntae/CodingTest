def solution(numbers):
    numbers = sorted(numbers, key=lambda x:str(x)*3, reverse=True)
    answer = ''.join(list(map(str,numbers)))
    return answer if int(answer) else "0"