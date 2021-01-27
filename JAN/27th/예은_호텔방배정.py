# 정확도만
# def solution(k, room_number):
#     answer = []
#     hotel = [i for i in range(1, k + 1)]
#     for one in room_number:
#         if one in hotel:
#             answer.append(hotel.pop(hotel.index(one)))
#         else:
#             # 일치하는 방이 없으면 그 숫자 이후꺼 쭉 봐서 있으면 바로 배정
#             for room in hotel:
#                 if (room > one):
#                     answer.append(hotel.pop(hotel.index(room)))
#                     break
#     return answer

room_number = [1,3,4,1,3,1]
k = 10

import sys
sys.setrecursionlimit(10 ** 7)


def find_empty(one, node):
    if one not in node:  # 빈방이면 바로 할당
        node[one] = one + 1
        return one
    else: # 빈 방 아니면 재귀
        empty_room = find_empty(node[one], node)
        node[one] = empty_room + 1
        return empty_room


def solution(k, room_number):
    node = {}  # {할당한 방 : 직후 빈방 }
    answer = []
    for one in room_number:
        find_empty(one, node)
    answer = list(node.keys())
    return answer

print(solution(k, room_number))