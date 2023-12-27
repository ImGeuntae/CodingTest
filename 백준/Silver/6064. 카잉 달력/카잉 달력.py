for _ in range(int(input())):
    M,N,x,y = map(int,input().split())
    a,b = M,N
    while b>0:
        a,b = b,a%b
    a = M*N//a
    while x<=a:
        if (x-y)%N:
            x += M
        else:
            print(x)
            break
    else:
        print(-1)