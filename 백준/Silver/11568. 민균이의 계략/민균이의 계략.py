N = int(input())
dp = []
for n in map(int,input().split()):
    for [a,b] in dp:
        if n>a:
            idx = 0
            while b+1 < dp[idx][1]:
                idx += 1
            dp.insert(idx,[n,b+1])
            break
    else:
        dp.append([n,1])
print(dp[0][1])