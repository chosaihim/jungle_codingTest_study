# https://www.youtube.com/watch?v=811QZGDysx0

import sys
sys.setrecursionlimit(10**6)

k = 10
room_number = [1, 3, 4, 1, 3, 1]
chk = {}
answer = []

def find(node):
    # rn이 없으면 
    if node not in chk:
        answer.append(node)
        result = node+1
        chk[node] = result
        return result
        
    # rn이 있으면
    else:
        next_node = chk[node]
        result = find(next_node)
        chk[node] = result
        return result
    
for r in room_number:
    find(r)
    

print(answer)
    