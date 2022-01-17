def Prime_num(n):
    answer = 0
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2,m+1):
        if sieve[i] == True:
            for j in range(i+i,n+1,i):
                sieve[j] = False
    print(sieve)
                    
    for k in range(n,1,-1):
        if sieve[k] == True:
            return k
print(Prime_num(100))