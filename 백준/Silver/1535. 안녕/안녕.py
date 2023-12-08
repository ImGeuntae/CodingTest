dp = [[0]*101 for _ in range(int(input())+1)]
for idx,(L,J) in enumerate(zip(map(int,input().split()),map(int,input().split())),start=1):
    for i in range(1,101):
        if i <= L:
            dp[idx][i] = dp[idx-1][i]
        else:
            dp[idx][i] = max(dp[idx-1][i],J+dp[idx-1][i-L])
print(dp[-1][100])