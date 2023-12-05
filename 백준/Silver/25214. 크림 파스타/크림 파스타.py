import sys
input()
m,ans,dp = 1e9,0,[]
for n in map(int,sys.stdin.readline().split()):
    m = min(m,n)
    ans = max(ans,n-m)
    dp.append(ans)
print(*dp)