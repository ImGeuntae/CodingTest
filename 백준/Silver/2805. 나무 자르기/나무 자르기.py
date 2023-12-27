N,M = map(int,input().split())
T = list(map(int,input().split()))
L,R = 0,max(T)
while L<=R:
    m = (L+R)//2
    if (s:=sum(t-m for t in T if t>m)) < M:
        R = m-1
    elif s > M:
        ans = m
        L = m+1
    else:
        ans = m
        break
print(ans)