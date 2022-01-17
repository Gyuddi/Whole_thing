N = int(input())
time_table = []

for i in range(N):
    a, b = map(int,input().split())
    time_table.append([a,b])

for i in range(len(time_table)-1):
    for j in range(i,len(time_table)):
        if time_table[i][1] > time_table[j][1]:
            time_table[i],time_table[j] = time_table[j],time_table[i]
        if time_table[i][1] == time_table[j][1]:
            if time_table[i][0] > time_table[j][0]:
                time_table[i],time_table[j] = time_table[j],time_table[i]
answer = [time_table[0]]
for i in range(1,len(time_table)):
    if time_table[i][0] >= answer[-1][1]:
        answer.append(time_table[i])

print(len(answer))