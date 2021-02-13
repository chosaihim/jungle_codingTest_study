n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
timetable = ["23:59"]
timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
from collections import deque

# 버스의 모든 자리가 다 차는 경우 : 제일 늦은 사람보다 1분 빨리
# 버스에 자리가 비어있는 경우 : 가장 늦은 버스 


def real(n, t, m, timetable):
    time = []
    for i in timetable:
        split = i.split(":")
        hour = int(split[0])*60
        mini = int(split[1])
        if hour+mini == 24*60:
            time.append(24*60-1)
        else:
            time.append(hour+mini)

    time.sort()
    time = deque(time)

    bus_time = []
    for i in range(n):
        bus_time.append(9*60 + t*i)

    bus_cnt = m * n

    while time = 



def solution(n, t, m, timetable):
    that_time = real(n, t, m, timetable)

    if that_time//60 < 10:
        that_hour = '0' + str(that_time//60)
    else:
        that_hour = str(that_time//60)

    if that_time%60 < 10:
        that_min = '0' + str(that_time%60)
    else:
        that_min = str(that_time%60)
    answer = that_hour + ":" + that_min
    return answer

print(solution(n, t, m, timetable))