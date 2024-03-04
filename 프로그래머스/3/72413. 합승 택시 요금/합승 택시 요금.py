def solution(n, s, a, b, fares):
    answer = 0
    F_W = [[0 if i==j else float("inf") for j in range(n+1)] for i in range(n+1)]
    route = [[] for _ in range(n+1)]
    for x,y,z in fares:
        F_W[x][y] = z
        F_W[y][x] = z
    for j in range(1,n+1):
        for i in range(1,n+1):
            for k in range(1,n+1):
                F_W[i][k] = min(F_W[i][k],F_W[i][j]+F_W[j][k])
    return min(F_W[s][i] + F_W[i][a] + F_W[i][b] for i in range(1,n+1))