from itertools import product

# 90.9 점 (테케5 시간초과)
def solution(user_id, banned_id):
    answer = []
    cand = []
    for banned in banned_id:
        one_voca_cand = []
        for user in user_id:
            flag = True
            if len(banned) != len(user):
                continue
            for i in range(len(user)):
                if banned[i] == '*':
                    continue
                elif banned[i] != user[i]:
                    flag = False
                    break
            if flag:
                one_voca_cand.append(user)
        cand.append(one_voca_cand)
    print(cand)
    real_cand = list(product(*cand)) # product 사용하면 시간초과 날수밖에 없는듯 (product 시간 오지게 김)
    # real_cand.sort()
    for one in real_cand:
        one = set(one)
        if one not in answer and len(one) == len(banned_id):
            answer.append(one)
    print(answer)
    return len((answer))



# 처음부터 하나씩 비교한다
# 별이면 다음문자로 넘어가서 비교한다
# banned_id 별로 가능한 후보군을 리스트화해둔다
# 만들어진 리스트들 에서 중복없이 뽑는 경우의 수

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

print(solution(user_id, banned_id))