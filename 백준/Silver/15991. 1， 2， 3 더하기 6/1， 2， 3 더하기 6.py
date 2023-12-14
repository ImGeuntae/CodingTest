dp=[0]*(10**5+2)
a,b,c=0,1,0
for i in range(0,10**5+1,2):
    a,b,c=b,c,a+b+c
    dp[i]=dp[i+1]=c%(10**9+9)
for _ in range(int(input())):
    print(dp[int(input())])