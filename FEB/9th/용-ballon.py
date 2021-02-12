# https://programmers.co.kr/learn/courses/30/lessons/68646
import heapq
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

def solution(a):
    answer = 2
    left_heap = []
    right_heap = []

    # 
    big_count = [0]*(len(a)+1)
    heapq.heappush(left_heap, a[0])

    # 기준 풍선
    for i in range(1,len(a)-1):
        if left_heap[0] > a[i]:
            big_count[i] += 1
        heapq.heappush(left_heap,a[i])

    heapq.heappush(right_heap, a[-1])
    for j in range(len(a)-2,0,-1):
        if big_count[j] >= 1:
            answer += 1
        elif right_heap[0] > a[j]:
                answer += 1
        heapq.heappush(right_heap, a[j])
            
        
    return answer

print(solution(a))