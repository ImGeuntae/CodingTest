N = int(input())
dp = [0]*(N+1)
for i in range(1,N+1):
    dp[i] = 1 + min([dp[i-(x**2)] for x in range(1,int(i**0.5)+1) if i >= x**2])
print(dp[N])