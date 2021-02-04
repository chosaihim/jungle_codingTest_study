import sys

relation = [["a","b","c"],["1","b","c"],["a","b","4"],["a","5","c"]]
def solution(relation) :
    answer = 0
    column = len(relation[0])
    row = len(relation)
    print(f"column :: {column}, row :: {row}")
    usedCheck = [False] * (1 << column)
    for i in range(1 << column) :
        bitmask = [0] * column
        restart = False
        for j in range(column) :
            if i & (1 << j) :
                bitmask[j] = 1
        print(f"Case :: {bitmask}")
        for j in range(column) :
            if bitmask[j] :
                for j in range(i) :
                    if usedCheck[j & i] :
                        restart = True
                        break
        if restart :
            continue
        checkList = []
        for k in range(row) :
            buff = []
            for j in range(column) :
                if bitmask[j] == 1 :
                    buff.append(relation[k][j])
            checkList.append(buff)
        print(checkList)
        print(list(set([tuple(check) for check in checkList])))
        if len(checkList) == len(list(set([tuple(check) for check in checkList]))) : 
            print(f"Candidate Keys -> {checkList}")
            usedCheck[i] = True
            answer += 1
        else :
            print("No keys.")
    return answer
