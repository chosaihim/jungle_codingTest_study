# 크레인 인형뽑기 게임



def solution(board, moves):
    board_length = len(board)
    board_ptr = [board_length for _ in range(board_length)]
    meet_doll = [False for _ in range(board_length)]
    for i in range(board_length):
        for j in range(board_length):
            if not meet_doll[j]:
                if board[i][j] == 0:
                    board_ptr[j] -= 1
                else:
                    meet_doll[j] = True
    stk = []
    answer = 0
    last_doll = 0
    for num in moves:
        if stk:
            last_doll = stk[-1]
        if board_ptr[num-1] == 0:
            continue
        if last_doll == board[board_length - board_ptr[num-1]][num-1]:
            board_ptr[num-1] -= 1
            stk.pop()
            answer += 2
            continue
        stk.append(board[board_length - board_ptr[num-1]][num-1])
        board_ptr[num-1] -= 1

    

    
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))