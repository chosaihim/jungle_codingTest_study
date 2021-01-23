import sys
import heapq

jobs = 	[[0, 3], [1, 9], [2, 6], [4, 3]]

def solution(jobs):

    jobs.sort()
    heap = []    
    curr_time = 0
    sum_time  = 0
    i = 0
    
    while i < len(jobs):
        start, hours = map(int, jobs[i])
        
        if start <= curr_time:
            heapq.heappush(heap, [hours,start])
        elif(heap):
            i -= 1
            hours, start = heapq.heappop(heap)
            sum_time += hours + (curr_time - start)
            curr_time += hours
        else:
            curr_time = start
            i -= 1
        i += 1
    
    if(heap):
        while(heap):
            hours, start = heapq.heappop(heap)
            sum_time += hours + (curr_time - start)
            curr_time += hours

    answer = sum_time // len(jobs)
    print(answer)
    return answer

solution(jobs)