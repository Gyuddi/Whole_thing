def solution(number, k):
    answer = []
    number = list(number)
    for i in range(len(number)-1):
        print(i)
        for j in range(i+1,len(number)):
            a = number[i]
            b = number[j]
            number.pop(i)
            number.pop(j)
            answer.append("".join(number))
            number.insert(i,a)
            number.insert(j,b)
            

    return answer

number = "1924"
k = 2
print(solution(number,k))
