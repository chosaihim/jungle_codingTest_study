import heapq

# lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
lines = ["2016-09-15 00:00:00.000 3s"]
# lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 01:00:02.5 0.001s","2016-09-15 01:00:04 3.0s"]


# 90점
def solution(lines):
    log = []        

    def parse(lines, log):
        for i in lines:
            tmp = i.split() # 날짜, 시간, 경과시간으로 쪼갬

            str_time = tmp[1] # "20:59:57.421"
            par_str_time = str_time.split(":") # ["20","59","57.421"]
            flo_time = float(par_str_time[0])*60*60 + float(par_str_time[1])*60 + float(par_str_time[2]) # 초단위로 모두 변환해서 합산
            int_time = int(flo_time*1000) # 1000곱하고 정수형 변환

            par_elapse = tmp[2].split("s") # ["0.351", ""]
            flo_elpase = float(par_elapse[0]) # 0.351
            int_elpase = int(flo_elpase*1000-1) # 351
            log.append([int_time - int_elpase, int_time, int_elpase])
    
    parse(lines,log)
    heap = []

    # log = [시작한 시간, 끝난 시간, 경과 시간]
    max_len = 1
    for j in log:
        # 넣지 못한다면 그때는 max를 갱신할 수 없으므로, heappush한 뒤에 pop한다.
        heapq.heappush(heap, j[1])
        while heap and j[0] - heap[0] >= 1000:
            heapq.heappop(heap)
        max_len = max(len(heap), max_len)
    
    max_len = max(len(heap), max_len)
    return max_len


print(solution(lines))








    
    