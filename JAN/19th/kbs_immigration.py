# 프로그래머스 입국심사 이분탐색
def solution(n, times):
    answer = 0
    times.sort()

    pl = 0
    pr = times[0] * n


    while pl < pr:
        mid = (pl + pr) // 2
        sum = 0
        for time in times:
            sum += mid // time
        if sum < n:
            pl = mid + 1
        else:
            pr = mid
        
    
    return (pl+pr) // 2

