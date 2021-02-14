def check_id(a,b):
    if len(a) != len(b):
        return False
    for i in range(len(a)):
        if b[i] == '*':
            continue
        if b[i] != a[i]:
            return False
    return True

def solution(user_id, banned_id):
    def dfs(i):
        if i == len(banned_id):
            check.add(tuple(sorted(tmp_check)))
            return
        for id in banned_dict[banned_id[i]]:
            if id not in tmp_check:
                tmp_check.add(id)   
                dfs(i+1)      
                tmp_check.remove(id)
            
    answer = 0
    banned_dict = {}
    for id in banned_id:
        banned_dict[id] = []
    for banned in set(banned_id):
        for user in user_id:
            if check_id(user,banned):
                banned_dict[banned].append(user)
    tmp_check = set()
    check = set()
    dfs(0)
    
    return len(check)
