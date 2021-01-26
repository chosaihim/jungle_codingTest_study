import sys

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
    blen = len(board)
    answer = 0
    top = 0

    stack = []
    for x in moves:
        y = 0

        while y < blen and board[y][x-1] == 0:
            y += 1

        if y >= blen:        # 이 줄에 인형 없음
            continue

        else:               # 인형 발견
            # print(stack)
            if len(stack) != 0:
                top = stack.pop()
            found = board[y][x-1]
            # print("found: ",board[y][x - 1])
            board[y][x-1] = 0

            if top != found:
                if top != 0:
                    stack.append(top)
                stack.append(found)
            else:
                # print("pop!")
                answer += 2
    return answer


print(solution(board, moves))