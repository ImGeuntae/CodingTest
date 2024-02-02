N = int(input())
DP = [[0]*3 for _ in range(2)]
for _ in range(N):
    X = list(map(int,input().split()))
    M = []
    for i in range(3):
        a,b = 0+(i>1),2+(i>0)
        M += [(min(DP[0][a:b]),max(DP[1][a:b]))]
    for i in range(3):
        for j in range(2):
            DP[j][i] = X[i] + M[i][j]
print(max(DP[1]))
print(min(DP[0]))