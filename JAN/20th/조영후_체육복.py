n = 5

lost = [2, 4]
reserve = [1, 3, 5]


def solution(n, lost, reserve):
	greedy = [1 for _ in range(n + 1)]
	greedy[0] = 0
	for student in reserve :
		greedy[student] = 2
	for student in lost :
		greedy[student] -= 1
	for i in range(1, n + 1) :
		if greedy[i] == 0 :
			if greedy[i-1] == 2 :
				greedy[i-1] = 1
				greedy[i] = 1
			elif i + 1 != n + 1 and greedy[i+1] == 2:
				greedy[i+1] = 1
				greedy[i] = 1

	cnt = 0
	for have in greedy :
		if have != 0 :
			cnt += 1
	return(cnt)


print(solution(n, lost, reserve))