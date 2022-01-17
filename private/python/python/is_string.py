def solution(s):
    answer = False
    if len(str(s)) == 4 or len(str(s)) == 6:
        if s.isdigit() == True:
            answer = True

    return answer

s= "a234"
print(s.isdigit())
print(solution(s))