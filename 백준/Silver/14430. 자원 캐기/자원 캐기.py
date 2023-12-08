N,M = map(int,input().split())
dp = [0]*(M+1)
for _ in range(N):
    for idx,i in enumerate(map(int,input().split()),start=1):
        dp[idx] = i + max(dp[idx],dp[idx-1])
print(dp[-1])