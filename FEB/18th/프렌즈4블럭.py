m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]


def solution(m, n, board): #? 높이가 m 너비 n
    _board = [list(board[i]) for i in range(m)]
    canBreak = [[False for i in range(n)] for i in range(m)] # 부숴질 수 있어?

    def search_for_erase() : # 지워야할 부분을 기준으로 오른쪽, 아래, 대각선 아래를 검사할거야
        dx, dy = [0,1,0,1], [0,0,1,1] # 차례로 [현재 인덱스, 오른쪽, 아래, 대각선 아래] 
        isContinue = False
        for h in range(m - 1) : # -2 번째 인덱스 까지만
            for w in range(n - 1) :
                flag = True
                interest = _board[h][w]
                if interest == 'x' :
                    continue
                for i in range(1, 4) :
                    if interest != _board[h + dy[i]][w + dx[i]] :
                        flag = False
                        break
                if flag :
                    isContinue = True
                    for i in range(0, 4) :
                        canBreak[h + dy[i]][w + dx[i]] = True
        return isContinue
                    
                        
    def erase_and_move() :
        for h in range(m) :
            for w in range(n) :
                if canBreak[h][w] :
                    _board[h][w] = 'x'
                    for bh in range(h, 0, -1) :
                        _board[bh][w] = _board[bh - 1][w]
                        _board[bh - 1][w] = 'x'
                        continue

    while search_for_erase() :
        erase_and_move()
        canBreak = [[False for i in range(n)] for i in range(m)] # refresh

    answer = 0
    for i in range(m) :
        answer += _board[i].count('x')
    # for i in range(m) :
    #     print(_board[i])
    return answer

print(solution(m,n,board))
