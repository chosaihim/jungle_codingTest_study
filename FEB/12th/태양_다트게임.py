dartResult = "1S*2T*3S"

def solution(dartResult):
    obj_list = list(dartResult)
    idx = 0
    answer = 0
    p = 1
    gob = 1
    prev = False
    while len(obj_list) :
        value = 0
        obj = obj_list.pop()
        if ord(obj) <= ord('9') and ord(obj) >= ord('0') :
            if obj == '0' and len(obj_list) and obj_list[-1] == '1':
                obj_list.pop()
                value = 10
            else :
                value = int(obj)
            answer += (pow(value, p) * gob)
            value = 0
            if prev : 
                prev = False
                gob = 2
            else :
                gob = 1
        if obj == '#' :
            gob = -gob
        if obj == '*' :
            gob *= 2
            prev = True
        if obj == 'S' :
            p = 1
        if obj == 'D' :
            p = 2
        if obj == 'T' :
            p = 3

    return answer

print(solution(dartResult))
