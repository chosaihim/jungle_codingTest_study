# https://programmers.co.kr/learn/courses/30/lessons/43164

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]

# DFS
# 우선 출발공항으로 시작하는 티켓을 뽑아 도착공항 알파벳순으로 리스트에 담는다.
# 그리고 순서대로 순회한다. 


from collections import deque
def DFS(start, tickets, route):
    que = []
    route.append(start)
    # 종결조건 : 모든 곳을 탐방했을 경우 
    if not tickets:
        return route
    
    # 현재 공항에서 출발하는 표들을 담는다. 
    for i in tickets:
        if i[0] == start:
            que.append(i)
    
    # 만약 잘못 왔다면 
    if not que:
        return False
    
    que = sorted(que, key = lambda x : x[1])

    # 한 표씩 탐방해본다. 
    for i in que:
        copy_tickets = tickets[:]
        copy_tickets.remove(i)
        copy_route = route[:]

        new_route = DFS(i[1], copy_tickets, copy_route)
        if new_route:
            return new_route


def solution(tickets):
    route = []
    answer = DFS('ICN', tickets, route)
    return answer

print(solution(tickets))