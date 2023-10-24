def solution(wallpaper):
    L = U = 50
    R = D = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[i])):
            if wallpaper[i][j] == "#":
                L = min(L,j)
                R = max(R,j+1)
                U = min(U,i)
                D = max(D,i+1)
    return [U,L,D,R]