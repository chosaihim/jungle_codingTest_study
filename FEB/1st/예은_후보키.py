from itertools import combinations

def solution(relation):
    answer = 0
    num = [i for i in range(len(relation[0]))]

    # 하나만으로 식별되는거 제끼고 두개부터 시작
    # 조합으로 다 구하고, 길이 같으면 후보키 ㅇ
    # append 는 그 자체를 더하고, extend는 Iterable의 내용물을 더한다
    combi_list = []
    for i in range(1, len(num) + 1):
        combi_list.extend(combinations(num, i))

    # 조합으로 구해서 싹 다 넣는다
    # 유일성만
    result_list = []
    for one in combi_list:
        tuple_list = [tuple(item[i] for i in one) for item in relation]
        if len(set(tuple_list)) == len(relation):
            answer += 1
            result_list.append(one)

    # 최소성 : 교집합 있으면 빼준다
    # discard 는 지우려는 애 없어도 에러 안발생한다
    check = set(result_list)
    for i in range(len(result_list)):
        for j in range(i + 1, len(result_list)):
            if (set(result_list[i]).issubset(set(result_list[j])) or set(result_list[j]).issubset(set(result_list[i]))):
                answer -= 1
                check.discard(result_list[j])
    answer = len(check)
    return answer


relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

print(solution(relation))

