import sys
from collections import deque

board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
board_y = len(board)

# 간단한 스택 문제

cnt = 0
basket = []
for m in moves:
    for y in range(board_y):
        if board[y][m-1] != 0:
            basket.append(board[y][m-1])
            if len(basket) >= 2 and basket[-1] == basket [-2]:
                basket.pop()
                basket.pop()
                cnt+=2
            board[y][m-1] = 0
            break

print(cnt)
