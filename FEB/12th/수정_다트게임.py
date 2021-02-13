dartResult = '1D2S#10S'

def solution(d):
    stk = []
    parse = list(d)
    bf_score = 0
    cur_score = 0
    l = len(parse)
    tmp = 0
    for i in range(l):

        c = parse[i]
        if c == 'S':
            pass
        elif c == 'D':
            tmp = stk.pop()
            tmp = tmp * tmp
            stk.append(tmp)
        elif c == 'T':
            tmp = stk.pop()
            tmp = tmp * tmp * tmp
            stk.append(tmp)
        elif c == '*':
            if i == 2:
                tmp = stk.pop()
                tmp += tmp
                stk.append(tmp)
            else:
                tmp = stk.pop()
                tmp2 = stk.pop()
                tmp += tmp
                tmp2 += tmp2
                stk.append(tmp2)
                stk.append(tmp)
        elif c == '#':
            tmp = stk.pop()
            tmp = tmp * (-1)
            stk.append(tmp)
        else:
            bf_score = cur_score
            cur_score = int(c)
            if bf_score == 1 and cur_score == 0:
                stk.pop()
                stk.append(10)
            else:
                stk.append(cur_score)
        print(stk)
    answer = sum(stk)

    return answer

print(solution(dartResult))