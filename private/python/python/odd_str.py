def solution(s):
    s = s.split(" ")
    answer = []

    for i in s:
        i = list(i)
        for j in range(len(i)):
            if j % 2 == 0:
                i[j] = i[j].upper()
            else:
                i[j] = i[j].lower()
            print(i)
        i = "".join(i)
        answer.append(i)
    return " ".join(answer)



s="try hello world"
print(solution(s))