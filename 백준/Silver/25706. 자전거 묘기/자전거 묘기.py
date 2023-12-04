import sys
N = int(input())
dp = list(map(int,sys.stdin.readline().split()))+[0]
for i in range(N-1,-1,-1):
    dp[i] = 1+dp[min(i+dp[i]+1,N)]
print(*dp[:-1])