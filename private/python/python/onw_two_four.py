def solution(n):
    answer = ''
    for i in range(len(str(n))*2,0,-1):
        three_num.append(real_n // (3**i))
        real_n = real_n % (3**i)
        if i == 1:
            three_num.append(real_n % (3**i))
    return answer
