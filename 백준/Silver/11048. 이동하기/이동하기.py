import sys
N,M = map(int,input().split())
dp = [[0]*(M+1) for _ in range(N+1)]
for n in range(1,N+1):
    for m,x in zip(range(1,M+1),map(int,sys.stdin.readline().split())):
        dp[n][m] = x + max(dp[n-1][m],dp[n][m-1])
print(dp[N][M])