import sys
dp,a,b=[0]*251,0,1
for i in range(251):
    dp[i],a,b = b,b,2*a+b
[print(dp[int(n)]) for n in sys.stdin]