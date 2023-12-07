dp = [0]+[1]+[2]+[4]+[0]*999997
for i in range(4,1000001):
    dp[i] = (sum(dp[i-3:i]))%(10**9+9)
for _ in range(int(input())):
    print(dp[int(input())])