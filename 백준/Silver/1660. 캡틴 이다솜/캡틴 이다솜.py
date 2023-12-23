N = int(input())
dp,n,L = [0]*(N+1),2,[1]
while L[-1]<=N:
    L += [L[-1]+n*(n+1)//2]
    n += 1
    for i in range(L[-2],min(L[-1],N+1)):
        dp[i] = min([dp[i-x] for x in L[:-1]]) + 1
print(dp[N])