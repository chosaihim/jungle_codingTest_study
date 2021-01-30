# 대각선 아래 오른쪽, 왼쪽 이니까 행+1,열그대로    행+1, 열+1
# 지나가면서 자기 자리까지 오기까지의 최댓값으로 그 자리를 갱신하면서 온다
# 이동한 자리 기준이면 a[i][j]에서는 max(a[i][j] + a[i-1][j], a[i][j] + a[i-1][j-1])

def solution(triangle):
    answer = 0
    for i in range(1, len(triangle)):
        triangle[i][0] += triangle[i-1][0]
        triangle[i][i] += triangle[i-1][i-1]

    for i in range(1, len(triangle)):
        for j in range(1, len(triangle[i]) - 1):
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j], triangle[i][j] + triangle[i-1][j-1])

    answer = max(triangle[len(triangle)-1])
    return answer


triangle = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]
print(solution(triangle))
