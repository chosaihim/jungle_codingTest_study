n = 2 # 셔틀 운행 횟수
t = 1 # 셔틀 운행 간격
m = 2 # 한 셔틀 최대 크루 수
timetable = ["09:00","09:00","09:00","09:00"]
from collections import deque

#83.3/100
def solution(n, t, m, timetable):
    answer = ''
    curr_time = 9 * 60
    last_bus  = curr_time + (n-1) * t

    # 일단 다 분으로 된 시간으로 고쳐본다!   
    # mintable = [int(time[0:2])*60 + int(time[3:5]) for time in timetable]
    mintable = []
    for time in timetable:
        mintime = int(time[0:2])*60 + int(time[3:5])
        if mintime <= last_bus:
            mintable.append(mintime)
    mintable.sort()
        
    # 일단 버스에 태울 수 있는 애들 다 태워본다!
    inAbus = 0
    crew_num = 0
    if mintable:
        while crew_num < len(mintable):
            if mintable[crew_num] <= curr_time and inAbus < m:
                crew_num += 1
                inAbus += 1
            else:
                if curr_time == last_bus: break
                curr_time += t
                inAbus = 0
            
        crew_num -= 1
        last_crew = mintable[crew_num]
        # print(f'..........................inbus:{inAbus}, crew:{crew_num}, curr_time:{curr_time},last:{lastInAbus}')

    # 마지막 버스가 마지막까지 꽉 찼다면?
    # 한명씩 비켜내고 내가 들어간다아!
    min_answer = last_bus
    if curr_time == last_bus and inAbus== m: #inAbus == m:
        while mintable[crew_num] >= last_crew and crew_num >= 0:
            crew_num -= 1
        if(crew_num < 0):
            min_answer = mintable[0] -1
        else:
            min_answer = mintable[crew_num] 
    
    # answer
    answer = format(min_answer//60,'02') + ":" + format(min_answer%60, '02')
    return answer
    




print(solution(n,t,m,timetable))