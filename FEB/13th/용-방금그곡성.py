# https://programmers.co.kr/learn/courses/30/lessons/17683

# case 3
m = "ABC"
musicinfos = ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]

m = "ABC"
musicinfos = ["00:00,00:05,HI,ABC#"]

m = 'A#'
musicinfos = ['13:00,13:02,HAPPY,B#A#']

def parsing(time):
    part_time = time.split(":")
    return int(part_time[0])*60+int(part_time[1])

def find(m1,m2,start,end):
    time = end - start + m2.count('#')

    # 뮤직 스타트
    i = 0
    # m2를 재생하면서
    for j in range(len(m2)):
        i += 1

        # 시간 초과
        if i > time:
            break

        # m1과 일치하는 부분이 있는지 본다.
        if m2[j] != m1[0]: continue
        else:
            j2 = j
            skip = False

            # 계속 비교해봅시다
            for k in range(len(m1)):
                if j2+k == len(m2):
                    j2 = -1*k

                if m2[j2+k] != m1[k]:
                    skip = True
                    break
            
            # 끝까지 일치했는가
            if skip == True: continue
            else:
                # #예외처리
                if j2 + k != len(m2)-1 and m2[j2+k+1] == '#' : continue
                else:
                    return True
    return False

                

def solution(m, musicinfos):
    m1 = list(m)
    cand = []
    
    for k in musicinfos:
        song = k.split(",")
        cnt = 0
        for i in song:

            # cnt = 0 : 음악 시작
            if cnt == 0:
                start = parsing(i)
                cnt += 1
                continue
            
            # cnt = 1 : 음악 끝
            if cnt == 1:
                end = parsing(i)
                cnt += 1
                continue

            # cnt = 2 : 음악 제목
            if cnt == 2:
                title = i
                cnt += 1
                continue

            # cnt = 3 : 분석
            if cnt == 3:
                m2 = list(i)
                if find(m1,m2,start,end):
                    cand.append([end-start, title])
    
    max_len = 0
    answer = '(None)'
    for j in cand:
        if j[0] > max_len:
            max_len = j[0]
            answer = j[1]
    return answer

print(solution(m,musicinfos))