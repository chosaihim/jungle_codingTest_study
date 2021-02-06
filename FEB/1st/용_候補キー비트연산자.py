# relation = [["ab", "c"], ["a", "bc"], ["x", "yz"], ["x", "c"]] 
relation = [["100","ryan","music","2"],["200","apeach","math","2"],["300","tube","computer","3"],["400","con","computer","4"],["500","muzi","music","3"],["600","apeach","music","2"]]
# relation = [["a","b","c"], ["1","b","c"], ["a","b","4"], ["a","5","c"]]
# relation = [["a","1","4"],["2","1","5"],["a","2","4"]]
# relation = [["a","aa"],["aa","a"],["a","a"]]
# relation = [["a","b","c"],["가","나","다"],["A","B","C"]]
# relation = [["0","0","0"],["0","0","0"],["0","2","1"]]


# 78.6점 
def solution(relation):
    # 검사할 attri의 갯수
    len_x = len(relation)
    # attri의 length
    len_y = len(relation[0])
    # 중복 체크용
    cand_key = {}

    # attribute 기준으로 리스트 구성
    attri = [[] for _ in range(len_y)]
    for j in range(len_y):
        for i in range(len_x):
            attri[j].append(relation[i][j])

    cnt = 0


    def find(cur_num, attri_idx, len_x, len_y, cand_key):
        uniq = 0
        chk_dic = {}
        # uniq 검사
        for i in attri_idx:
            chk_dic.clear()

            # uniq가 아닌 idx 조사
            for j in range(len_x):
                if (uniq & (1<<j)):
                    continue
                chk_dic[j] = attri[i][j]


            if chk_dic:
                # 해당 요소가 uniq인지 조사
                for key_origin, value_origin in chk_dic.items():
                    is_unique = True
                    for key_cmp, value_cmp in chk_dic.items():
                        if key_origin != key_cmp and value_origin == value_cmp:
                            is_unique = False

                    if is_unique:
                        uniq = uniq | (1<<key_origin)

        if uniq == (1<<len_x)-1:
            cand_key[cur_num] = True
            return 1
        
        return 0



    # 1의 갯수
    for q in range(1, len_y+1):
        # 처음부터 끝까지
        for cur_num in range((1<<q-1), (1<<len_y)):
            attri_idx = []
            one_chk = 0
            skip = False

            # cur_num 1 갯수 검사
            for e in range(len_y):
                if cur_num & (1<<e):
                    attri_idx.append(e)
                    one_chk += 1

            # 1의 갯수 검사
            if q != one_chk:
                skip = True

            # 중복 검사
            for key in cand_key.keys():
                if key & cur_num == key:
                    skip = True
                    break
            
            # 중복도 통과하면
            if not skip:
                cnt += find(cur_num, attri_idx, len_x, len_y, cand_key)

    return cnt

print(solution(relation))