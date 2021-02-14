# permutations 쓰면 시간초과

from itertools import permutations
from math import factorial

def solution(n, k):
    answer = []
    arr = [i for i in range(1, n+1)]
    i = 1
    if k == factorial(n):
        return arr[::-1]
    while (i != n):
        if k == factorial(n-i):
            first = 0
        elif k ==0:
            arr.sort(reverse=True)
            answer.extend(arr)
            return answer
        else:
            if k % factorial(n-i) == 0:
                first = k // factorial(n-i) - 1
            else:
                first = k // factorial(n-i)
        answer.append(arr[first])
        arr.pop(first)
        # print(arr)
        k %= factorial(n-i)
        i += 1
    answer.append(arr[0])
    return answer


n = 5
k = 10
print(solution(n, k))
