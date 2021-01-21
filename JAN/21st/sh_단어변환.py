words  = ["hot", "dot", "dog", "lot", "log", "cog"]
begin  = "hit"
target = "cog"

from collections import deque

def solution(begin, target, words): 
    

    def bfs(begin, target, words):
        visited = []    # 방문한 곳을 기록
        queue = []  # 큐에 시작점을 줄 세움

        depth = 0
        
        queue.append([begin,0])

        while queue:    # 큐가 빌떄까지 탐색을 계속
            
            comp, depth = queue.pop(0)

            if ((comp[1] == target[1]) and (comp[2] == target[2])) or ((comp[1] == target[1]) and (comp[2] == target[2])) or ((comp[1] == target[1]) and (comp[2] == target[2])):
                depth = depth + 1
                return depth

            for word in words:
                
                if (comp[1] == word[1]) and (comp[2] == word[2]):
                    queue.append([word,depth+1]);
                
                elif (comp[0] == word[0]) and (comp[2] == word[2]):
                    queue.append([word,depth+1]);

                elif (comp[0] == word[0]) and (comp[1] == word[1]):
                    queue.append([word,depth+1])

        return 0

    answer = bfs(begin,target,words)
    return answer