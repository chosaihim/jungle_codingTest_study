import math, collections

def solution(n, stations, w):
    #
    start = 1
    cnt = 0
    for s in stations:
        left = s - w
        right = s + w
        if left <= start <= right:
            start = right+1
            continue
        distance = left-start
        cnt += math.ceil(distance/(2*w+1))
        print(cnt)
        start = right+1
    if start <= n:
        distance = n-start+1
        cnt += math.ceil(distance / (2 * w + 1))

    return cnt