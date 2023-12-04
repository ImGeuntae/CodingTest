ans,dp = -1,1
for _ in range(int(input())):
    n = float(input())
    dp = max(n,dp*n)
    ans = max(ans,dp)
print('%0.3f'%ans)