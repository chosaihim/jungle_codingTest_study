from itertools import permutations
import math

def solution(numbers):
    answer = 0
    numbers = list(numbers)
    permutes = []
    for i in range(1, len(numbers)+1):
        permutes.extend(list(permutations(numbers, i)))
    numbers = []
    for one in set(permutes):
        numbers.append(int(''.join(one)))

    numbers = list(set(numbers))
    for number in numbers:
        flag = True
        if number == 1 or number == 0:
            continue
        for i in range(2, int(number**0.5)+1): # 자신의 제곱수까지만 나눠보면 된다
            if number % i == 0:
                flag = False
        if flag:
            answer += 1
    print(numbers)
    return answer


numbers = "17"
numbers = "011"
numbers = "111"

print(solution(numbers))

