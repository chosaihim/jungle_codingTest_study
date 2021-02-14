# https://programmers.co.kr/learn/courses/30/lessons/17677

str1 = "aa1+aa2"
str2 = "AAAA12"

def parsing(string):
    tmp = list(string.lower())
    letter = []
    rtn = []
    # 문자만 추려내기
    for i in range(len(tmp)-1):
        if not 97 <= ord(tmp[i]) <= 122: continue
        if not 97 <= ord(tmp[i+1]) <= 122: continue
        letter.append(tmp[i]+tmp[i+1])
        
    
    # 원소추가
    # 중복된 문자열이 있어도 set 안에 모두 들어갈 수 있게 해야한다.
    # tmp_bin : 딕셔너리형
    tmp_bin = {}
    num = 0
    for i in letter:
        if i not in tmp_bin:
            num = 1
        else:
            num = tmp_bin[i] + 1
        tmp_bin[i] = num
        rtn.append(i+str(num))
    return rtn


def solution(str1, str2):
    string1 = set(parsing(str1))
    string2 = set(parsing(str2))
    plus = string1 | string2
    share = string1 & string2
    if len(share) == 0 and len(plus) == 0:
        return 65536
    else:
        answer = int(len(share)/len(plus)*65536)
        return answer

print(solution(str1,str2))