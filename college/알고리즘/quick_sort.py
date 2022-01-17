def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []
        for i in arr[1:]:
            if i <= pivot:
                less.append(i)
            else:
                greater.append(i)
    return quick_sort(less) + [pivot] + quick_sort(greater)
print(quick_sort([2,5,4,9,7]))