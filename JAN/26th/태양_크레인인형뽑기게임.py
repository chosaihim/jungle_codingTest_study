import sys
debug = True
board, moves = [], []
if debug :
    board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
    moves = [1,5,3,5,1,2,1,4]

def solution(board, moves) :
    answer = 0
    baguni = []
    for mov in moves :
        for i in range(len(board)) :
            b = board[i][mov - 1]
            if b != 0 :
                if len(baguni) > 0 and baguni[-1] == b :
                    print(b)
                    baguni.pop()
                    answer += 2
                else :
                    baguni.append(b)
                board[i][mov-1] = 0
                break
    return answer

print(solution(board, moves))
