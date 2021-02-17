import sys
sys.setrecursionlimit(1000000)
def solution(n, m):
    def gcd(a, b) :
        if b == 0 :
            return a
        return gcd(b, a%b)
    answer = [gcd(n,m) , n*m / gcd(n,m)]
    return answer
