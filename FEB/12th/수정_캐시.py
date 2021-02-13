# https://programmers.co.kr/learn/courses/30/lessons/17680
import collections


def solution(cacheSize, cities):
    que = collections.deque(maxlen=cacheSize)
    time = 0

    for city in cities:
        city = city.lower()
        if city in que:
            que.remove(city)
            time += 1
        else:
            time += 5
        que.append(city)
    return time