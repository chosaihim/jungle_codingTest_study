from collections import deque

def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    dist = [0] * (n+1)
    for one in edge:
        graph[one[0]].append(one[1])
        graph[one[1]].append(one[0])

    bfs(graph, dist)
    answer = dist.count(max(dist))
    return answer

def bfs(graph, dist):
    queue = deque([1])
    dist[1] = 1
    while queue:
        x = queue.popleft()
        for one in graph[x]:
            if dist[one] == 0:
                dist[one] = dist[x] + 1
                queue.append(one)


