import sys
N,M=map(int,input().split())
dp=[[0]*(M+1) for _ in range(N+1)]
for i in range(1,N+1):
    for n,j in zip(map(int,sys.stdin.readline().split()),range(1,M+1)):
        dp[i][j] = n+dp[i][j-1]
for i in range(1,N+1):
    for j in range(1,M+1):
        dp[i][j] += dp[i-1][j]
for _ in range(int(input())):
    a,b,c,d = map(int,sys.stdin.readline().split())
    print(dp[c][d]-dp[a-1][d]-dp[c][b-1]+dp[a-1][b-1])