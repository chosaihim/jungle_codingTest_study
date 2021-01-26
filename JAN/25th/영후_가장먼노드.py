from collections import deque

n = 6

edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    ary = [[] for _ in range(n + 1)]
    visit = [0 for _ in range(n + 1)]
    que = deque([])
    
    for link in edge :
        ary[link[0]].append(link[1])
        ary[link[1]].append(link[0])

    visit[1] = 1
    for node in ary[1] :
        que.appendleft([node, 0])
        visit[node] = 1

    max_depth = 0
    cnt = 1

    while True :
        flag = 0
        nbr, depth = que.pop()

        for node in ary[nbr] :
            if visit[node] != 1 :
                que.appendleft([node, depth + 1])
                visit[node] = 1
                flag = 1

        if flag == 0 :
            if max_depth == depth :
                cnt += 1
            elif max_depth < depth :
                max_depth = depth
                cnt = 1

        if not que :
            break
    
    return cnt

print(solution(n, edge))