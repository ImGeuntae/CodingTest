N,K = map(int,input().split())
dp = [0]*(K+1)
for _ in range(N):
    a,b = map(int,input().split())
    dp = dp[:a] + [max(dp[x-a]+b,dp[x]) for x in range(a,K+1)]
print(dp[K])