for _ in range(int(input())):
    input()
    a = b = 0
    S = [list(map(int,input().split())) for _ in range(2)]
    for x,y in zip(S[0],S[1]):
        a,b, = max(a,b+x),max(b,a+y)
    print(max(a,b))