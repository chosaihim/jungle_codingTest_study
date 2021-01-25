import sys
from collections import deque

def solution(n, edge):
    max_depth = 0
    queue = deque()
    visited = [False for _ in range(n + 1)]
    #vertex = [[False for _ in range(n + 1)] for _ in range(n + 1)]
    vertex = [[] for _ in range(n + 1)]
    for e in edge :
        vertex[e[0]].append(e[1])
        vertex[e[1]].append(e[0])
    visited[1] = True
    depth_cnt = [0 for _ in range(50000 + 1)]
    depth_cnt[0] = 1
    answer = 0
    queue.append((1,0))
    while(queue) :
        node, depth = queue.popleft()
        max_depth = max(depth, max_depth)
        for v in vertex[node] :
                if not visited[v] :
                    visited[v] = True
                    print(v, depth + 1)
                    queue.append((v, depth + 1))
                    depth_cnt[depth + 1] += 1
    answer = depth_cnt[max_depth]
    return answer
