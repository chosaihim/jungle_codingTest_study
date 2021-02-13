# https://programmers.co.kr/learn/courses/30/lessons/42839

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n//2+1):
        if n % i == 0:
            return False
    else:
        return True

def solution(numbers):
    numbers = list(numbers)
    cnt = 0
    next = []
    prev = []
    results = []

    def dfs(curr, i):  # k: 몇 개를 뽑아서 순열을 만들까
        if len(curr) == len(numbers) - i:
            results.append(prev[:])
        for n in curr:
            next = curr[:]
            next.remove(n)

            prev.append(n)
            dfs(next, i)
            prev.pop()

    for i in range(len(numbers)+1):
        dfs(numbers, i)

    ans=[]
    for r in results:
        if len(r) != 0:
            r = ''.join(r)
            ans.append(int(r))
    ans = list(set(ans))
    for a in ans:
        print(a)
        if isPrime(a):
            cnt += 1

    return cnt

print(solution(numbers))