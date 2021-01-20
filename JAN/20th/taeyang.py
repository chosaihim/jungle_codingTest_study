import sys
debug = True
if debug : sys.stdin = open('input.txt', 'r')
n = int(sys.stdin.readline().rstrip())
lost = list(map(int, sys.stdin.readline().rstrip().split()))
reserve = list(map(int, sys.stdin.readline().rstrip().split()))
def solution(n, lost, reserve):
    answer = 0
    isLost = [False] * (n + 1)
    isReserve = [False] * (n + 1)
    for l in lost :
        isLost[l] = True
    for r in reserve :
        isReserve[r] = True
    for i in range(1, n + 1) :
        if isLost[i] :
            if isReserve[i] :
                isReserve[i] = False
                isLost[i] = False
    for i in range(1, n + 1) :
        if isLost[i] :
            if i - 1 > 0 and isReserve[i - 1] :
                answer += 1
                isReserve[i - 1] = False
                isLost[i] = False
            elif i + 1 <= n and isReserve[i + 1] :
                answer += 1
                isReserve[i + 1] = False
                isLost[i] = False
        else :
            answer += 1
    return answer

print(solution(n,lost,reserve))
