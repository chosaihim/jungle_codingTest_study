# 제일 작은 수를 찾는다. (a)

k = 3
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

from collections import deque
import heapq
def solution(stones, k):
    # 1. 일단 제일 작은 수(n1)를 찾는다. 
    # 2. 그 idx에서 왼쪽으로 k-1번째, 오른쪽으로 k-1번째를 찾아 각각의 최대수를 heap에 넣는다.
    # 3. 최대수들 중, 최소수가 answer이다.
    que = deque()
    minimum = 200000001

    cnt = 1
    # 첫 원소 추출
    for i in range(len(stones)):
        tmp = stones[i]
        if tmp > minimum: continue
        elif tmp < minimum:
            minimum = tmp
            que.clear()
        que.append(i)

    heap = []
    while que:
        tmp = que.popleft()
        maximum = 0
        for i in range(1, k):
            # 왼쪽
            if tmp-i < 0: continue
            elif stones[tmp-i] > maximum:
                maximum = stones[tmp-i]
        if maximum != 0:
            heapq.heappush(heap, maximum)

        maximum = 0
        for i in range(1, k):
            # 오른쪽
            if tmp+i > len(stones)-1: continue
            elif stones[tmp+i] > maximum:
                maximum = stones[tmp+i]
        if maximum != 0:
            heapq.heappush(heap, maximum)
        
    answer = heap[0]
        
    return answer

print(solution(stones,k))