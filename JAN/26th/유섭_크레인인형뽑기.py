def solution(board, moves):
    answer = 0
    a=len(board)
    b=len(board[1])

    stack=[]

    for m in moves:
        m=m-1
        for i in range(a):
            if board[i][m]!=0:
                stack.append(board[i][m])
                board[i][m]=0
                break
        if len(stack)>=2 and stack[-1]==stack[-2]:
            stack.pop()
            stack.pop()
            answer+=2
        


    return answer
