import sys
def solution(triangle) :
    answer = 0
    height = len(triangle)
    cache = [[0 for _ in range(height + 1)] for _ in range(height + 1)]
    for h in range(1, height) :
        for idx in range(h) :
            cache[h][idx] = triangle[h][idx]
    cache[0][0] = triangle[0][0]
    for h in range(1, height) :
        for idx in range(h) :
            cache[h][idx] += max(cache[h - 1][idx - 1], cache[h - 1][idx])
            if h == height - 1 : 
                answer = max(answer , cache[h][idx])
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
