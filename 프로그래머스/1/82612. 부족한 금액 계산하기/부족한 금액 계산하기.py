def solution(price, money, count):
    answer = (((count*(count+1))/2)*price) - money
    if answer > 0:
        return answer
    else:
        return 0