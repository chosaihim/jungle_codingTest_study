import sys
from collections import deque


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):

    stack = []

    boardsize = len(board)
    pop = 0

    for move in moves:
        get = 0
        for i in range(boardsize):
            if(board[i][move-1]):
                get = board[i][move-1]
                board[i][move-1] = 0
                break
        if stack and (stack[-1] == get):
            stack.pop();
            pop += 2
        elif get != 0:
            stack.append(get)
        
        # print(stack)
    
    return pop

print(solution(board, moves))