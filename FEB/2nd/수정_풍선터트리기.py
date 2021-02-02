from builtins import map

a = [2,4,1,3,5]
def solution(a):
    answer = 0;
    a_last = len(a) - 1
    minimum_left = [0 for _ in range(a_last + 1)]
    minimum_right = [0 for _ in range(a_last + 1)]
    #     두번째부터 마지막-1까지
    minimum_left[1] = a[0]
    minimum_right[a_last - 1] = a[a_last]

    for i in range(2, a_last + 1):
        minimum_left[i] = min(minimum_left[i - 1], a[i - 1])
    for j in range(a_last - 2, -1, -1):
        minimum_right[j] = min(minimum_right[j + 1], a[j + 1])

    print(minimum_left)
    print(minimum_right)
    for i in range(1, a_last):
        if minimum_left[i] > a[i] or minimum_right[i] > a[i]:
            answer += 1
    answer += 2
    return answer

print(solution(a))