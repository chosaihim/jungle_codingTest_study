
def solution(dartResult):
    answer = 0
    score = []
    dartResult = list(dartResult)
    for i in range(len(dartResult)):
        if 48 <= ord(dartResult[i]) <= 57:
            if i != len(dartResult) - 1 and dartResult[i] == '1' and dartResult[i + 1] == '0':
                dartResult[i] = 10
            else:
                dartResult[i] = int(dartResult[i])

    # 10 처리해주기
    # 0이면서 전 원소 10인 애들 빼주기
    # pop하면 인덱스 다 변하니까 제로인덱스도 줄여주기
    zero_index = list(filter(lambda x: dartResult[x] == 0, range(len(dartResult))))
    for i in range(len(zero_index)):
        if zero_index[i] > 0 and dartResult[zero_index[i] - 1] == 10:
            dartResult.pop(zero_index[i])
            zero_index = [one - 1 for one in zero_index]


    for one in dartResult:
        if type(one) == int:
            score.append(one)
        elif one == 'D':
            score[-1] = score[-1]**2
        elif one == 'T':
            score[-1] = score[-1]**3
        elif one == '*':
            if len(score) == 1:
                score[0] *= 2
            else:
                score[-1] *= 2
                score[-2] *= 2
        elif one == '#':
            score[-1] *= -1

    answer = sum(score)
    return answer


dartResult = "1S2D*3T"
dartResult = "1D2S#10S"
dartResult = "1D2S0T"
dartResult = "1S*2T*3S"
dartResult = "1D2S3T*"
dartResult = "10S10S10S"

print(solution(dartResult))