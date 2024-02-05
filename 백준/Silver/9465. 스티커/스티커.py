for _ in range(int(input())):
    n = int(input())
    a = b = c = d = 0
    S = [list(map(int,input().split())) for _ in range(2)]
    for x,y in zip(S[0],S[1]):
        a,b,c,d = c,d,max(a,b,d)+x,max(a,b,c)+y
    print(max(c,d))