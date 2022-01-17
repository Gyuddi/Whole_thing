def solution(s):
    s = list(s)
    answer = []
    answer_list = []
    if len(s) == 1:
        return 1
    for i in range(1,len(s)//2+1):
            count = []
            num = 1
            for j in range(0,len(s),i):
                if s[j:j+i] == s[j+i:j+i+i]:
                    num += 1
                    
                    # count.append("".join(s[j:j+i]))
                else:
                    if num == 1:
                        count.append("".join(s[j:j+i]))
                        continue
                    count.append(num)
                    num = 1
                    count.append("".join(s[j:j+i]))
            answer.append(count)

    for i in range(len(answer)):
        summ = 0
        for j in range(len(answer[i])):
            summ += len(str(answer[i][j]))
        answer_list.append(summ)

    return min(answer_list)
s="ababcdcdababcdcd"
print(solution(s))