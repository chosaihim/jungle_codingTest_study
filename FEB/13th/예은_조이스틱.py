def solution(name):
    answer = 0
    numbers = [min(ord(one) - ord('A'), ord('Z') - ord(one) + 1) for one in name]
    idx = 0
    while 1:
        answer += numbers[idx]
        numbers[idx] = 0
        if sum(numbers) == 0:
            break
        left, right = 1, 1
        while numbers[idx - left] == 0:
            left += 1
        while numbers[idx + right] == 0:
            right += 1
        answer += left if left < right else right
        idx += -left if left < right else right
    # print(numbers)
    return answer


# ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 아스키코드 65~90

# min(65와의 차이, 90과의 차이 + 1)
# 알파벳 바꾸는 횟수 저장 배열
# 더해주고 0으로 바꾼다 -> 이 배열의 합이 0이 될때까지 반복한다
# 왼쪽으로 갈지, 오른쪽으로 갈지는 이동횟수가 더 적은 쪽으로 이동한다
# 알파벳 안바꿔도 되는 애들이면 넘어간다 (바꿔야하는 애 만날때까지 이동횟수 더해준다)
# 양쪽에 대해서 위 과정을 진행하고, 더 횟수가 적은 쪽으로 결정한다


name = "JEROEN"
# name = "JAN"
# name = "JAZ"
# name = "ZZZ"
# name = "AZAZ"
# name = "ZAAAAAAAAZ"
# name = "ZZAAAZ" # 답 6     반례 ( 다시 돌아가야하는 경우) -> 재귀 ?
name = "AAAAA"
# name = "ZAAAZZ"
name = 'BBBAAB'
print(solution(name))