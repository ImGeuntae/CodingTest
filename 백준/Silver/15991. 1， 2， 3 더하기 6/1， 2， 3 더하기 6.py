dp=[1,1,2,2,3,3]
for i in range(6,10**5+1):
    dp += [(dp[i-2]+dp[i-4]+dp[i-6])%(10**9+9)]
for _ in range(int(input())):
    print(dp[int(input())])