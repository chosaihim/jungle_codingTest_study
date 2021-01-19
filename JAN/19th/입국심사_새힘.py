##테스트 케이스 7,8 실패

def solution(n, times):
       
    pl = 0
    pr = max(times) * n
    
    min_time = 10**10
    while True:
        
        if n == 0: break
            
        
        pc = (pr+pl)//2
        
        #해당 시간에 검사할 수 있는 사람 수 check
        checked = 0
        for time in times:
            checked += pc//time
        
        
        if checked < n: #검색범위를 뒷쪽으로
            pl = pc + 1
        else:           #검색범위를 앞쪽 절반으로
            pr = pc - 1
            min_time = min(min_time, pc)
        if pl > pr:
            break

    return min_time