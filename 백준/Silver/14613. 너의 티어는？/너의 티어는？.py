W,L,D=map(float,input().split())
p = [W,D,L]
for n in range(2,21):
    dp = [0]*(2*n+1)
    for idx,i in enumerate(p):
        dp[idx] += i*W
        dp[idx+1] += i*D
        dp[idx+2] += i*L
    p = dp
print(format(sum(p[31:41]),'.8f'))
print(format(sum(p[21:31]),'.8f'))
print(format(sum(p[11:21]),'.8f'))
print(format(sum(p[1:11]),'.8f'))
print(format(p[0],'.8f'))