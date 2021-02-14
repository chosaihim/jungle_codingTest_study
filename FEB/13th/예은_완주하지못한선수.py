from collections import defaultdict

def solution(participant, completion):
    answer = ''
    participant_dict = defaultdict(int)

    for one in participant:
        participant_dict[one] += 1
    for one in completion:
        participant_dict[one] -= 1
    answer = [key for key, value in participant_dict.items() if value == 1]
    return answer[0]


participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))