for _ in range(int(input())):
    M,N,x,y = map(int,input().split())
    if x>y:
        M,N,x,y = N,M,y,x
    ans,n = x,M-N-1
    a,b = M,N
    while b>0:
        a,b = b,a%b
    a = M*N//a
    while x!=y:
        x = (x+n)%N+1
        ans += M
        if ans > a:
            ans = -1
            break
    print(ans)