a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]
#result = 6

def solution(a):
    answer = 2
    
    # 나를 중심으로 양쪽의 풍선이 둘다 나보다 작으면 실패
    # 나를 중심으로 양쪽으로 최소값이 나보다 작으면 실패
    # 왜냐면1. 양쪽으로 나보다 작은 최소값이 있었다면 내 양옆으로 살아남아서 와도 문제
    # 왜냐면2. 내 옆으로 안오려면 어쨌든 작은 값이 터져야하니깐 작은값 터뜨릴 기회를 잃어버림!
    # 양쪽 끝 제끼고 시작!
    
    left_min = a[0]
    
    right_min = a[-1]
    right_mins = [0]*len(a)
    
    for i in range(len(a)-1,-1,-1):
        right_mins[i] = min(a[i],right_min)
        right_min = right_mins[i]
    
    for i in range(1, len(a)-1):
    
        if a[i] < left_min or a[i] < right_mins[i+1]:
            answer += 1        
        left_min = min(left_min,a[i])
    
    return answer

print(solution(a))