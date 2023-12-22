N,M = map(int,input().split())
dp = [[[0,0] for _ in range(M-7)] for _ in range(N-7)]
for i in range(N):
    for j,n in enumerate(input()):
        for x in range(max(0,i-7),min(N-7,i+1)):
            for y in range(max(0,j-7),min(M-7,j+1)):
                dp[x][y][(n=='B')-((i-x)+(j-y))%2] += 1
print(min(min(min(y) for y in x) for x in dp))