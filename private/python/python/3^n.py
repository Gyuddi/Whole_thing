def solution(n):
    answer = 0
    three_num = []
    real_n = n
    for i in range(len(str(n))*2,0,-1):
        three_num.append(real_n // (3**i))
        real_n = real_n % (3**i)
        if i == 1:
            three_num.append(real_n % (3**i))
    three_num = "".join(map(str,three_num))
    three_num = three_num.lstrip("0")
    three_num = three_num[::-1]
    print(three_num)
    three_num = list(map(int, three_num))
    three_num = three_num[::-1]
    print(three_num)
    for i in range(len(three_num)):
        answer += three_num[i] * (3**i)

    return answer

n = 45
solution(n)