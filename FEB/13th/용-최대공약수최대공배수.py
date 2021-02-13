# https://programmers.co.kr/learn/courses/30/lessons/12940

def solution(n, m):
    # 최대공약수
    t = n
    while t > 1:
        if n%t == 0 and m%t == 0:
            break
        t -= 1
    
    i = 1
    
                
    answer = []
    return answer