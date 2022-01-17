import math
def solution(progresses, speeds):
    answer = []
    real_answer = []
    time = 1
    for i in range(len(progresses)):
        count = 0
        count = math.ceil((100-progresses[i])/speeds[i])
        answer.append(count)
    print(answer)
    maxi = answer[0]
    for i in range(1,len(answer)):
        if answer[i] <= maxi:
            time += 1
        if answer[i] > maxi:
            maxi = answer[i]
            real_answer.append(time)
            time = 1
        if i == len(answer)-1:
            real_answer.append(time)

    return real_answer

progresses = [93, 30, 55]
speeds = 	[1, 30, 5]
print(solution(progresses, speeds))