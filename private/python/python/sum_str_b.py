import math
def solution(s):
    s = list(s)
    answer = 0
    count_list =[]
    answer_list = []
    for i in range(1,(math.ceil(len(s)/2))+1):
        count = []
        for j in range(0,len(s),i):
            if s[j:j+i] == s[j+i:j+i+i]:
                count.append(1)
                count.append("".join(s[j:j+i]))
            else:
                count.append("".join(s[j:j+i]))
            print(count)
    #     for i in range(len(count)-1):
    #         if count[i] == count[i+1]:
    #             del count[i]
    #     if len(count) != 0:
    #         count_list.append(count)
    # print(count_list)
    # for i in range(len(count_list)):
    #     summ = 0
    #     for j in range(len(count_list[i])):
    #         summ += len(count_list[i][j])
    #     summ += len(count_list[i])
    #     answer_list.append(summ)
    # if len(answer_list) == 0:
    #     return len(s)


    # return min(answer_list)
s="abcabcdede"
print(solution(s))