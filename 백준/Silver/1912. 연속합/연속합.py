import sys
input()
ans,dp = -1000,0
for n in map(int,sys.stdin.readline().split()):
    dp = max(n+dp,n)
    ans = max(ans,dp)
print(ans)