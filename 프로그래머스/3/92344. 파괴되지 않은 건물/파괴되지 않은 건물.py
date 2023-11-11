def solution(board, skill):
    m, n = len(board), len(board[0])
    X = [[0]*(n+1) for _ in range(m+1)]
    for [t, r1, c1, r2, c2, d] in skill:
        d = d*([-1,1][t-1])
        X[r1][c1] += d
        X[r1][c2+1] -= d
        X[r2+1][c1] -= d
        X[r2+1][c2+1] += d
    for j in range(m+1):
        for i in range(1,n+1):    
            X[j][i] += X[j][i-1]
    for i in range(n+1):
        for j in range(1,m+1):
            X[j][i] += X[j-1][i]
    return sum([1 if 0 < board[x][y] + X[x][y] else 0 for x in range(m) for y in range(n)])