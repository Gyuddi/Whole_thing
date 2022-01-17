def shell_sort(a):
    h = 4
    while h>=1:
        for i in range(h,len(a)):
            j = i
            while j>= h and a[j]<a[j-h]:
                a[j],a[j-h] = a[j-h],a[j]
                j-=h
        h //=3
    return a
a = [2,4,6,7,5,1,3,7,9,8,5,1,3,5]
print(shell_sort(a))