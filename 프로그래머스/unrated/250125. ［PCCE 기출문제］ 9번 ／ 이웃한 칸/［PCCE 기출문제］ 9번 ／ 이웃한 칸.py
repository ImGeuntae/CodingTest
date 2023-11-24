def solution(board, h, w):
    ans,n,m = 0,len(board),len(board[0])
    for x,y in [(1,0),(-1,0),(0,1),(0,-1)]:
        if 0 <= h+x < n and 0 <= w+y < m and board[h+x][w+y] == board[h][w]:
            ans += 1
    return ans