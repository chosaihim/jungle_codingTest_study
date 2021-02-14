# 아스키코드값 출력해주는 ord, chr 함수 너무너무 소중
# 소문자a~z : 97~122

def solution(str1, str2):
    answer = 0
    str1 = str1.lower()
    str2 = str2.lower()
    set_str1 = []
    set_str2 = []
    temp = ''
    i = -1
    while(i < len(str1)-1):
        i += 1
        if 97 <= ord(str1[i]) <= 122:
            temp += str1[i]
            if len(temp) == 2:
                set_str1.append(temp)
                temp = ''
                i -= 1
        else:
            temp = ''

    temp = ''
    i = -1
    while(i < len(str2)-1):
        i += 1
        if 97 <= ord(str2[i]) <= 122:
            temp += str2[i]
            if len(temp) == 2:
                set_str2.append(temp)
                temp = ''
                i -= 1
        else:
            temp = ''

    str1_num = dict()
    str2_num = dict()
    for one in set_str1:
        if one in str1_num.keys():
            str1_num[one] += 1
        else:
            str1_num[one] = 1

    for one in set_str2:
        if one in str2_num.keys():
            str2_num[one] += 1
        else:
            str2_num[one] = 1

    print(str1_num)
    print(str2_num)

    # 교집합 구하기
    boonja = 0
    for one in str1_num.keys():
        if one in str2_num.keys():
            boonja += min(str1_num[one], str2_num[one])

    # 합집합 구하기
    boonmo = 0
    for one in str1_num.keys():
        if one in str2_num.keys():
            boonmo += max(str1_num[one], str2_num[one])
        else:
            boonmo += str1_num[one]

    for one in str2_num.keys():
        if one in str1_num.keys():
            continue
        else:
            boonmo += str2_num[one]

    if (len(set_str1) == 0 and len(set_str2) == 0):
        answer = 1
    else:
        answer = boonja / boonmo
    answer = int(answer * 65536 // 1)
    return answer


# test1
str1 = "FRANCE"
str2 = "french"

#test2
str1 = "handshake"
str2 = "shake hands"

#test3
str1 = "aa1+aa2"
str2 = "AAAA12"



print(solution(str1, str2))
