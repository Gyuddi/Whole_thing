import random

N=10
listnum = list(range(N))
random.shuffle(listnum)

print(listnum)

def sort_num(listnum):
    for i in range(N):
        for j in range(i+1,N):
            if listnum[i] > listnum[j]:
                listnum[i],listnum[j] = listnum[j],listnum[i]
    print(listnum)

sort_num(listnum)
