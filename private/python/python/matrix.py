def solution(arr1, arr2):
    answer = []
    for i in range(len(arr1)):
        new = []
        for j in range(len(arr1[0])):
            new.append(arr1[i][j]+arr2[i][j])
        answer.append(new)
    return answer
arr1 = [[3],[2]]	
arr2 = [[3],[5]]
print(solution(arr1,arr2))