s = "110010101001"


def solution(s):
	cnt1 = 0
	cnt2 = 0
	while True :
		for nbr in s :
			if nbr == '0' :
				cnt2 += 1
		s = s.replace("0", "")
		s = format(len(s), 'b')
		cnt1 += 1

		if s == '1' :
			break

	return([cnt1, cnt2])

print(solution(s))
	