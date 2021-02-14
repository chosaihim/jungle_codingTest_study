# https://programmers.co.kr/learn/courses/30/lessons/64062
# 제일 작은 수를 찾는다. (a)

k = 3
stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]

# 이분탐색
# 연속 k번으로 인원수 - 돌 높이 <= 0 이면, 뛸 수 없으므로 인원수 감소
# 연속 k번으로 인원수 - 돌 높이 > 0 이면, 충분하므로 인원수 증가

# bool : True = 인원수를 늘림 // False = 인원수를 감소
def binary(crew, stones, k):
    flag = k
    for height in stones:
        if flag == 0:
            return False
        if height - crew <= 0:
            flag -= 1
        else:
            flag = k
    if flag == 0:
            return False
    return True



def solution(stones, k):
    left = 1
    right = 200000000
    while left <= right:
        mid = (left + right) // 2
        if binary(mid, stones, k):
            left = mid + 1
        else:
            right = mid - 1
    return left

print(solution(stones,k))