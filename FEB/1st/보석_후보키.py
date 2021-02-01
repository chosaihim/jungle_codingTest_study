from itertools import combinations

def solution(relation):
    answer = 0
    row = len(relation)
    column = len(relation[0])
    column_list = [num for num in range(column)]
    
    for i in range(column):
        one_set = set()
        for j in range(row):
            one_set.add(relation[j][i])
        if len(one_set) == row:
            answer += 1
            column_list.remove(i)
    havetocheck_list = []
    if len(column_list) >= 2:
        two_combilist = list(combinations(column_list,2))
        print(two_combilist)
        for x, y in two_combilist:
            two_set = set()
            for i in range(row):
                two_set.add((relation[i][x], relation[i][y]))
            if len(two_set) == row:
                answer += 1
                havetocheck_list.append({x, y})
        print(havetocheck_list)
    else:
        return answer
        
    if len(column_list) >= 3:
        three_combilist = list(combinations(column_list,3))
        for x, y, z in three_combilist:
            flag = False
            for check in havetocheck_list:
                if check.issubset({x,y,z}):
                    flag = True
            if flag:
                continue
            else:
                three_set = set()
                for i in range(row):
                    three_set.add((relation[i][x],relation[i][y],relation[i][z]))
                if len(three_set) == row:
                    answer += 1
                    havetocheck_list.append({x,y,z})
    else:
        return answer
                


    
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))