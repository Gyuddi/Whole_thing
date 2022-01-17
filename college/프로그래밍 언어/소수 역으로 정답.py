def reverse(x):
    x=str(x)
    for i in range(len(x)-1):
        if x[i] == "0":
            x = x[:i]
    x=x[::-1]
    x=int(x)
    return x

def isPrime(x):
    count = 0
    for i in range(2,x):
        if x % i == 0:
            count+=1
    if count == 0:
        return x


def q7():
    x=int(input())
    m = list(map(int, input().split()))
    answer = []
    for num in m:
        num = reverse(num)
        if type(isPrime(num)) == int:
            answer.append(isPrime(num))
    return answer


print(q7())