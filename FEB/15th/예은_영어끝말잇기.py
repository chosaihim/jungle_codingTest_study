import math

def solution(n, words):
    answer = []
    temp = []
    rule1, rule2 = 101, 101
    for i in range(len(words)):
        if words[i] not in temp:
            temp.append(words[i])
        else:
            rule1 = i
            break
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            rule2 = i
            break
    idx = min(rule1, rule2)
    if idx == 101: return [0,0]

    answer = [(idx + 1) % n if (idx + 1) % n else n, math.ceil((idx + 1) / n)]
    return answer


n = 3
words = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "tank", "tank"]

n = 5
words = ["hello", "observe", "effect", "take", "either",
         "recognize", "encourage", "ensure", "establish", "hang",
         "gather", "refer", "reference", "estimate", "executive"]

n = 2
words = ["hello", "one", "even", "never", "now", "world", "draw"]

print(solution(n, words))
