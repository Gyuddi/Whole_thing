def find_s_index(arr):
    smallest = arr[0]
    s_index = 0
    for i in range(1,len(arr)):
        if arr[i]<smallest:
            smallest = arr[i]
            s_index = i
    return s_index
def selection_sort(arr):
    new_arr=[]
    for i in range(len(arr)):
        idx = find_s_index(arr)
        new_arr.append(arr.pop(idx))
    return new_arr

a = [5,9,6,8,7,7,8,9,4,1,2,6,5]
print(selection_sort(a))
