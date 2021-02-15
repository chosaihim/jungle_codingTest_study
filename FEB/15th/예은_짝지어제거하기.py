def solution(s):
    answer = 0
    stack = []
    for one in s:
        if len(stack) == 0:
            stack.append(one)
        elif stack[-1] == one:
            stack.pop()
        else:
            stack.append(one)
    answer = 1 if len(stack) == 0 else 0
    return answer

s = "baabaa"
# s = "cdcd"
# s = "aaaaaaaaaaaaaaaaaaaaabbaaaaaaaaabbbbbbaaaaaaabbaaaaaaaaabbbb"

print(solution(s))

