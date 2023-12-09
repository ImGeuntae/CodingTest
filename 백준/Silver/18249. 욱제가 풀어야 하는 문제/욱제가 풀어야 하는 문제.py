import sys
dp,a,b,n = [0]*191230,0,1,10**9+7
for i in range(191230):
    dp[i],a,b = b,b,(a+b)%n
input()
for n in sys.stdin:
    print(dp[int(n)])