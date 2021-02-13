import heapq

def solution(jobs):
    wait = []
    cand = []
    for i in jobs:
        heapq.heappush(wait, i)
    
    cur_time = 0
    sum_avg = 0
    while wait:
        # 작업 시작
        now = heapq.heappop(wait)

        # now의 작업 완료 시간
        cur_time += now[1]
        sum_avg += cur_time-now[0]
        

        # 다음 작업의 시작 시간이 현재 작업 완료 시간보다 빠르면, 작업 시간이 빠른 순으로 cand에 추가
        while wait and wait[0][0] <= cur_time:
            tmp = heapq.heappop(wait)
            # cand = [소요시간, 시작시간]
            heapq.heappush(cand, [tmp[1], tmp[0]])
        
        # 작업이 끝나면 소요시간 순으로 처리한다.
        while cand:
            # tmp2 = [소요시간, 시작시간]
            tmp2 = heapq.heappop(cand)
            cur_time += tmp2[0]
            sum_avg += cur_time-tmp2[1]
    answer = sum_avg // len(jobs)
    return answer

