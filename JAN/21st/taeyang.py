import sys
from collections import deque
queue = deque()

def bfs(word:str, target, words) :
    while(queue) :
        w, d = queue.popleft()
        if w == target :
            return d
        if d > len(words) :
            return 0
        print(w, d)
        for i in range(len(words)) :
            comp = 0
            for j in range(len(words[i])) :
                if w[j] != words[i][j] :
                    comp += 1
            if comp == 1 :
                queue.append((words[i], d + 1))
    return 0


            

def solution(begin, target, words) :
    print(begin, target, words)
    queue.append((begin,0))
    answer = bfs(begin, target, words)
    return answer
