def solution(board, moves):
    busket = []
    answer = 0
    for i in moves:
        m = 0
        while m < len(board):
            if board[m][i-1]:
                busket.append(board[m][i-1])
                board[m][i-1] = 0
                break
            m += 1
        if len(busket) >= 2 and busket[-1] == busket[-2]:
            answer += 2
            del busket[-2:]
    return answer