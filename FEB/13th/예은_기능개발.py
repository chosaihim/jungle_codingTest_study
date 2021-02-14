def solution(progresses, speeds):
    answer = []
    days= []
    for i in range(len(progresses)):
        one = progresses[i]
        count = 0
        while (one < 100):
            one += speeds[i]
            count += 1
        days.append(count)

    temp = 1
    prev = days[0]
    for i in range(1, len(days)):
        if prev >= days[i]:
            temp += 1

        else:
            answer.append(temp)
            temp = 1
            prev = days[i]
    answer.append(temp)
    return answer


progress = [93, 30, 55]
speeds = [1, 30, 5]

progress = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

print(solution(progress, speeds))