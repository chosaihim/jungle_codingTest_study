from itertools import combinations

relation = [["100", "ryan"  ,"music"   ,"2"],
            ["200", "apeach","math"    ,"2"],
            ["300", "tube"  ,"computer","3"],
            ["400", "con"   ,"computer","4"],
            ["500", "muzi"  ,"music"   ,"3"],
            ["600", "apeach","music"   ,"2"]]

# uniqueness
# minimality

# find all combinations
def solution(relation):
    answer = 0
    
    key_set = []
    col_len = len(relation[0])
    row_len = len(relation)
    indices = [i for i in range(col_len)]
    index_comb = []
    
    # index combination
    for i in range(1, col_len+1):
        combi = combinations(indices,i)
        for comb in combi:
            comb_set = set()
            for c in comb:
                comb_set.add(c)
            index_comb.append(comb)
            
    # print(index_comb)
    
    #check uniqueness
    
    for comb in index_comb:
        # print(f'comb:{comb}')
        
        # make a trial key set with the combination
        trial = set()
        for row in range(row_len):
            onekey = ''
            for col in comb:
                onekey += relation[row][col]
            trial.add(onekey)
        # print(f'tiral:{trial}')
        
        validset_flag = True
        # 이거 총 row 개수와 같다면!!
        if(len(trial) == row_len):
            # print(f'enough entries: {trial}')
            # 이제 이 set의 subset이 존재하지 않는다면
            for key in key_set:
                if key.issubset(comb):
                    validset_flag = False
                    break
            # 추가해주기!
            if validset_flag:
                temp_set = set()
                for c in comb:
                    temp_set.add(c)
                key_set.append(temp_set)
            
        # print(key_set)

    answer = len(key_set)    
    return answer

print(solution(relation))
        # make a trial key set with the combination
        trial = set()
        for row in range(row_len):
            onekey = ''
            for col in comb:
                onekey += relation[row][col]
            trial.add(onekey)
        # print(f'tiral:{trial}')
        
        validset_flag = True
        # 이거 총 row 개수와 같다면!!
        if(len(trial) == row_len):
            # print(f'enough entries: {trial}')
            # 이제 이 set의 subset이 존재하지 않는다면
            for key in key_set:
                if key.issubset(comb):
                    validset_flag = False
                    break
            # 추가해주기!
            if validset_flag:
                temp_set = set()
                for c in comb:
                    temp_set.add(c)
                key_set.append(temp_set)
            
        # print(key_set)

    answer = len(key_set)    
    return answer

print(solution(relation))




#### 해설 #######
# 유일성 :
# 1. 2차원 배열로 들어온 relation[row][col]의 값 중 col이 같은 값을 하나의 set에 넣어서 검증하면 된다고 생각했다.
# 2. 여러 col의 조합이 유일한지 확인하기 위해서는 인위적인 조작이 필요하다고 생각했다.
# 3. 컬럼들의 경우의 수를 모두 얻은 후에 각 값들의 유일성을 검증하기로 했다.
# 4. itertools의 combinations를 사용해서 col의 모든 조합을 만든다.
# 5. 반복문으로 col의 조합을 가져와서 합친 쳐서 하나의 tempCol을 만들고 set에 넣어서 개수를 확인한다.
#   ex) 1,2 조합이라면 set(["100ryan","200apeach","300tube","400con","500muzi","600apeach"])
# 6. 개수가 원래 row의 수와 동일하면 유일성이 보장된 것이기 때문에 따로 저장해둔다.
 

# 최소성 : 
# 1. 유일함이 보장된 조합에서 최소성을 검증한다.
# 2. 리스트 내에서 부분집합을 갖고 있다면 최소성 조건에 맞지 않기 때문에 삭제 대상 set에 넣는다.
# 3. 유일성이 보장된 그룹의 수에서 삭제 대상의 수를 뺀다.

# from itertools import combinations

# relation = [["100", "ryan"  ,"music"   ,"2"],
#             ["200", "apeach","math"    ,"2"],
#             ["300", "tube"  ,"computer","3"],
#             ["400", "con"   ,"computer","4"],
#             ["500", "muzi"  ,"music"   ,"3"],
#             ["600", "apeach","music"   ,"2"]]

# def solution(relation):
#     answer = 0
    
#     # [list] all of colume combinations
#     all = list()
    
#     # [list] unique combinations
#     uniqueIndex = []
    
#     if len(relation) > 0:
#         colSize = len(relation[0])  # number of columes
#         rowSize = len(relation)     # number of rows
    
#     # [set] all combinations of colums in set()
#     for i in range(1, colSize +1):
#         all.extend([set(k) for k in combinations([j for j in range(colSize)], i)])
#         # using extend b.c. append causes run time error
#     print(all)
    
    
#     # check unique of valid sets
#     for comb in all:
#         vaildSet = set()
        
#         # combine all the rows in the comb, and make a string
#         for row in range(rowSize):
#             temp = ''
#             for col in comb:
#                 temp += relation[row][col-1]
#             vaildSet.add(temp)
        
#         if len(vaildSet) == rowSize:
#             uniqueIndex.append(comb)
    
#     # check minimalized
#     # will be deleted
#     delSet = set()
#     # check subsets
#     for stdMinElem in uniqueIndex:
#         for index, compMinElem in enumerate(uniqueIndex):
#             # if it's not itself, but the subset of smthing else, remove
#             if stdMinElem.issubset(compMinElem) and stdMinElem != compMinElem:
#                 delSet.add(uniqueIndex.index(compMinElem))
                
#         # unique - non-minized's
#         answer = len(uniqueIndex) - len(delSet)    
        
#     return answer


# ## Print answer
# print(solution(relation))
