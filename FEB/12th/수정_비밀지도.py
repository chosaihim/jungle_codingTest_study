a = [9, 20, 28, 18, 11]
b = [30, 1, 21, 17, 28]
n = 5

def make(arr,n):
    for i in range(n):
        tmp = list(str(bin(arr[i])))
        tmp.pop(0)
        tmp.pop(0)
        d = len(tmp)
        for _ in range(n - d):
            tmp.insert(0,'0')
        arr[i] = tmp
    return arr


def solution(n, arr1, arr2):
    arr1 = make(arr1, n)
    arr2 = make(arr2, n)
    print(arr1)
    print(arr2)
    answer = []
    for i in range(n):
        tmp = []
        for j in range(n):
            if arr1[i][j] == '1' or arr2[i][j] == '1':
                tmp.append('#')
            else:
                tmp.append(' ')
        print(tmp)
        answer.append(''.join(tmp))
    print(answer)
    return answer

solution(n,a,b)