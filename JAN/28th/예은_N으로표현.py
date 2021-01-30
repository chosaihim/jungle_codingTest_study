def solution(N, number):
    answer = 0
    num_set = [set([]) for _ in range(9)]
    for i in range(1, 9):
        num_set[i].add(int(str(N)*i))
        for j in range(1, i):
            for k in num_set[j]:
                for l in num_set[i-j]:
                    num_set[i].add(k + l if (k+l) >= 0 else 0)
                    num_set[i].add(k - l if (k-l) >= 0 else 0)
                    num_set[i].add(l - k if (l-k) >= 0 else 0)
                    num_set[i].add(k * l if (k*l) >= 0 else 0)
                    if l != 0:
                        num_set[i].add(k // l)
                    if k != 0:
                        num_set[i].add(l // k)
        num_set[i] = list(num_set[i])
    for i in range(1, 9):
        if number in num_set[i]:
            answer = i
            break
    if answer == 0: answer = -1
    return answer


N = 5
number = 12

print(solution(N, number))