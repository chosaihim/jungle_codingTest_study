import heapq
import copy

def solution(a):
    answer = len(a)
    if len(a) < 3:
        return answer
    left_min = a[0]
    heap = copy.deepcopy(a[2:])
    heapq.heapify(heap)
    right_min = heapq.heappop(heap)
    check_set = set()
    for i in range(1, len(a)-1):
        target = a[i]
        if target > left_min and target > right_min:
            answer -= 1
        check_set.add(a[i])
        if left_min > a[i]:
            left_min = a[i]
        if right_min == a[i]:
            tmp = heapq.heappop(heap)
            while True:
                before_len = len(check_set)
                check_set.add(tmp)
                after_len = len(check_set)
                if before_len==after_len:
                    tmp = heapq.heappop(heap)
                else:
                    break
            right_min = tmp
            # print(right_min)
            # print(target, right_min)
    return answer

print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33]))
