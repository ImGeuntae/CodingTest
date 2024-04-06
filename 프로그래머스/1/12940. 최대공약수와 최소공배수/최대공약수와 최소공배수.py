def solution(n, m):
    x = n*m
    while (n%m and n):
        n,m = m,n%m
    return [m,x/m]