def insert_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j] = key
    return arr

a = [2,1,5,6,4,5,1,0,2]
print(insert_sort(a))