
def solution(lines):
    data = []
    time = []
    time_t = []
    max_v = 0
    S = 0

    # 1. 시각과 시간 파싱
    for l in lines:
        data = l.split()
        h, m, tmp= data[1].split(':')
        h = int(h)
        m = int(m)
        s, ms = tmp.split('.')

        H = h * 3600 * 1000
        M = m * 60 * 1000
        S = int(s) * 1000
        S = H + M + S + int(ms)

        time.append(S)
        S = 0
        r = data[2].replace('s','')
        t =float(r) * 1000
        time_t.append(int(t))

    # 2. 각 구간 전후로 1초동안 몇 개의 처리량이 있는지 max값 비교
    l = len(time)
    for i in range(l):
        bf = time[i] - time_t[i]
        af = time[i]
        cnt = 0
        for j in range(l):
            start = time[j]-time_t[j]
            end = time[j]
            if start < bf+1000 and bf <= end:
                cnt += 1
        max_v = max(max_v, cnt)
        cnt = 0
        for j in range(l):
            start = time[j] - time_t[j] +1
            end = time[j]
            if start < af+1000 and af <= end:
                cnt += 1
        max_v = max(max_v, cnt)
    return max_v
