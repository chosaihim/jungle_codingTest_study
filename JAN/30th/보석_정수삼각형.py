def solution(triangle):
    answer = 0
    triangle_level = len(triangle) # 예시에서는 5 인덱스는 0~4
    dp_table = [[] for _ in range(triangle_level)]
    dp_table[0].append(triangle[0][0])

    for i in range(1, triangle_level): # 1부터 4까지
        for j in range(i+1): # 0부터 i 까지
            upper_left = 0
            upper_right = 0
            if j != 0:
                upper_left = dp_table[i-1][j-1]
            if j != i:
                upper_right = dp_table[i-1][j]
            dp_table[i].append(max(upper_left, upper_right) + triangle[i][j])

    
    answer = max(dp_table[-1])



    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))