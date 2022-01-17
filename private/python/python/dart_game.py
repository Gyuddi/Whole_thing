def solution(dartResult):
    answer = 0
    dartResult = dartResult.replace("10","K")
    n = []
    for i in range(len(dartResult)):
        if dartResult[i] == "K":
            n.append(10)
        elif dartResult[i].isdigit() == True:
            n.append(int(dartResult[i]))
        elif dartResult[i] == "S":
            continue
        elif dartResult[i] == "D":
            n.append(n[-1] ** 2)
            n.remove(n[-2])
        elif dartResult[i] == "T":
            n.append(n[-1] ** 3)
            n.remove(n[-2])
        elif dartResult[i] == '*':
            if len(n) > 1:
                n[-2] *= 2
            n[-1] *= 2
        elif dartResult[i] == "#":
            n[-1] = -n[-1]

    return sum(n)

dartResult = "1S2D*3T*"
print(solution(dartResult))