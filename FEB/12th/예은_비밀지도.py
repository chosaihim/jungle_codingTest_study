def solution(n, arr1, arr2):
    answer = []
    arr1 = [list(bin(one).split('b')[1]) for one in arr1]
    arr2 = [list(bin(one).split('b')[1]) for one in arr2]

    for one in arr1:
        while(len(one) != n):
            one.insert(0, '0')

    for one in arr2:
        while (len(one) != n):
            one.insert(0, '0')

    result = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr1[i][j] == '0' and arr2[i][j] == '0':
                result[i][j] = ' '
            else:
                result[i][j] = '#'

    for one in result:
        answer.append(''.join(one))

    return answer

# 이진수로 변환한다  bin 함수 이용
# 샾과 공백으로 나타낸다

# test1
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

# test2
# n = 6
# arr1 = [46, 33, 33, 22, 31, 50]
# arr2 = [27, 56, 19, 14, 14, 10]

print(solution(n, arr1, arr2))