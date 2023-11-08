def solution(n):
    if n < 3:
        return n
    else:
        a,b = 1,2
        for _ in range(2,n):
            a,b = b, a+b
        return b%1000000007