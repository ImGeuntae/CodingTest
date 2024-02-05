dp = [0]*2
for i in range(int(input())):
    dp = [0]+[max(dp[n:n+2])+int(x) for n,x in zip(range(i+1),input().split())]+[0]
print(max(dp))