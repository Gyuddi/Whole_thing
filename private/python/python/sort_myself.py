def solution(strings, n):
    answer = []
    for i in strings:
        i = i[n]+i
        answer.append(i)
    answer.sort()
    for j in range(len(answer)):
        answer[j] = answer[j][1:]
    return answer

strings = ["sun", "bed", "car"]
n = 1
print(solution(strings,n))