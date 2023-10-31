import sys
board = list(map(int,sys.stdin.read().split()))
n = max(board)
x = board.index(n)
print(n)
print(x//9+1,x%9+1)