def F(p,w,b):
    if (n:=len(p))>1:
        if (s:=sum(map(sum,p))) == n*n:
            b += 1
        elif s == 0:
            w += 1
        else:
            for x1,x2,y1,y2 in [(0,n//2,0,n//2),(n//2,n,0,n//2),(0,n//2,n//2,n),(n//2,n,n//2,n)]:
                q = [Q[x1:x2] for Q in p[y1:y2]]
                x,y = F(q,0,0)
                w,b = w+x,b+y
    elif p[0][0]:
        b += 1
    else:
        w += 1
    return w,b

N = int(input())
P = [list(map(int,input().split())) for _ in range(N)]
print(*F(P,0,0))