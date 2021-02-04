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

    if len(column_list) >= 4:
        three_combilist = list(combinations(column_list,4))
        for x, y, z, a in three_combilist:
            flag = False
            for check in havetocheck_list:
                if check.issubset({x,y,z,a}):
                    flag = True
            if flag:
                continue
            else:
                three_set = set()
                for i in range(row):
                    three_set.add((relation[i][x],relation[i][y],relation[i][z],relation[i][a]))
                if len(three_set) == row:
                    answer += 1
                    havetocheck_list.append({x,y,z,a})
    else:
        return answer        

    if len(column_list) >= 5:
        three_combilist = list(combinations(column_list,5))
        for x, y, z, a, b in three_combilist:
            flag = False
            for check in havetocheck_list:
                if check.issubset({x,y,z,a,b}):
                    flag = True
            if flag:
                continue
            else:
                three_set = set()
                for i in range(row):
                    three_set.add((relation[i][x],relation[i][y],relation[i][z],relation[i][a], relation[i][b]))
                if len(three_set) == row:
                    answer += 1
                    havetocheck_list.append({x,y,z,a,b})
    else:
        return answer    

    if len(column_list) >= 6:
        three_combilist = list(combinations(column_list,6))
        for x, y, z, a, b, c in three_combilist:
            flag = False
            for check in havetocheck_list:
                if check.issubset({x,y,z,a,b,c}):
                    flag = True
            if flag:
                continue
            else:
                three_set = set()
                for i in range(row):
                    three_set.add((relation[i][x],relation[i][y],relation[i][z],relation[i][a], relation[i][b], relation[i][c]))
                if len(three_set) == row:
                    answer += 1
                    havetocheck_list.append({x,y,z,a,b,c})
    else:
        return answer    

    if len(column_list) >= 7:
        three_combilist = list(combinations(column_list,7))
        for x, y, z, a, b, c, d in three_combilist:
            flag = False
            for check in havetocheck_list:
                if check.issubset({x,y,z,a,b,c,d}):
                    flag = True
            if flag:
                continue
            else:
                three_set = set()
                for i in range(row):
                    three_set.add((relation[i][x],relation[i][y],relation[i][z],relation[i][a], relation[i][b], relation[i][c], relation[i][d]))
                if len(three_set) == row:
                    answer += 1
                    havetocheck_list.append({x,y,z,a,b,c,d})
    else:
        return answer 

    if len(column_list) >= 8:
        three_combilist = list(combinations(column_list,8))
        for x, y, z, a, b, c, d, e in three_combilist:
            flag = False
            for check in havetocheck_list:
                if check.issubset({x,y,z,a,b,c,d,e}):
                    flag = True
            if flag:
                continue
            else:
                three_set = set()
                for i in range(row):
                    three_set.add((relation[i][x],relation[i][y],relation[i][z],relation[i][a], relation[i][b], relation[i][c], relation[i][d], relation[i][e]))
                if len(three_set) == row:
                    answer += 1
                    havetocheck_list.append({x,y,z,a,b,c,d,e})
    else:
        return answer 
                


    
    return answer

print(solution([["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]))