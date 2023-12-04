N = int(input())
dp = [0]*(N+1)
for i in range(1,N+1):
    j = i//2
    dp[i] = j*(i-j) + dp[j] + dp[i-j]
print(dp[-1])