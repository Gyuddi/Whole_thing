def solution(n):
    answer = 0
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    for i in range(2,n+1):
        if sieve[i] == True:
            print(i)
            answer += 1



    return answer

n =100
print(solution(n))