def solution(m, n, board):
    B = list(map(list,(zip(*[list(b) for b in board][::-1]))))
    bomb = True
    ans = 0
    while bomb:
        bomb = set()
        for i in range(n-1):
            for j in range(m-1):
                try:
                    if (B[i][j] == B[i][j+1] == B[i+1][j] == B[i+1][j+1]):
                        bomb.update([(i,j),(i,j+1),(i+1,j),(i+1,j+1)])
                except:
                    continue
        for (x,y) in sorted(list(bomb), key=lambda x:-x[1]):
            B[x].pop(y)
            ans += 1
    return ans