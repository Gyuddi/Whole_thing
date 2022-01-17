def solution(n):
    answer = []
    real_answer = []
    res = [[None] * n for i in range(1,n+1)]
    total_count = 1
    return_count = 0
    a = 0
    def triangle(a,n,total_count):
        
        for i in range(a,n):
            if res[i][a] != 0:
                break
            res[i][a] = total_count
            total_count += 1
        for j in range(a,n-2):
            if res[n-1][j+1] != 0:
                break
            res[n-1][j+1] = total_count
            total_count += 1
        for k in range(n-1,a,-1):
            if res[k][k] != 0:
                break
            res[k][k] = total_count
            total_count += 1


        return res

    for i in range(n//2):
        x=triangle(a,n,total_count)
        answer.append(x)
        total_count = res[1][1] + 1
        res = [[0] * n for i in range(1,n+1)]
        n = n-3

    # for i in range(len(answer)):
    #     for j in range(len(answer[i])):
    #         for k in range(len(answer[i][j])):
    #             if answer[i][j][k] != 0:
    #                 real_answer.append(answer[i][j][k])
    


    
    return answer


        
    


    
    
n = 10
print(solution(n))