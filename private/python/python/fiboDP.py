def FibonacciDP(n):
    dicFibonacci = {}
    dicFibonacci[0] = 0
    dicFibonacci[1] = 1
    for i in range(2,n+1):
        dicFibonacci[i] = dicFibonacci[i-1] + dicFibonacci[i-2]
    return dicFibonacci[n]

for i in range(0,10):
    print(FibonacciDP(i))