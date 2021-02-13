# https://programmers.co.kr/learn/courses/30/lessons/12925
s = '1234'

def solution(s):
    stack = []
    a = list(s)
    flag = 1
    answer = 0
    for i in range(len(s)):
        if i == 0:
            if a[i] == "+":
                flag = 1
            elif a[i] == "-":
                flag = -1
            elif a[i] == "0":
                stack.append(0)
            elif a[i] == "1":
                stack.append(1)
            elif a[i] == "2":
                stack.append(2)
            elif a[i] == "3":
                stack.append(3)
            elif a[i] == "4":
                stack.append(4)
            elif a[i] == "5":
                stack.append(5)
            elif a[i] == "6":
                stack.append(6)
            elif a[i] == "7":
                stack.append(7)
            elif a[i] == "8":
                stack.append(8)
            elif a[i] == "9":
                stack.append(9)

        else:
            if a[i] == "0":
                stack.append(0)
            elif a[i] == "1":
                stack.append(1)
            elif a[i] == "2":
                stack.append(2)
            elif a[i] == "3":
                stack.append(3)
            elif a[i] == "4":
                stack.append(4)
            elif a[i] == "5":
                stack.append(5)
            elif a[i] == "6":
                stack.append(6)
            elif a[i] == "7":
                stack.append(7)
            elif a[i] == "8":
                stack.append(8)
            elif a[i] == "9":
                stack.append(9)
    for j in range(len(stack)):
        answer = answer + stack[j]*10**(len(stack)-1-j) 
    answer = answer * flag

    return answer

