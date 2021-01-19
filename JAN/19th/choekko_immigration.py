import sys

n = 5
times = [1, 1, 10]


def solution(n, times) :
	times.sort()

	pl = 0
	pr = rst = (times[0] * n)

	while True :
		pc = (pl + pr) // 2
		
		sum = 0
		for time in times :
			sum += pc // time
			if sum > n :
				break

		if sum >= n :
			rst = min(rst, pc)
			pr = pc - 1
		else :
			pl = pc + 1

		if pl > pr :
			break
	return rst

print(solution(n, times))
		
		