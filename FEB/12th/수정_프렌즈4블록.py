board = ['CCEEEG','CCDEEE','CCDDEE','EEEDGG','EEEGGG']
n = 6
m = 5


dx = [1, 0, 1]
dy = [0, 1, 1]


def prints(board):
    for i in range(m):
        for j in range(n):
            print(board[i][j], end=' ')
        print()
    print()


def check(board, target, i, j, m, n):
    cnt = 0
    for t in range(3):
        if 0 <= i + dy[t] < m and 0 <= j + dx[t] < n:
            if board[i + dy[t]][j + dx[t]] == target:
                cnt += 1
    if cnt == 3:
        return True
    else:
        return False


def removing(remove, board, m, n):
    for i in range(m):
        for j in range(n):
            if remove[i][j]:
                board[i][j] = 0
    prints(board)


    for j in range(n):
        here = m - 1
        bottom = here - 1
        while 0 <= bottom:
            bottom = here - 1
            while bottom >= 0 and board[bottom][j] == 0:
                bottom -= 1
            k = 0
            while bottom-k >= 0 and board[bottom-k][j] != 0:
                board[here-k][j] = board[bottom-k][j]
                k += 1

            if bottom-k < 0 or board[bottom-k][j] == 0:
                bottom -= k


    return board


def solution(m, n, board):
    count = 0

    for i in range(m):
        board[i] = list(board[i])

    while True:
        remove = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            for j in range(n):
                target = board[i][j]
                if target != 0 and check(board, target, i, j, m, n):
                    remove[i][j] = True
                    for t in range(3):
                        remove[i + dy[t]][j + dx[t]] = True
        for i in range(m):
            for j in range(n):
                if remove[i][j]:
                    count += 1
        prints(remove)

        flag_conti = False
        for i in range(m):
            for j in range(n):
                if remove[i][j]:
                    flag_conti = True

        else:
            if not flag_conti:
                break
        board = removing(remove, board, m, n)
        prints(board)

    answer = count
    return answer


print(solution(m,n,board))