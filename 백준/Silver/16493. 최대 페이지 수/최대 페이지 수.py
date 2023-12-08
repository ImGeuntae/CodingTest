N,M = map(int,input().split())
dp = [0]*(N+1)
for _ in range(M):
    d,p = map(int,input().split())
    i = N
    while i >= d:
        dp[i] = max(dp[i],p+dp[i-d])
        i -= 1
print(dp[-1])