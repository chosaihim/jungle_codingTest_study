cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

from collections import deque

def solution(cacheSize, cities):
    cash = deque(maxlen=cacheSize)
    answer = 0
    for i in cities:
        tmp = i.lower()
        if tmp in cash:
            cash.remove(tmp)
            answer += 1
        else:
            answer += 5
        cash.append(tmp)
    return answer