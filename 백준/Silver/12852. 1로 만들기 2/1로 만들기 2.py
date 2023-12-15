n=int(input())
dp=list(range(-1,n*3+1))
for i in range(1,n+1):
    dp[i*2]=min(dp[i*2],dp[i]+1)
    dp[i*3]=min(dp[i*3],dp[i]+1)
    dp[i+1]=min(dp[i+1],dp[i]+1)
print(dp[n])
for _ in range(dp[n]+1):
    print(n, end=' ')
    if dp[n]-1 == dp[n-1]:
        n -= 1
    elif n%2==0 and dp[n]-1 == dp[n//2]:
        n //= 2
    else:
        n //= 3