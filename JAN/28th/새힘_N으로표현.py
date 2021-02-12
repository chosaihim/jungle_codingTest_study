#해설참조

N = 5; number = 12 # return = 4
N = 2; number = 11 # return = 3

# 1 ~ 8 개의 N으로 만든 수들의 집합 만들기
# [set x 8] 리스트 필요
# 모든 리스트에 Nx(N개) 수를 수동으로 만들어 줌
# 1~N-1를 돌면서, 집합들을 조합해서 N개로 만든 수들의 집합 만들기
def solution(N, number):
    answer = 0
    
    if N == number:
        return 1;
    
    # [set x 8] 리스트 필요
    sets = [set() for i in range(8+1)]
    # 수동으로 NNN.. 넣어주기
    for i in range(1,8+1):
        sets[i].add(int(str(N)*i))
        # print(sets[i])
    # print(sets)
    
    
    for i in range(2,9):
        for j in range(1,i):
            for first_set in sets[j]:
                for second_set in sets[i-j]:
                    sets[i].add(first_set + second_set)
                    sets[i].add(first_set - second_set)
                    sets[i].add(first_set * second_set)
                    if second_set: sets[i].add(first_set // second_set)
    
    answer = -1
    for i in range(1,9):
        if number in sets[i]:
            answer = i
            break
                    
    return answer

print(solution(N,number))