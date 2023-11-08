def solution(n):
    a = b = 1
    for _ in range(1,n):
        a,b = b, a+b
    return b%1000000007