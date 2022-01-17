def solution(n):
    divisor = []
    for i in range(n):
        if n % i == 0:
            divisor.append(i)
    return sum(divisor)