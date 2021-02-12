# https://programmers.co.kr/learn/courses/30/lessons/17681

n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27, 56, 19, 14, 14, 10]

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]



def solution(n, arr1, arr2):
    amap = [0]*n
    answer = []

    

    for i in range(n):
        tmp = arr1[i] | arr2[i]
        tmp2 = [0]*n
        for j in range(n):
            if 1<<j & tmp:
                tmp2[n-j-1] = "#"
            else:
                tmp2[n-j-1] = " "
        tmp3 = ''.join(tmp2)
        answer.append(tmp3)

    return answer


print(solution(n,arr1,arr2))