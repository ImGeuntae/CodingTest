N,M = map(int,input().split())
dp = [0]*(N+1)
for _ in range(M):
    d,p = map(int,input().split())
    for i in range(N,d-1,-1):
        dp[i] = max(dp[i],p+dp[i-d])
print(dp[-1])