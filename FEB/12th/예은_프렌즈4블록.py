def solution(m, n, board):
    answer = 0
    board = [list(one) for one in board] # 문자열을 배열로 바꿈
    # print(board)


    while(1):
        temp = answer
        mapping = [[0 for _ in range(n)] for _ in range(m)]
        # 순서대로 하나씩 돌면서 나 기준 오른쪽, 아래, 오른쪽아래 확인해서 다 같으면 다 1로 만든다
        # 아니라면, 넘어간다
        # map에서 1이라면 확인하지않고 넘어간다
        # 아래, 오른아래, 오른
        dx = [1, 1, 0]
        dy = [0, 1, 1]
        for i in range(m):
            for j in range(n):
                if board[i][j] == 0: continue
                flag = 1
                for k in range(3):
                    nx = i + dx[k]
                    ny = j + dy[k]
                    if nx >= m or ny >= n:
                        continue
                    if board[nx][ny] == board[i][j]:
                        flag += 1
                if flag == 4:
                    for k in range(3):
                        nx = i + dx[k]
                        ny = j + dy[k]
                        if nx >= m or ny >= n:
                            continue
                        mapping[nx][ny] = 1
                    mapping[i][j] = 1
                flag = 0

        # map에서 1인 애들을 지운다
        # board 세로 배열 만들어야함 ; list(map(list, zip(*board))) 전치하는방법!!! 익혀두자요
        tra_board = list(map(list, zip(*board)))
        for i in range(m):
            for j in range(n):
                if mapping[i][j] == 1:
                    tra_board[j].pop(i)
                    tra_board[j].insert(0, 0)
                    answer += 1

        board = list(map(list, zip(*tra_board)))
        # print(board)
        # print(temp, answer)
        if (temp == answer): break
        # 위 과정을 더이상 map에 1이 되는 경우가 없을 때까지 반복한다


    return answer


# test1
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]

#test2
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]

print(solution(m, n, board))
dd = list(map(list, zip(*board)))
# print(dd)