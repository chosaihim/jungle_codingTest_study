import sys
import heapq

a = [9,-1,-5]

def solution(a):
    answer = 0
    # logic
    # upper group (a[0]~ a[idx]) 
    # target value (a[idx])
    # lower group (a[idx] ~ a[n-1])
    #! target value가 upper group의 최솟값과 lower group의 최솟값보다 작으면 불가능 하다.
    #? if( target < min(lowergroup) , target < min(uppergroup) ) return impossible;
    #! group을 나타내는 방법으로 heap 자료구조를 사용한다.
    
    q = []
    upper_check = [False] * len(a)
    lower_check = [False] * len(a)
    upper_check[0] = True #@ 앞에 어떤 수도 올수 없는 첫번째 인덱스는 상관없지
    upper_check[len(a) - 1] = True
    lower_check[len(a) - 1] = True
    heapq.heappush(q, a[0])

    for i in range(1, len(a) - 1) :
        if q[0] > a[i] : #@ uppergroup 의 최솟값이 target value보다 큰가?
            upper_check[i] = True
        heapq.heappush(q, a[i])
    q = []
    heapq.heappush(q, a[len(a) - 1])
    for i in range(len(a) - 1, 0, -1) :
        if q[0] > a[i] :
            lower_check[i] = True
        heapq.heappush(q, a[i])
    for i in range(len(a)) :
        if upper_check[i] or lower_check[i] :
            answer += 1
    return answer 
