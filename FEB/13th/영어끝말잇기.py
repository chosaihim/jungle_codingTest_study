def solution(n, words):
    import math
    answer = []
    prev_w = "."
    save_w = set()
    for i,w in enumerate(words):
        if (i != 0 and prev_w[-1] != w[0]) or w in save_w:
            break
        save_w.add(w)
        prev_w = w
    else: return [0,0]

    if (i+1)%n:
        return [(i+1)%n, math.ceil((i+1)/n)]
    else:
        return [n, math.ceil((i+1)/n)]
