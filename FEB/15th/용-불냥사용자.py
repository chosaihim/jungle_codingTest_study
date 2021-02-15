# DFS
# user_id를 분해하여 2차원 배열로 만든다. (id_list)
# banned_id도 분해하여 2차원 배열로 만든다. (ban_list)
# DFS의 인자는 word(ban_list에서 pop)이다. 
# 현재 id_list에서 for문을 돌면서 word와 일치하면 해당 요소를 pop한다.
# 그리고 다음 id_list를 찾는다.
# 귀결 조건 : ban_id가 pop되고, 탐색에 성공했을 때, ban_list가 없다면 종료한다.

# case 1:
user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]

# case 2:
user_id, banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]

import copy
answer = 0
def compare(a_id, ban):
    # id와 ban은 parsing된 단어이다. (한글자씩 들어 있는 리스트)
    if len(ban) != len(a_id):
        return False

    for i in range(len(a_id)):
        if a_id[i] == ban[i] or ban[i] == '*':
            continue
        else:
            return False
    # print('success compare[id:', a_id,'] [ban:', ban, ']')
    return True


def DFS(id_list, ban_list, trash_bin, final):
    global answer

    # 귀결조건
    # trash_bin은 여태까지 담아놓은 a_id가 있다.
    # 이 리스트가 final안에 존재하지 않으면 final에 추가하고 answer에 1 더한다.
    if not ban_list:
        if not final:
            final.append(trash_bin)
            answer += 1
        else:
            for i in final:
                tmp_final = set(i)

                if not tmp_final - trash_bin:
                    return
            tmp_trash = list(trash_bin)
            final.append(trash_bin)
            answer += 1
        return


    cur_ban = ban_list.pop()
    for a_id in id_list:
        if compare(a_id, cur_ban):
            new_id_list = id_list[:]
            new_id_list.remove(a_id)
            trash_word= ''
            new_trash_bin = copy.deepcopy(trash_bin)
            for letter in a_id:
                trash_word += letter
            new_trash_bin.add(trash_word)

            new_ban_list = ban_list[:]
            DFS(new_id_list, new_ban_list, new_trash_bin, final)

    
    
def parsing(idlist):
    rtn_list = []
    for i in idlist:
        tmp = list(i)
        rtn_list.append(tmp)
    return rtn_list
    

def solution(user_id, banned_id):
    final = []
    trash_bin = set()
    id_list = parsing(user_id)
    ban_list = parsing(banned_id)
    DFS(id_list, ban_list, trash_bin, final)
    # print(final)
    return answer

print(solution(user_id, banned_id))