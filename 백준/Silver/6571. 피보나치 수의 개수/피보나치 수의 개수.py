a,b = map(int,input().split())
while a+b:
    x,y,ans = 0,1,0
    while y<=b:
        x,y = y,x+y
        if a<=y<=b:
            ans += 1
    print(ans)
    a,b = map(int,input().split())