def solution(k, room_number):
    room_dic = {}
    answer = []
    for room in room_number:
        n = room
        visit = [n]
        while n in room_dic:
            n = room_dic[n]
            visit.append(n)
        answer.append(n)
        for j in visit:
            room_dic[j] = n+1
    return answer

solution(10, [1,3,4,1,3,1])