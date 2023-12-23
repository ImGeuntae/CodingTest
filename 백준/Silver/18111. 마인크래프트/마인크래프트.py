import sys
input = sys.stdin.readline
N,M,B = map(int,input().split())
L,ans = [0]*257,[100000000,0]
for _ in range(N):
    for i in input().split():
        L[int(i)] += 1
S = (sum(a*b for a,b in enumerate(L))+B)//(N*M)
for x in range(S+1):
    if (t:=sum(b*(x-a) if x>a else b*2*(a-x) for a,b in enumerate(L)))<=ans[0]:
        ans = [t,x]
print(*ans)