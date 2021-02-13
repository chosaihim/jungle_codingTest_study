# https://programmers.co.kr/learn/courses/30/lessons/12948

def solution(phone_number):
    stk = []
    phone_number = list(phone_number)
    l = len(phone_number)
    for i in range(l,l-4,-1):
        tmp = phone_number.pop()
        stk.append(tmp)
    str=''
    for i in range(l-4):
        str += '*'
    for i in range(4):
        str += stk.pop()
    return str