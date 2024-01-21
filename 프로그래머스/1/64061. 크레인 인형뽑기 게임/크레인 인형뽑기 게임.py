def solution(board, moves):
    board = [[bb for bb in b if bb] for b in zip(*board[::-1])]
    busket = [-1]
    answer = 0
    for m in moves:
        if board[m-1]:
            busket += [board[m-1].pop()]
            if busket[-1] == busket[-2]:
                del busket[-2:]
                answer += 2
    return answer