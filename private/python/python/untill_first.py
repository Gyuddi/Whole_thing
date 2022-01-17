def solution(num):
    answer = 0 
    if num == 1: 
        return 0 
    while True: 
        if num % 2 == 0:
            num = num/2  
        else:
            num = num*3+1 
        answer += 1 
        if num == 1: 
            break
        elif answer == 500: 
            return -1 
    return answer

    
num = 6
print(solution(num))