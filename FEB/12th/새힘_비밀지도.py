n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
#output = ["#####","# # #", "### #", "# ##", "#####"]

def solution(n, arr1, arr2):
    answer = []

    map_bin = [0]*n;    
    for i in range(n):
        map_bin[i] = arr1[i] | arr2[i]
    
    for i in range(n):
        row = ''     
        for j in range(n-1,-1,-1):
            if map_bin[i] & 1 << j:
                row += "#"
            else:
                row += " "
        answer.append(row)    
    return answer

print(solution(n,arr1,arr2))