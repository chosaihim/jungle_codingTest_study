def solution(numbers):
#     그리디
#       가장 앞자리가 가장 큰 수부터 나열하면 됨
    ans = []
    for i in range(9,-1,-1):
        for n in numbers:
            cand = list(str(n))[0]
            if i == cand:
                ans.append(''.join(cand))
    return ''.join(ans)
