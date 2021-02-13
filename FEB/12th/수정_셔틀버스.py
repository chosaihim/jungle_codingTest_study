# https://programmers.co.kr/learn/courses/30/lessons/17678
ta = ['08:00', '09:09', '09:10']
n =2
t =10
m =2

import collections


def ntot(time):
    h = time // 60
    m = time - h * 60
    h = str(h) if h >= 10 else '0' + str(h)
    m = str(m) if m >= 10 else '0' + str(m)
    return h + ':' + m


def solution(n, t, m, timetable):
    answer = ''
    timetable = collections.deque(timetable)
    table = []
    while timetable:
        ta = timetable.popleft()
        hour, min = ta.split(":")
        table.append(int(hour) * 60 + int(min))
    table.sort()
    timetable = collections.deque(table)

    # t를 오늘안의 유효한 값으로 만듬 (필요없을수도)
    # while n * t > 900:
    #     t -= 1

    # 앞에서부터 빼본다
    lastbus = 540 + t * (n - 1)
    oclock = 540
    cnt = 0
    for i in range(n - 1):
        if timetable:
            cand = timetable.popleft()
            if oclock < cand:  # 못탐           cnt >= m
                timetable.appendleft(cand)
            else:  # 탐
                cnt += 1
            oclock += i*t
    else:
        # 다 돌고 마지막 버스임
        # 사람이 꽉찼다면
        if m <= len(timetable):
            # 근데 얘도 못탄다면?
            if timetable[-1] > lastbus:
                return ntot(lastbus)
            else:
                return ntot(timetable[-1]-1)
        else:
            return ntot(lastbus)

print(solution(n,t,m,ta))