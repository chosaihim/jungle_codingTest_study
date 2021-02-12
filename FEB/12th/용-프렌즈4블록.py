# https://programmers.co.kr/learn/courses/30/lessons/17679
m = 6
n = 6
# board = ['TTTANT', 'RRFACC', 'RRRFCC', 'TRRRAA', 'TTMMMF', 'TMMTTJ']
# board = ['IIIIOO', 'IIIOOO', 'IIIOOI', 'IOOIII', 'OOOIII', 'OOIIII']
# board = ['AAAAA','AUUUA','AUUAA','AAAAA']
board =  ['ABCD', 'BACE', 'BCDD', 'BCDD']
board = ['AABBEE','AAAEEE','VAAEEV','AABBEE','AACCEE','VVCCEE' ]

# 1. 전체를 탐색하면서 2x2 탐색
# 2. 2x2를 탐색하면 set 자료구조에 위치 추가
# 3. set에서 하나씩 pop하면서 위에서 블록을 땡겨옴
# 4. set이 없어질 때 까지 반복 

from collections import deque

def dup_board(board, new_board):
    for i in board:
        tmp = list(i)
        new_board.append(tmp)
    return


def search(new_board, i, j, char):
    # 4블록이 같은지 확인
        if new_board[i-1][j] != char:
            return False
        elif new_board[i][j-1] != char:
            return False
        elif new_board[i-1][j-1] != char:
            return False
        else:
            return True

def trav(new_board, m, n, que):
    que.clear()
    for i in range(m-1, 0, -1):
        for j in range(n-1, 0, -1):
            if new_board[i][j] == -1: continue
            char = new_board[i][j]
            if search(new_board, i, j, char):
                if [i,j] not in que:
                    que.append([i,j])
                if [i-1,j] not in que:
                    que.append([i-1, j])
                if [i,j-1] not in que:
                    que.append([i, j-1])
                if [i-1,j-1] not in que:
                    que.append([i-1, j-1])
    return len(que)

def delete(new_board, que):
    for i in que:
        new_board[i[0]][i[1]] = -1


def pull(new_board, que):
    while que:
        for i in range(len(que)):
            tmp = que.popleft()
            x = tmp[0]
            y = tmp[1]
            nx = x - 1
            while nx >= 0:
                if new_board[nx][y] != -1:
                    new_board[x][y] = new_board[nx][y]
                    new_board[nx][y] = -1
                    que.append([nx,y])
                    break
                else:
                    nx -= 1

def solution(m, n, board):
    new_board = []
    dup_board(board, new_board)
    answer = 0

    que = deque([])
    while True:
        # 지울 블록을 찾는다.
        answer += trav(new_board, m, n, que)

        # 지울 블록이 없으면 끝
        if not que:
            break

        # 지운다
        delete(new_board, que)

        # 땡긴다
        pull(new_board, que)

    return answer

print(solution(m, n, board))
