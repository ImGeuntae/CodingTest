def solution(n):
    x = 2
    while True:
        if n%x == 1:
            return x
            break
        x += 1