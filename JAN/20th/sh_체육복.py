def solution(n, lost, reserve):
    
    lost.sort()a
    reserve.sort()
    tmp=[]
    
    for student in lost:
        tmp.append(student)
    
    for student in tmp:
        if student in reserve:
            reserve.remove(student)
            lost.remove(student)
    
    borrow = 0
    for student in lost:
        if student-1 in reserve:            
            reserve.remove(student-1)
            borrow += 1
        elif student+1 in reserve:            
            reserve.remove(student+1)
            borrow += 1
    
    answer = n - len(lost) + borrow
    
    return answer