def lsd_sort(a):
    width = 3
    n = len(a)
    r = 128
    temp = [None] * n
    for d in reversed(range(width)):
        count = [0] * (r+1)
        for i in range(n):
            count[ord(a[i][d])+1] += 1
        print(count)
        for j in range(1,r):
            count[j] += count[j-1]
        print(count)
        for i in range(n):
            p = ord(a[i][d])
            temp[count[p]] = a[i]
            print(temp)
            count[p] += 1
            print(count)
        for i in range(n):
            a[i] = temp[i]
        print(d,"번째 문자: ",end="")
        for x in a:
            print(x,end=" ")
        print()
a = ["ICN","ADW","FSF","GRE","BVN"]
lsd_sort(a)