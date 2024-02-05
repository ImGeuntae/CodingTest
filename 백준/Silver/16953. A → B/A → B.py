from collections import deque
A,B = map(int,input().split())
Q = deque([(A,1)])
S = {A}
while Q:
    n,x = Q.popleft()
    if n==B:
        print(x)
        break
    else:
        for a in [n*2,n*10+1]:
            if a not in S and a<=B:
                S.add(a)
                Q += [(a,x+1)]
else:
    print(-1)