N = int(input())
H = [input().split() for _ in range(N)]
dp = [[[0,0,0] for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1
for i in range(N):
    for j in range(2,N):
        if H[i][j] == '0':
            dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
            if H[i][j-1] == H[i-1][j] == '0':
                dp[i][j][2] = sum(dp[i-1][j-1])
print(sum(dp[-1][-1]))