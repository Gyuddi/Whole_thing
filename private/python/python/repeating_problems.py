def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    intRet = fibo(n-1) + fibo(n-2)
    return intRet

for i in range(1,10):
    print(fibo(i))