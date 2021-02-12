# 시작시간, 끝나는 시간 기준으로 개수가 변한다
# 시작시간 ~ 시작+1초 , 끝시간 ~ 끝+1초
# 한개에 대해서 이렇게 두번 확인해주면 됨

def solution(lines):
    answer = 0
    calculated = []
    # 시간 parsing, 초 환산, 정렬
    for one in lines:
        parsed_time = one.split(' ')[1].split(':')
        duration = int(float(one.split(' ')[2].split('s')[0])*1000)
        ending_time = int((int(parsed_time[0])*3600 + int(parsed_time[1])*60 + float(parsed_time[2]))*1000)
        start_time = ending_time - duration + 1
        if start_time < 0:
            start_time = 0
        calculated.append([start_time, ending_time])
    calculated.sort(key=lambda x:x[0])
    print(start_time, ending_time, duration)

    length = len(calculated)
    for i in range(length): # 시작 시간 기준
        s_time = calculated[i][0]
        e_time = s_time + 999
        temp = 0
        for j in range(length):
            if calculated[j][0] <= e_time and calculated[j][1] >= s_time:
                temp += 1
        answer = max(answer, temp)

    for i in range(length): # 끝 시간 기준
        s_time = calculated[i][1]
        e_time = s_time + 999
        temp = 0
        for j in range(length):
            if calculated[j][0] <= e_time and calculated[j][1] >= s_time:
                temp += 1
        answer = max(answer, temp)
    return answer

lines =	["2016-09-15 00:00:00.000 3s"]
lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
# lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s",
#          "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s",
#          "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s",
#          "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s",
#          "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

print(solution(lines))