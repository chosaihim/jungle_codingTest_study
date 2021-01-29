n = 6
times = [7, 10]

def solution(n, times):
    times.sort()
    max_t = times[0]*n
    min_t = times[0]
        
    # 심사 대상 수 = sum(예상 총 시간 // 개별 검사 시간)
    while min_t < max_t:
        ex = (max_t + min_t) // 2
        ex_n = 0
        for i in times:
            ex_n += ex // i
        # 만약 더 많은 사람을 심사할 수 있다면 : ex를 내려야된다.
        if ex_n >= n: 
            max_t = ex
        # 만약 충분한 사람을 심사할 수 없다면 : ex를 올려야된다.
        else:
            min_t = ex + 1
    ex = (max_t + min_t) // 2
    return ex
        


result = solution(n,times)
print(result)