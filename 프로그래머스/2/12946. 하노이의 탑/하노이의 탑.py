def Hanoi(n,a,b,c):
    return Hanoi(n-1,a,c,b) + [[a,b]] + Hanoi(n-1,c,b,a) if n else []
def solution(n):
    return Hanoi(n,1,3,2)