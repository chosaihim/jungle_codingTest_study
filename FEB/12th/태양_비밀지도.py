n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

def solution(n, arr1, arr2):
    arr_result = [0] * n 
    def parse_to_binary(n, value) :
        sharp = ""
        for _ in range(n) :
            if value & pow(2,_) :
                sharp = "#" + sharp
                value -= pow(2,_)
            else :
                sharp = " " + sharp
        return sharp

    answer = []
    for i in range(n) :
        arr_result[i] = arr1[i] | arr2[i]
        answer.append(parse_to_binary(n, arr_result[i]))
    
    return answer

print(solution(n,arr1,arr2))
