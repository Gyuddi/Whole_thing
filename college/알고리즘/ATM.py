n=int(input())
times=list(map(int,input().split()))
summ = 0
times = sorted(times)
answer = []
for time in times:
    summ += time
    answer.append(summ)
print(sum(answer))

