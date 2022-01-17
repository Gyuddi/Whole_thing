def solution(n):
    sum = 0
    n = list(str(n))
    for i in n:
        i = int(i)
        sum += i
    return sum
n = 123
print(solution(n))