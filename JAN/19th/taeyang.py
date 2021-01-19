import sys
debug = True
if debug : sys.stdin = open('input.txt', 'r')

n = int(sys.stdin.readline().rstrip())
times = list(map(int, sys.stdin.readline().rstrip().split()))

def solution(n, times) :
    times.sort()
    start, end = 0, times[0] * n
    while start < end :
        mid = (start + end) // 2
        print(mid)
        sum = 0
        for t in times :
            sum += mid // t
        if sum >= n :
            end = mid
        elif sum < n :
            start = mid + 1
    return (start + end) // 2

print(solution(n, times))
