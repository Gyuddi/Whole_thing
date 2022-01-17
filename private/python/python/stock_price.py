def solution(prices):
    answer = []

    for i in range(len(prices)):
        count = 0
        for j in range(i,len(prices)):
            if prices[i] <= prices[j]:
                count +=1
            else:
                count +=1
                break
        answer.append(count)
    answer[0] = answer[0]-1
    answer.pop(-1)
    answer.append(0)
    return answer

prices = [1, 2, 3, 2, 3,1]
print(solution(prices))