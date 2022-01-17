def solution(s):
    count1 = 0
    count2 = 0
    answer = True
    s = s.lower()
    for i in range(len(s)):
        if s[i] == 'p':
            count1 +=1
        elif s[i] == 'y':
            count2 +=1
    if count1 != count2:
        answer = False

    return answer

s = "pPy"
print(solution(s))