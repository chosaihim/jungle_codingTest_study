# 크레인 인형뽑기 게임
def move_to_bucket(board, num, bucket):
    index = num - 1
    is_moved_bucket = False
    moved_doll = 0
    for i in range(len(board)):
        if board[i][index] != 0 :
            moved_doll = board[i][index]
            board[i][index] = 0
            is_moved_bucket = True
            break
    if is_moved_bucket and bucket:
        if bucket[-1] == moved_doll:
            bucket.pop()
            return 2
        else:
            bucket.append(moved_doll)
            return 0
    elif bucket == []:
        bucket.append(moved_doll)
        return 0
    
    return 0


def solution(board, moves):
    bucket = []
    answer = 0
    for num in moves:
        answer += move_to_bucket(board, num, bucket)
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))