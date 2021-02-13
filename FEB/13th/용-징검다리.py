# 제일 작은 수를 찾는다. (a)

k = 3
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

from collections import deque
import heapq
def solution(stones, k):
    que = deque()
    visited = [0]*200001
    answer = 200000001
    
    cnt = 1

    # 제일 작은 수를 que에 담는다.
    for i in range(len(stones)):
        if stones[i] > answer: continue
        elif stones[i] < answer:
            que.clear()
        que.append(i)
        answer = stones[i]


    while cnt < k:
        cnt += 1
        heap = []
        # 다음 돌 선정
        for j in range(len(que)):
            tmp = que.popleft()
            visited[tmp] = 1
            # 왼쪽
            if tmp - 1 >= 0 and visited[tmp-1] == 0:
                visited[tmp-1] = 1
                que.append(tmp-1)
            # 오른쪽
            if tmp + 1 <= len(stones)-1 and visited[tmp+1] == 0:
                visited[tmp+1] = 1
                que.append(tmp+1)
    answer = 200000001
    for k in que:
        answer = min(answer,stones[k])

        
    return answer

print(solution(stones,k))