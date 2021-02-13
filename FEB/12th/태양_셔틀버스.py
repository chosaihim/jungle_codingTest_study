from collections import deque
def solution(n, t, m, timetable):
    answer = -1
    crew = []
    bus = [9 * 60]

    def parseTime(time : str) :
        hm = list(time.split(':'))
        return int(hm[0]) * 60 + int(hm[1])
        

    for i in range(len(timetable)) :
        crew.append(parseTime(timetable[i]))
    crew = deque(sorted(crew))

    for i in range(n - 1) :
        bus.append(bus[0] + (i+1) * t)

    last_take_cdx = 0
    for bdx in range(len(bus)) : # 매 버스에 대해서
        take = 0
        for cdx in range(last_take_cdx, len(crew)) : # 마지막 탑승자 부터 크루 전부에 대해서
            print(f'{bdx} 버스({bus[bdx]})에 : {cdx} 번째 crew({crew[cdx]})가 가능?')
            if bdx == n - 1 : # 마지막 버스다
                if take == m - 1 : # 한 버스 허용량 직전
                    if crew[cdx] <= bus[bdx]: # 현재 크루가 마지막 버스 마지막 자리를 차지할수 있는 상황
                        answer = crew[cdx] - 1
                    else : # 못태우는 크루만 있을 경우
                        answer = bus[bdx]
                    last_take_cdx = cdx + 1
                    break
            if crew[cdx] <= bus[bdx] : # 크루가 탑승할때
                last_take_cdx = cdx + 1
                print(f'{bdx} 버스({bus[bdx]})에 탑승 : {cdx} 번째 crew ({crew[cdx]})')
                take += 1
                if take == m :
                    break;
        
    if answer == -1 :
        if last_take_cdx == len(crew) : # crew는 전부 탑승한 상태 버스가 남음
            answer = bus[n - 1]
        else : # crew가 아무도 못탔고, 내가 취사 선택 가능할 때
            answer = bus[n - 1]
    #PARSING
    hh = answer // 60
    mm = answer % 60
    return (str(hh) if hh >= 10 else '0' + str(hh)) + ':' + (str(mm) if mm >= 10 else '0' + str(mm))
