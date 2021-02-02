def solution(a):
    import sys
    import heapq as hq
    answer = 1
    n=len(a)

    right = a[1::]
    hq.heapify(right)
    left = set()
    left_min = sys.maxsize
    
    for i in range(n-1):
        #is_possible
        if a[i] < left_min or a[i] < right[0]:
            answer += 1
        #update left_min
        if a[i] < left_min:
            left_min = a[i]
        left.add(a[i])
        #update right_min
        if right[0] == a[i+1]:
            hq.heappop(right)
            while right and right[0] in left:
                hq.heappop(right)

    return answer