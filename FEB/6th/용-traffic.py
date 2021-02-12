import heapq

# lines = ["2016-09-15 00:00:00.000 3s"]
# lines = ["2016-09-15 01:00:02.5 0.001s","2016-09-15 01:00:04 3.0s"]
# lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
# lines = ["2016-09-15 00:00:00.000 3s"]
# lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]

# 90점
def solution(lines):
    log = []


    def dot_parse(str):
        if len(str) == 3:
            return int(str)
        elif len(str) == 2:
            return int(str)*10
        elif len(str) == 1:
            return int(str)*100
        else:
            print("dot_parse error, str:", str)
            return 0

    def parse(lines, log):
        for i in lines:
            split_lines = i.split(" ") # split_lines = ["2016-09-15", "20:59:57.421", "1.351s"]
            split_times = split_lines[1].split(":") # split_times =  ["20", "59", "57.421"]
            time = int(split_times[0])*60*60*1000 + int(split_times[1])*60*1000

            # time parsing
            # 만약에 .이 있으면 분리한다.
            if '.' in split_times[2]:
                dot_times = split_times[2].split(".") #dot_times =  ["57", "421"]
                time += int(dot_times[0]) * 1000 + dot_parse(dot_times[1])

            # 없으면 그대로 써준다 
            else:
                time += int(split_times[2]) * 1000

            # elpase parsing
            # s 떼기
            no_s_elapse = split_lines[2].split("s") # ["1.351", ""]
            elapse = 0
            if '.' in no_s_elapse[0]:
                split_elapse = no_s_elapse[0].split(".") # ["1", "351"]
                elapse += int(split_elapse[0])*1000 + dot_parse(split_elapse[1])
            else:
                elapse += int(no_s_elapse[0]) * 1000
            elapse -= 1
            # 시작 시간 순 힙정렬
            heapq.heappush(log, [time-elapse, time+999])
            

    parse(lines,log)
    heap = []

    # log = [시작한 시간, 끝난 시간 + 1초]
    max_len = 0
    while log:
        tmp = heapq.heappop(log)
        heapq.heappush(heap, tmp[1])
        if heap and heap[0] < tmp[0]:
            heapq.heappop(heap)
        max_len = max(max_len, len(heap))
        
    return max_len


print(solution(lines))