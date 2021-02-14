# https://programmers.co.kr/learn/courses/30/lessons/42627

jobs = [[0, 3], [1, 9], [2, 6]]
jobs = [[0, 10], [2, 10], [9, 10], [15, 2]]

import heapq

# jobs = [시작시간, 소요시간]
def solution(jobs):
    length = len(jobs)
    heapq.heapify(jobs)
    cur_time = 0
    total = 0
    wait = []


    while jobs:
        # 만약 중간에 wait가 비어있다면, 시작 시간이 제일 빠른 작업을 넣는다. 
        temp = heapq.heappop(jobs)
        heapq.heappush(wait, [temp[1], temp[0]])

        
        while wait:
            tmp = heapq.heappop(wait)

            if tmp[1] <= cur_time:
                cur_time += tmp[0]
                total += cur_time - tmp[1]
            else:
                cur_time = tmp[0] + tmp[1]
                total += tmp[0]
                
            # 작업 중일 때, 다른 작업이 들어오면 소요시간 순으로 대기시킨다. 
            while jobs and jobs[0][0] < cur_time:
                tmp2 = heapq.heappop(jobs)
                heapq.heappush(wait, [tmp2[1], tmp2[0]])
            

    # 소요시간 계산
    answer = total // length
    return answer

print(solution(jobs))
