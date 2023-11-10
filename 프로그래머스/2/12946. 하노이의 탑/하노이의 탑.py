def Hanoi(n,a,b,c):
    return [a,b] if n == 1 else Hanoi(n-1,a,c,b)+[a,b]+Hanoi(n-1,c,b,a)
def solution(n):
    H = Hanoi(n,1,3,2)
    return [[x,y] for x,y in zip(H[0::2],H[1::2])]