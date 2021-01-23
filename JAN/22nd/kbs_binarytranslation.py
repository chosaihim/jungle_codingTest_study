import sys

zero_count = 0
translation_cnt = 0
def translation(s):
    global zero_count
    global translation_cnt

    if s == '1':
        return 
    translation_cnt += 1
    length = 0
    for word in s:
        if word == '1':
            length += 1
        else:
            zero_count += 1
    translation(bin(length)[2:])
    


def solution(s):
    global zero_count
    global translation_cnt
    translation(s)

    answer = [translation_cnt, zero_count]
    # print(answer)
    return answer

# solution("110010101001")