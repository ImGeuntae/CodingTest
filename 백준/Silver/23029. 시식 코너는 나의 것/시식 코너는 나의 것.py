dp = [0]*3
for _ in range(int(input())):
    i = int(input())
    dp = dp[1]+(i//2),dp[2]+i,max(dp)
print(max(dp))