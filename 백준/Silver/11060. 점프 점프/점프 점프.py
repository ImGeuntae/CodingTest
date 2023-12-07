input()
dp = [0]+[-1]*1100
for idx,i in enumerate(map(int,input().split())):
    if dp[idx]>=0:
        for j in range(idx+1,idx+1+i):
            if dp[j] == -1:
                dp[j] = dp[idx]+1
            else:
                dp[j] = min(dp[j],dp[idx]+1)
print(dp[idx])