lines = [
    "2016-09-15 20:59:57.421 0.351s",
    "2016-09-15 20:59:58.233 1.181s",
    "2016-09-15 20:59:58.299 0.8s"  ,
    "2016-09-15 20:59:58.688 1.041s",
    "2016-09-15 20:59:59.591 1.412s",
    "2016-09-15 21:00:00.464 1.466s",
    "2016-09-15 21:00:00.741 1.581s",
    "2016-09-15 21:00:00.748 2.31s" ,
    "2016-09-15 21:00:00.966 0.381s",
    "2016-09-15 21:00:02.066 2.62s"
]
# lines = [
#     "2016-09-15 01:00:04.002 2.0s",
#     "2016-09-15 01:00:07.000 2s"
# ]

# 일단 문자열을 split해서 날짜 버리고 
# 시간분초미리초 다 합쳐서, 
# [시작,끝]인 배열의 배열로 만든다.

# sorting 한다.
# 초를 뒤로 움직여가면서 최대값을 갱신(?)

def solution(lines):
    answer = 0
    timeline = []
    
    #time line array
    for line in lines:
        
        #split!
        date, finish_str, running_str = line.split()
        
        #finish
        hh,mm,ss = finish_str.split(":")
        sec,msec = ss.split(".") 
        finish = int(hh)*3600 + int(mm)*60 + float(ss)
        
        #running time
        running_str = running_str.split('s')[0]
        running = float(running_str)
        
        # print(f'finish: {finish}, running:{running}')
        
        #time line
        start = finish - running + 0.001
        timeline.append([start,finish])
    
    
    timeline.sort()
    # print(timeline)
    
    len_time = len(timeline)
    for i in range(len_time):
        start , end = timeline[i]
        
        start_cnt = 0
        end_cnt = 0
        
        for j in range(len_time):
            start_j, end_j = timeline[j]
        
            #after start
            if start <= end_j and start_j < start + 1.0:
                start_cnt += 1
            answer = max(answer, start_cnt)
            
            #after ends
            if start_j < end+1.0 and end <= end_j:
                end_cnt += 1
            answer = max(answer,end_cnt)
            
        # print(f'answer:{answer}')
    
    return answer

print(solution(lines))