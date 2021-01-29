N = 2
number = 11

def find(N, number):
    if number == N:
        return 1
    visited = {}
    prev = [[] for _ in range(9)]
    cnt = 1
    prev[1].append(N)
    visited[N] = 1
    setting = N

    # key가 이미 들어있는지 확인하고, 없으면 visited에 넣는다.
    def is_visited(key, visited, prev, cnt):
        a = visited.get(key, 0)
        if a == 0:
            print("hi")
            prev[cnt].append(key)
            visited[key] = 1
            return
        else:
            return
    # cnt 2 부터 시작한다.
    while cnt < 8:
        print("prev:", prev)
        cnt += 1
        lp = 1
        rp = cnt-1
        while lp < cnt:
            for i in prev[lp]:
                for j in prev[rp]:
                    print("i:",i,"j:",j)
                    if lp + rp > 8:
                        continue
                    # 더하기
                    new = i + j
                    print("new:", new)
                    if new == number:
                        return cnt
                    is_visited(new, visited, prev, cnt)

                    # 빼기
                    new = i - j
                    if new == number:
                        return cnt
                    if new > 0:
                        is_visited(new, visited, prev, cnt)
                    
                    # 곱하기
                    new = i * j
                    if new == number:
                        return cnt
                    is_visited(new, visited, prev, cnt)

                    # 나누기
                    if j == 0:
                        continue
                    new = i // j
                    if new == number:
                        return cnt
                    is_visited(new, visited, prev, cnt)
            lp += 1
            rp -= 1
        setting = 10**(cnt-1)*N+setting
        print("cnt:", cnt, "setting:", setting)
        prev[cnt].append(setting)
        if setting == number:
            return cnt
    return -1
    
answer = find(N, number)
print(answer)
