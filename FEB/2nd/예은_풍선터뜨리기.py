# -> 방향으로 가면서 최솟값을 저장하는 배열 생성
# <- 방향으로 가면서 최솟값을 저장하는 배열 생성
# 그 생성된 배열과 현재값 비교해서 둘다에 내가 없으면 안됨

def solution(a):
    answer = len(a)
    if len(a) < 3:
        answer = len(a)
    else:
        length = len(a)
        go_right = []
        go_left = [0] * length
        right_min = 1000000001
        left_min = 1000000001
        for i in range(length):
            if right_min > a[i]:
                right_min = a[i]
            go_right.append(right_min)
        for i in range(length-1, -1, -1):
            if left_min > a[i]:
                left_min = a[i]
            go_left[i] = left_min
        for i in range(length):
            if a[i] != go_right[i] and a[i] != go_left[i]:
                answer -= 1
    return answer


# a = [9,-1,-5] # 3
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33] # 6

print(solution(a))
