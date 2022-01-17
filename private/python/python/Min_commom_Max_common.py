def solution(n, m):
    answer = []
    bigger  = max([m,n])
    for i in range(bigger+1,0,-1):
        if m % i == 0 and n % i == 0:
            answer.append(i)
            print(answer)
            break
    maxi = (n*m) / answer[0] 
    answer.append(maxi)
    return answer

n = 2
m = 5
print(solution(n,m))