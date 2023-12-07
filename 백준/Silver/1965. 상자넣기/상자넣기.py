n = int(input())
box = [0]+list(map(int,input().split()))
dp,ans = [0]+[1]*n,0
for i in range(1,n+1):
    dp[i] += max(dp[j] for j in range(i-1,-1,-1) if box[i] > box[j])
    ans = max(ans,dp[i])
print(ans)