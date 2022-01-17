def merge_sort(arr):
    n = len(arr)
    if n <= 1:
        return arr
    mid = n//2
    g1 = merge_sort(arr[:mid])
    g2 = merge_sort(arr[mid:])
    result = []
    while g1 and g2:
        if g1[0] < g2[0]:
            result.append(g1.pop(0))
        else:
            result.append(g2.pop(0))
    while g1:
        result.append(g1.pop(0))
    while g2:
        result.append(g2.pop(0))
    return result

a = [8,4,6,8,9,4,1,2,3]
print(merge_sort(a))
