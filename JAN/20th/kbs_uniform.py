def solution(n, lost, reserve):
    answer = n
    lost.sort()
    reserve.sort()
    tmp = []
    for student in lost:
        tmp.append(student)
    
    for lost_student in tmp:
        if lost_student == 4:
            lost_student = lost_student
        if lost_student in reserve:
            lost.remove(lost_student)
            reserve.remove(lost_student)
    
    print(lost, reserve)
    
    for lost_student in lost:
        flag = 0
        if lost_student-1 in reserve:
            flag = 1
            reserve.remove(lost_student-1)
        elif lost_student+1 in reserve:
            flag = 1
            reserve.remove(lost_student+1)
        if flag == 0:
            answer -= 1

    
    return answer

print(solution(5,[1,2,4,5],[2,3,4]))