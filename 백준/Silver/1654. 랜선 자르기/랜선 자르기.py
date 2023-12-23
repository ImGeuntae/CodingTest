import sys
N,K = map(int,input().split())
X = [int(i) for i in sys.stdin]
L,R = 1,max(X)
while L<=R:
    M = (L+R)//2
    if sum(n//M for n in X) < K:
        R = M-1
    else:
        ans = M
        L = M+1
print(ans)