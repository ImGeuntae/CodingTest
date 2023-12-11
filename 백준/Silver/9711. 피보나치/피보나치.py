dp,a,b = [0]*10001,0,1
for i in range(1,10001):
    dp[i],a,b=b,b,a+b
for i in range(int(input())):
    p,q = map(int,input().split())
    print("Case #{}: {}".format(i+1,dp[p]%q))