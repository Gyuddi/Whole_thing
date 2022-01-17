import math
def find_prime(n):
    answer = 0
    prime_num = []
    for i in range(2,n+1):
        for j in range(2,i):
            if i % j == 0:
                break
        else:
            prime_num.append(i)
            answer += 1
    return prime_num


def solution(n):
    x = int(math.sqrt(n))
    prime_list = find_prime(x)
    all_list = list(range(2,n+1))
    for i in prime_list:
        try:
            for j in range(x):
                all_list.remove(i*j)
        except ValueError:
            pass
    return all_list





n=100
print(solution(n))