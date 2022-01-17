def solution(answers):
    answer = []
    supo = [[1,2,3,4,5],[2,1, 2, 3, 2, 4, 2, 5],[3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    total_count = [0,0,0]


    for i in range(len(supo)):
        for j in range(len(answers)):
            n = j % len(supo[i]) 
            if answers[j] == supo[i][n]:
                total_count[i] += 1
    
    for idx,score in enumerate(total_count):
        if score ==max(total_count):
            answer.append(idx+1)

    return answer

answers = [1,2,3,4,5]
print(solution(answers))













# 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5