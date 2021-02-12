def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        tmp = arr1[i]|arr2[i]
        string = []
        for j in range(n-1,-1,-1):
            if (1<<j)|tmp == tmp:
                string.append('#')
            else:
                string.append(' ')
        answer.append(''.join(string))

    return answer
