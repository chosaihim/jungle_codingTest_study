def solution(phone_number):
    phone_length = len(phone_number)
    answer = ['*' for _ in range(phone_length - 4)]
    answer.extend(phone_number[-4:])
    return ''.join(answer) # join
