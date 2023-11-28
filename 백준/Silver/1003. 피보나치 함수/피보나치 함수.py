for _ in range(int(input())):
    n = int(input())
    if n:
        a0,a1,b0,b1 = 1,0,0,1
        for _ in range(2,n+1):
            a0,a1,b0,b1 = b0,b1,a0+b0,a1+b1
        print(b0,b1)
    else:
        print(1,0)