# 가장 먼 노드
from collections import deque

def bfs(n, edge, graph):
    queue = deque()
    queue.append((1,0))
    max_depth = 0
    node_count = 0
    visited = [True for _ in range(n+1)] # 0이 포함된 개수
    visited[1] = False
    while queue:
        node, depth = queue.popleft()
        if depth > max_depth:
            node_count = 0
        max_depth = max(max_depth, depth)
        if max_depth==depth:
            node_count += 1
        for i in graph[node]:
            if visited[i]:
                queue.append((i, depth+1))
                visited[i] = False
    return node_count



def solution(n, edge):
    graph = [[] for _ in range(n+1)] # 0이 포함된 개수
    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)
    
    answer = bfs(n, edge, graph)
    
    return answer

print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))