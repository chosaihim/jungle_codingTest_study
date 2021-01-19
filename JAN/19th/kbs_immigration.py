# 프로그래머스 입국심사 이분탐색
def solution(n, times):
    answer = 0
    times.sort()

    pl = 1
    pr = times[-1] * n
    mid = 0

    if n == 1:
        answer = times[0]
        print(answer)
        return answer

    while pl < pr:
        mid = (pl + pr) // 2
        people = 0
        for time in times:
            people += mid // time
        if people < n:
            pl = mid + 1
        else:
            pr = mid - 1
        
    answer = mid
    print(answer)
    return answer

solution(10, [1,5])