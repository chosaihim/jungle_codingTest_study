from collections import deque

def solution(begin, target, words): 
    
    if target not in words: return 0
    
    def bfs(begin, target, words):
        
        queue = []
        depth = 0       
        max_depth = len(words)
        
        queue.append([begin,0])
        while queue:
            
            comp, depth = queue.pop(0)            

            if comp == target:    return depth            
            if depth > max_depth: return 0
            
            for word in words:
                diff = 0
                
                for i in range(len(word)):
                    if comp[i] != word[i]:
                        diff += 1
                if diff == 1:
                    queue.append([word,depth+1]);
                        
        return 0
        
    return bfs(begin,target,words)