import sys

def solution(jobs):
    answer = 0
    sum_time = 0
    curr_time = 0
    jobs_len = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1]) # 소요시간이 작은 순으로 정렬. 
    while len(jobs) != 0:
        for i in range(len(jobs)):
            if jobs[i][0] <= curr_time:
                curr_time += jobs[i][1]
                sum_time += curr_time - jobs[i][0]
                jobs.pop(i)
                break
            if i == len(jobs) - 1: # 현재 시간에 아직 작업이 없을 경우 시간을 증가시켜줌
                curr_time += 1

    answer = sum_time // jobs_len
    return answer

print(solution([[0, 3], [1, 9], [2, 6]]))