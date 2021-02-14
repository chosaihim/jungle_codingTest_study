name = "JAZ"
# name = 'BBABA'
# name = 'BBBAAB'
# name = 'BBAABB'


from collections import deque
def ordering(name):
    name_list = list(name)
    for i in range(len(name_list)):
        name_list[i] = ord(name_list[i])
    return name_list


# A : 65 / Z :90 / mid : 77.5
def updown(letter):
    # 만약 65~77까지면 A에서부터 움직인다.
    if 65 <= letter <= 77:
        return letter-65
    else:
        return 91-letter


# cursor는 idx=0부터 시작한다.
# 가장 가까운 
def leftright(order):
    rtn = 0
    cursor = 0
    order[0] = 0
    while sum(order) > 0:
        left = 1
        right = 1
        print('cursor:', cursor)

        # 좌탐색
        while order[cursor - left] == 0:
            left += 1
        
        # 우탐색
        while order[cursor + right] == 0:
            right += 1
        
        # 왼쪽이 가까운 경우
        if left < right:
            rtn += left
            cursor -= left
        else:
            rtn += right
            cursor += right
        order[cursor] = 0

    return rtn
    
            

def solution(name):
    order = ordering(name)
    que = deque()
    answer = 0
    for i in range(len(order)):
        order[i] = updown(order[i])
        answer += order[i]
 
    # A가 있는 자리는 0이 될 것이다. 좌우로 움직이는 경우의 수는 A만 신경쓰면 된다.
    answer += leftright(order)

    return answer

print(solution(name))