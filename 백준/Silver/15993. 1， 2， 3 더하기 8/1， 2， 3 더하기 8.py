import sys
dp=[(0,0) for _ in range(10**5+1)]
dp[1:4]=[(1,0),(1,1),(2,2)]
for i in range(4,10**5+1):
    a,b=zip(*dp[i-3:i])
    dp[i]=(sum(b)%(10**9+9),sum(a)%(10**9+9))
input()
for i in sys.stdin:
    print(*dp[int(i)])