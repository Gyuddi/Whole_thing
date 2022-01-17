def solution(n):
    answer = ""
    n = list(str(n))
    for i in sorted(n,reverse=True):
        answer += i
    return int(answer)

n = 123456789
print(solution(n))