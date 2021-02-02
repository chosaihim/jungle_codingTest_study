# https://programmers.co.kr/learn/courses/30/lessons/49189 가장 먼 노드
import collections
n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


def solution(n, edge):
    arr = [[] for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    visited = [0 for _ in range(n+1)]

    for e in edge:
        arr[e[1]].append(e[0])
        arr[e[0]].append(e[1])

    deque = collections.deque([[1,0]])     # vertex 1, depth 0

    while deque:
        vertex, depth = deque.popleft()

        if visited[vertex] == 0:
            dist[vertex] = depth
            visited[vertex] = 1
            for node in arr[vertex]:
                if visited[node] == 0:
                    deque.append([node, depth+1])

    m = max(dist)
    return dist.count(m)


print(solution(n,edge))