import heapq


jobs = [[4, 5], [6, 2], [7, 3], [9, 3], [10, 1]]


def solution(jobs):
	heapq.heapify(jobs)
	heap = []
	len_jobs = len(jobs)
	tmp = heapq.heappop(jobs)
	before_end = tmp[0] + tmp[1]
	time = tmp[1]
	while True :
		while jobs :
			after = heapq.heappop(jobs)
			if after[0] < before_end :
				heapq.heappush(heap, [after[1], after[0]])
			else :
				if heap :
					heapq.heappush(jobs, after)
				else :
					time += after[1]
					before_end += after[0] - before_end + after[1]
				break
		
		if heap :
			run, start = heapq.heappop(heap)
			time += before_end - start + run
			before_end += run
		
		if not jobs and not heap:
			break 
	return time//len_jobs

print(solution(jobs))

