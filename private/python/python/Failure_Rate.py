def solution(N, stages):
    answer = []
    percentage ={}
    count_sum = 0

    for i in range(1, N + 1):
        if len(stages) == 0:
            percentage[i] = 0
            continue
        count_sum += stages.count(i)
        if (len(stages) - count_sum + stages.count(i)) == 0:
            percentage[i] = 0
            continue
        percentage[i] = stages.count(i)/ (len(stages) - count_sum + stages.count(i))
    return sorted(percentage, key=lambda x: percentage[x], reverse=True)

N = 5
stages = [2,1,2,4,2,4,3,3]
print(solution(N,stages))