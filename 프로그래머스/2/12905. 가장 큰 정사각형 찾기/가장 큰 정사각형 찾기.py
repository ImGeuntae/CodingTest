def solution(board):
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if (board[i][j]):
                board[i][j] = min(board[i-1][j-1],board[i-1][j],board[i][j-1]) + 1
    return (max([max(b) for b in board]))**2