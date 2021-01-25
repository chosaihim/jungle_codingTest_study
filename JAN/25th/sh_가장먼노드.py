import sys

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

def solution(n, edge):
    
    graph = [[] for _ in range(n+1)]
    dist = [0 for _ in range(n+1)]
    visited= [0 for _ in range(n+1)]

    for ed in edge:
        graph[ed[0]].append(ed[1])
        graph[ed[1]].append(ed[0])

    queue =[[1,0]]

    while queue:
        vertex,depth = queue.pop(0)

        if visited[vertex] == 0:
            dist[vertex] = depth
            visited[vertex] = 1
            for node in graph[vertex]:
                if visited[node] == 0:
                    queue.append([node,depth+1])
    
    answer = dist.count(max(dist))
    return answer

print(solution(n, edge))

