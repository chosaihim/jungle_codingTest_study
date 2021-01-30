# 1 = 1
# 2 = 1+1
# 3 = 1+2, 2+1
# 4 = 1+3, 2+2, 3+1
# . . .
# 같은 숫자 N번 쓴거 | 위에 저 조합
# 예를 들어, 5를 4번 썼다면 5555 | (1번사용과 3번사용 사칙연산) | (2번사용과 2번사용 사칙연산) | (3번사용과 1번사용 사칙연산)
# 8번까지 사용가능하니까 1~8 까지의 계산결과를 배열에 다 담음 (set으로 중복제거, 음수 제거)
# 전체 돌면서 number 있는지 확인

def solution(N, number):
    answer = 0
    num_set = [set([]) for _ in range(9)] # 중복제거 위해 set 사용
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