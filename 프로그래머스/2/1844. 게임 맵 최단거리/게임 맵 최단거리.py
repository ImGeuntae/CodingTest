def solution(maps):
    n,m = len(maps),len(maps[0])
    queue = [(0,0)]
    d = [(1,0),(-1,0),(0,1),(0,-1)]
    while queue:
        x,y = queue.pop(0)
        for i in range(4):
            xx,yy = x+d[i][0], y+d[i][1]
            if 0<=xx<=n-1 and 0<=yy<=m-1 and maps[xx][yy] == 1:
                maps[xx][yy] += maps[x][y]
                queue.append((xx,yy))
    return maps[n-1][m-1] if maps[n-1][m-1] != 1 else -1