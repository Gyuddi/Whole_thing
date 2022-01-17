n = int(input())
count = 0

if n%5 ==0:
    count = n // 5
elif n%5 == 1:
    if n == 1:
        count = -1
    # elif 
    else:
        count = (n//5-1) + 2
elif n%5 == 2:
    if n == 2 or n == 7:
        count = -1
    else:
        count = (n//5-2) + 4
elif n%5 == 3:
    count = n//5 + 1
elif n%5 == 4:
    if n ==4 :
        count = -1
    else:
        count = (n//5-1) + 3
print(count)