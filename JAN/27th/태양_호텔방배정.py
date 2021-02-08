# union-find 학습
import sys
sys.setrecursionlimit(10**7)
def solution(k, room_number):
    def find(a):
        if a not in room:
            room[a] = a
            return a
        room[a] = find(room[a]+1)
        return room[a]
    room = {}
    ans = [0 for _ in range(len(room_number))]
    for i in range(len(room_number)):
        ans[i] = find(room_number[i])
    return ans

def solution2(k, room_number):
    def find(a):
        if a == room[a]:
            return a
        room[a] = find(room[a])
        return room[a]
    def union(a,b):
        a = find(a)
        b = find(b)
        if a == b :
            return
        room[a] = b
        return
    room = [i for i in range(k+1)]
    ans = [0 for _ in range(len(room_number))]
    if len(room_number) ==1:
        return room_number
    for i in range(len(room_number)):
        ans[i] = find(room_number[i])
        union(ans[i],ans[i]+1)
        # room[ans[i]] = find(room_number[i]+1)
    return ans
