# https://programmers.co.kr/learn/courses/30/lessons/17678

n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
timetable = ["23:59"]
timetable = ["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
from collections import deque


def time_parsing(timetable):
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
    return time


def bus(n, t):
    bus_table = []
    for i in range(n):
        bus_table.append(9*60+i*t)
    print('bus_table:', bus_table)
    return bus_table

# 무지는 무조건 마지막 버스 마지막 자리에 타야한다.
# 앞의 대기자들은 모두 버스에 태운다.
# 마지막 버스에서 남은 자리가 있으면 마지막 버스 도착 시간에 무지를 태운다.
# 아니라면 마지막 탑승자보다 1분 빨리 도착한다.
def find(time_table, bus_table, n, t, m):
    time_table = deque(time_table)
    # 마지막 버스까지 태워본다. 
    for i in range(len(bus_table)):
        seat = 0
        while time_table and time_table[0] <= bus_table[i] and seat < m:
            tmp = time_table.popleft()
            seat += 1
    print(seat)
    if seat < m:
        return bus_table[i]
    else:
        return tmp-1

    
    

        
        




def solution(n, t, m, timetable):
    time_table = time_parsing(timetable)
    bus_table = bus(n, t)

    that_time = find(time_table, bus_table, n, t, m)

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