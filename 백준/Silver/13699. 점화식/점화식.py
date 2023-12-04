dp = [1]
for i in range(1,int(input())+1):
    dp.append(sum([dp[j]*dp[-1-j] for j in range(i)]))
print(dp[-1])