import sys
x = sys.stdin.readline().rstrip()

def deleteZero(x) :
    cnt = 0 
    for i in range(len(x)) :
        if x[i] == '0' :
            cnt += 1
    x = x.replace('0', '')
    return (x, cnt)

def toBinary(x) :
    return (bin(len(x))[2:], 1)

def solution(s) :
    zeroCnt, transCnt = 0, 0
    while len(s) != 1 :
        zcnt, tcnt = 0, 0
        s, zcnt = deleteZero(s)
        s, tcnt = toBinary(s)
        zeroCnt += zcnt
        transCnt += tcnt

    return [transCnt, zeroCnt]

print(solution(x))
