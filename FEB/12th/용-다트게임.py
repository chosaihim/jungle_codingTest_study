# https://programmers.co.kr/learn/courses/30/lessons/17682

dartResult = "1S2D*3T"

# print(dart)    


def solution(dartResult):
    dart = list(dartResult)
    number = []
    skip = False
    for i in range(len(dart)):
        if skip == True:
            skip = False
            continue


        # 숫자인가요
        elif dart[i] == "0":
            number.append(0)
        
        elif dart[i] == "1":
            if i + 1 < len(dart):
                if dart[i+1] == "0":
                    number.append(10)
                    skip = True
                else:
                    number.append(1)


        elif dart[i] == "2":
            number.append(2)

        elif dart[i] == "3":
            number.append(3)

        elif dart[i] == "4":
            number.append(4)

        elif dart[i] == "5":
            number.append(5)

        elif dart[i] == "6":
            number.append(6)

        elif dart[i] == "7":
            number.append(7)

        elif dart[i] == "8":
            number.append(8)

        elif dart[i] == "9":
            number.append(9)

        # SDT
        elif dart[i] == "S":
            continue
        elif dart[i] == "D":
            number[-1] = number[-1]**2
        elif dart[i] == "T":
            number[-1] = number[-1]**3
        
        # 스타/아차
        elif dart[i] == "*":
            if len(number) == 1:
                number[-1] = number[-1]*2
            else:
                number[-1] = number[-1]*2
                number[-2] = number[-2]*2

        elif dart[i] == "#":
            number[-1] = number[-1]*(-1)

    answer = sum(number)

    return answer

print(solution(dartResult))