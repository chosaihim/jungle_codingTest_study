triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]	

def solution(triangle):

#재귀
    # cache = [[None for _ in range(len(triangle))] for _ in range(len(triangle))]
    
    # def max_route(row,col):
    #     answer = 0
    #     if row == 0: return triangle[0][0]
    #     if cache[row][col]: return cache[row][col]
        
    #     for i in range(-1,1,1):
    #         if row-1 >= 0 and 0 <= col+i <= row-1:
    #             answer = max(answer, triangle[row][col] + max_route(row-1,col+i))
        
    #     cache[row][col] = answer
    #     return answer

    # route = 0
    # for i in range(len(triangle)):
    #     route = max(route, max_route(len(triangle)-1,i))    
    # return route

# dp 테이블
    max_depth = len(triangle)
    dp = [[None for _ in range(len(triangle))] for _ in range(len(triangle))]
    dp[0][0] = triangle[0][0]

    for i in range(1,max_depth):
        dp[i][0] = dp[i-1][0] + triangle[i][0]
        dp[i][i] = dp[i-1][i-1] + triangle[i][i]
        for j in range(1,i):
            dp[i][j] = triangle[i][j] + max(dp[i-1][j-1],dp[i-1][j])
    
    temp = [dp[max_depth-1][i] for i in range(max_depth)]
    return max(temp)

print(solution(triangle))