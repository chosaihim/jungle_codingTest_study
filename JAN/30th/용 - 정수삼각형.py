triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
def solution(triangle):
    depth = len(triangle)
    dp = list([0 for _ in range(depth)] for _ in range(depth))
    dp[0][0] = triangle[0][0]
    for i in range(1, depth):
        for j in range(len(triangle[i])):
            # 맨 왼쪽이면
            if j == 0:
                dp[i][j] = dp[i-1][0] + triangle[i][j]
            elif j == len(triangle[i])-1:
                dp[i][j] = dp[i-1][len(triangle[i-1])-1] + triangle[i][j]
            else:
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]

    answer = max(dp[depth-1])
    return answer

result = solution(triangle)
print(result)