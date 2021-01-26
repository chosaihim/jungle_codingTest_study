def solution(board, moves):
    answer = 0
    stack = [[] for _ in range(len(board) + 1)]
    result = []

    for j in range(len(board)):
        for i in range(len(board) - 1, -1, -1):
            if (board[i][j] == 0):
                continue
            stack[j + 1].append(board[i][j])

    for i in range(len(moves)):
        if len(stack[moves[i]]) == 0:
            continue
        result.append(stack[moves[i]].pop())
        if (len(result) >= 2) and (result[-1] == result[-2]):
                result.pop()
                result.pop()
                answer += 2

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

# 열로 스택을 만든다 (행 숫자 큰게 젤 앞으로, 작은게 젤 뒤로, 0은 제끼기)
# list 크기 == 0 이면 아무것도 안한다
# moves 에 해당되는 스택에서 pop해서 결과 배열에 넣는다
# 같은 원소가 연속되면 사라지게하고 카운트 +2
