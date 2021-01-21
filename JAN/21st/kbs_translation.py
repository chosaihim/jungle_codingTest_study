# 프로그래머스 단어변환
import sys
from collections import deque

def bfs(x, target, words):
    queue = deque()
    queue.append((x, 0))
    count = 0
    word_len = len(words[0])
    visited = [True for _ in range(len(words))]
    while queue:
        x, count = queue.popleft()
        if x==target:
            return count
        for i in range(len(words)):
            spell_check = 0
            if visited[i]:
                for j in range(word_len):
                    if x[j]!=words[i][j]:
                        spell_check += 1
            if spell_check==1:
                visited[i] = False
                count += 1
                queue.append((words[i], count))


def solution(begin, target, words):
    if target not in words:
        return 0
    answer = bfs(begin, target, words)
    


    return answer

print(solution('hit', 'cog', ['hot', 'dot', 'dog', 'lot', 'log', 'cog']))