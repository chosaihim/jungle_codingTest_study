from math import gcd

def solution(n, m):
    answer = []
    a = gcd(n,m)
    b = int(n*m / a)
    answer = [a, b]
    return answer

#test1
n = 3
m =12

# test2
n = 5
m = 12
print(solution(n,m))


############## 모듈 안쓰기 (유클리드 호제법 구현)
# a를
def hoje(n, m):
    a = max(n,m)
    b = min(n,m)
    while b != 0:
        temp = a
        a = b
        b = temp % b
    return a

print(hoje(n,m))
