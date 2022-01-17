# def fibo2(n):
#     f = [0] * (n+1)
#     if (n>0):
#         f[1] = 1
#         for i in range(2,n+1):
#             f[i] = f[i-1]+f[i-2]
#     return f[n]
# for i in range(30):
#     print(fibo2(i))

# def fibo1(n):
#     if n < 2:
#         return n
#     else:
#         return fibo1(n-1) + fibo1(n-2)
# for i in range(30):
#     print(fibo1(i))  

def fibo3(n):
    if n < 2:
        return n
    else:
        fibo = 0
        fibo_b = 1
        fibo_bb = 0
        for i in range(2,n+1):
            fibo = fibo_b + fibo_bb
            fibo_bb = fibo_b
            fibo_b = fibo
            
    return fibo

for i in range(16):
    print(fibo3(i))  