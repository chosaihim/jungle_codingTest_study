from collections import deque

def solution(n, t, m, timetable):
    answer = ''
    timetable = [int(one.split(':')[0])*60 + int(one.split(':')[1]) for one in timetable]
    timetable.sort()
    timetable = deque(timetable)
    bus_time = deque([540])
    for i in range(1, n):
        bus_time.append(bus_time[-1] + t)
    last_bus_time = bus_time[-1]

    while(len(bus_time) != 1):
        x = bus_time.popleft()
        accomo = 0
        while (timetable[0] <= x):
            if timetable[0] <= x:
                accomo += 1
                timetable.popleft()
                if accomo == m: break

    # 이제 마지막 버스가 남았다
    # 버스가 풀방된다면, 탈 수 있는 가장 늦은 애보다 1분 빠르게
    # 버스가 풀방 안된다면, 버스 시간에 오기
    last_person = 0
    accomo = 0
    for one in timetable:
        if one <= bus_time[0]:
            accomo += 1
            if accomo == m:
                answer = one - 1
                break
    if accomo < m:
        answer = bus_time[0]

    answer_hour = answer // 60
    answer_minutes = answer % 60
    if answer_hour < 10:
        answer_hour = '0' + str(answer_hour)
    else:
        answer_hour = str(answer_hour)

    if answer_minutes < 10:
        answer_minutes = '0' + str(answer_minutes)
    else:
        answer_minutes = str(answer_minutes)
    answer = answer_hour + ':' + answer_minutes
    return answer

# 버스시간 맨 뒤부터 비교한다
# 맨 뒤버스를 타기 위한 도착시간을 구한다
# 탈 수 있는 제일 늦은 애보다 1분 빨리 온다
# 다 탈 수 없다면 마지막 버스 시간에 온다

# 탈 수 있는 제일 늦은 애 구하기
# 맨앞버스부터 가능한 애들 태워서 보내버림



# test1
n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]

# test2
# n = 2
# t = 10
# m = 2
# timetable = ["09:10", "09:09", "08:00"]

#test6
# n=10
# t=60
# m=45
# timetable=["23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59",
#            "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]


print(solution(n, t, m, timetable))

