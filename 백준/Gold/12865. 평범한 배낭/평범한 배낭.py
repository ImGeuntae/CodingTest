N,K = map(int,input().split())
dp = [0]*(K+1)
for _ in range(N):
    a,b = map(int,input().split())
    dp = [dp[x] if a>x else max(dp[x-a]+b,dp[x]) for x in range(K+1)]
print(dp[-1])