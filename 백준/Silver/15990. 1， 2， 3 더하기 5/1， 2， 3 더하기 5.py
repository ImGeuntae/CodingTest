dp = [[0]*3 for _ in range(10**5+1)]
dp[1],dp[2],dp[3] = [1,0,0],[0,1,0],[1,1,1]
for i in range(4,10**5+1):
    dp[i] = [(sum(dp[i-n-1])-dp[i-n-1][n])%(10**9+9) for n in range(3)]
for _ in range(int(input())):
    print(sum(dp[int(input())])%(10**9+9))