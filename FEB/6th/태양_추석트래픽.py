import sys
import heapq
def get_time(s) :
    hour = int(s[0:2]) * 60 * 60 * 1000;
    minute = int(s[3:5]) * 60 * 1000;
    second = int(s[6:8]) * 1000 + int(s[9:12])
    return hour + minute + second

def get_process_time(s) :
    time = int(s[0]) * 1000
    if len(s) > 2 :
        temp = s[2:];
        d = int(temp[0:len(temp)-1])
        for i in range(3 - len(temp)+1) :
            d *= 10
        time += d
    return time

def solution(lines) :
    answer = 0
    logs = []
    hq = []
    for l in lines :
        time = get_process_time(l[24:])
        start = get_time(l[11:23]) - time + 1
        logs.append((start, time))
    logs.sort()
    for h in logs :
        s, t = h[0], h[1]
        print(s, t)
        while len(hq) != 0 and hq[0] <= s :
            heapq.heappop(hq)
            heapq.heapify(hq)
        heapq.heappush(hq, s + t - 1 + 1000)
        heapq.heapify(hq)
        answer = max(answer, len(hq))
    return answer

print(solution(["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]))
