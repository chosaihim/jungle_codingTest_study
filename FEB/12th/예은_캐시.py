from collections import deque

def solution(cacheSize, cities):
    answer = 0
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        cities = [one.lower() for one in cities]
        cities_deque = deque()
        cities_deque.append(cities[0])
        answer  = 5
        for i in range(1, len(cities)):
            if cities[i] in cities_deque:
                cities_deque.remove(cities[i])
                answer += 1
            else:
                if len(cities_deque) == cacheSize:
                    cities_deque.popleft()
                answer += 5
            cities_deque.append(cities[i])
    return answer

# test1
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

# test2
# cacheSize= 3
# cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]

# test3
# cacheSize = 2
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]

# test5
cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]

# test6
# cacheSize = 0
# cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]


print(solution(cacheSize, cities))