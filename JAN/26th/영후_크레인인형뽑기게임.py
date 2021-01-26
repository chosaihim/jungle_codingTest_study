from collections import deque

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]

moves = [1,5,3,5,1,2,1,4]

def solution(board, moves):
	cnt = 0
	window = [0 for _ in range(len(board))]
	for i in range(len(board)) :
		for j in range(len(board)) :
			if board[j][i] != 0 :
				window[i] = j
				break
	# print(window)
	stk = []
	for move in moves :
		if window[move - 1] == len(board) : 
			continue
		tmp = board[window[move - 1]][move - 1]
		if stk and stk[-1] == tmp :
			stk.pop()
			cnt += 2
		else :
			stk.append(tmp)
		window[move - 1] += 1
	return cnt 

print(solution(board, moves))

