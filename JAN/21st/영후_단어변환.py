import sys

begin = 'hit'
target = 'cog'

words = ["hot", "dot", "dog", "lot", "log", "cog"]


def valid(str1, str2) :
	cnt = 0
	for i in range(len(str1)) :
		if str1[i] != str2[i] :
			cnt += 1
	if cnt == 1 :
		return 1
	else :
		return 0

def solution(begin, target, words):
	stk = []
	min_value = 51
	
	for i, content in enumerate(words) :
		if valid(begin, content) :
			stk.append((1 << i, content, 1))    # 비트맵으로 방문 표시했음


	while stk :
		bitfield, word, cnt = stk.pop()

		if word == target :
			min_value = min(min_value, cnt)	

		for i, content in enumerate(words) :
			if (bitfield & 1 << i) == 0 and valid(word, content) :
				stk.append(((bitfield | 1 << i), content, cnt + 1))

	if min_value == 51 :
		return 0
	
	return min_value

print(solution(begin, target, words))
		

	
	

	
	
