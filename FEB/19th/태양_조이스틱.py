names = ["JEROEN", "JAN", "CANAAAAANAN","AAAZAAZA"]

def solution(name):
    answer = 0
    target = ''.join('A' for _ in range(len(name)))
    alpha = [chr(_) for _ in range(65,91)]
    #? 조이스틱을 움직이는 방법은 4가지가 있다. [좌,우] [상,하] 어떤 방법이 더 적은 횟수로 도달 가능한지.
    #? 포인터 위치는 첫번째에서 시작한다.
    #? 'AAAA..'에서 시작한다.
    #? 위로 움직이거나 아래로 움직일 때, A -> Z , Z -> A 로 이동이 가능하다. 0 -> 26, 26번, 0 -> 26 , 1번
    #? 좌측으로 움직일 때, 첫번째 포인터에서 마지막 포인터로 이동 가능하다. 0 -> last index, last index -> 0
    #? 우측으로 움직일때는? 고려 안해도 되는 문제가 되나? 
    #? 가장 가까운 알파벳, 가장 가까운 바꿀 위치 찾기
    #? 그리고 카운팅
    #? 인덱스의 양옆을 하나더 추가하는건 어떨까.
    def verti(src, dest) :
        v1, v2 = ord(src), ord(dest)
        cnt = abs(v1 - v2)
        if cnt > 13 :
            cnt = 26 - cnt
        res = alpha[ord(src) + cnt]
        return (cnt, res)

    def horiz(srclist, destlist, ptr) :
        length = len(srclist)
        for i in range(length) :
            if srclist[i] != destlist[i] :
                return (i, abs(i - ptr))
            if srclist[-i] != destlist[-i]:
                return (length - i, abs(length - i + ptr))

    ptr = 0 # 시작 포인터는 0으로 한다.
    while name != target : # 문자가 같을 때까지 특정 알고리즘을 반복한다.
        if name[ptr] != target[ptr] : # 문자 자체가 다르므로 
            verti(name[ptr], target[ptr]) # 상하 알고리즘 적용한다. return (count, res)를 이용한다. 문자를 바꿔준다.
        else :
            return # 좌우 알고리즘을 적용한다. return (ptr, count)를 적용한다.

    return answer

print(solution(names[1]))
