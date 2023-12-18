import sys
dp = [0]*3
input()
for i in map(int,sys.stdin):
    dp = dp[1]+(i//2),dp[2]+i,max(dp)
print(max(dp))