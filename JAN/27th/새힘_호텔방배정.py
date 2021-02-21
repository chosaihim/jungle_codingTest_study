k = 10
room_number = [1,3,4,1,3,1]

# https://mungto.tistory.com/202
def solution(k, room_number):
    answer = []
    assigned = dict()
    
    for room in room_number:
        room_num = assigned.get(room,0) #get: key에 해당하는 value를 return
        
        # 방 배정이 안되어 있다면, 그방에 바로 넣어드림!
        if not room_num:
            assigned[room] = room + 1
            answer.append(room)
        # 방 배정이 되어 있다면, 그 뒷방으로 배정
        else:
            filled = [room_num]
            while True:
                temp = room_num
                room_num = assigned.get(room_num,0)
                
                if room_num:
                    filled.append(room_num)
                else:
                    answer.append(temp)
                    assigned[temp]=temp+1
                    
                    # 이전에 지나친 방들 다 업데이트 해주기!
                    for idx in filled:
                        assigned[idx] = temp + 1
                    
                    break
                
            
    return answer


print(solution(k, room_number))



# 다른 풀이
# def solution(k, room_number):
#     room_dic = {}
#     ret = []
#     for i in room_number:
#         n = i
#         visit = [n]
#         while n in room_dic:
#             n = room_dic[n]
#             visit.append(n)
#         ret.append(n)
#         for j in visit:
#             room_dic[j] = n+1
#     return ret