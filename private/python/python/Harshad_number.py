def solution(x):
    answer = True
    x = str(x)
    hashad = 0
    for i in range(len(x)):
        hashad += int(x[i])
    if int(x) % hashad != 0 :
        return False
    return answer

x = 16
print(solution(x))