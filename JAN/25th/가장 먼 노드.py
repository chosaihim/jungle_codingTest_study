import sys
from collections import deque

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]

# dfs로 푼다
# 가장 먼 노드로 가면서 최단 경로도 체크해야한다.
# dfs로 끝점을 찾아가면서 경로 갯수를 체크한다.
# 끝점에 도달하면 해당 리스트를 갱신한다. 
# 

visited = [0]*(n+1)
que = deque()
matrix = [[] for _ in range(n+1)]

for i in range(len(edge)):
    a = edge[i][0]
    b = edge[i][1]
    matrix[a].append(b)
    matrix[b].append(a)

for j in matrix[1]:
    que.append(j)
    visited[j] = 1
visited[1] = 1


print(matrix)
while que:
    cand = len(que)
    for k in range(len(que)):
        tmp = que.popleft()
        for l in matrix[tmp]:
            if visited[l] == 0:
                visited[l] = 1
                que.append(l)


print(cand)