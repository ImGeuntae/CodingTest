N,K = map(int,input().split())
dp = [0]*(K+1)
for _ in range(N):
    a,b = map(int,input().split())
    for x in range(K,a-1,-1):
        dp[x] = max(dp[x],dp[x-a]+b)
print(dp[-1])