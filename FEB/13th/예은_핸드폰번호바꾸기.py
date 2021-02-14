def solution(phone_number):
    answer = ''
    phone_number = list(phone_number)
    a = ['*' for _ in range(len(phone_number)-4)]
    answer = ''.join(a + phone_number[-4:])
    return answer

phone_number = "01033334444"

print(solution(phone_number))