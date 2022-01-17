# def partition(S,low,high):
#     pivotitem = S[low]
#     i = low+1
#     j = high 
#     while i<=j:
#         while S[i] < pivotitem:
#             i += 1
#         while S[j] > pivotitem:
#             j -= 1
#         if i < j:
#             S[i],S[j] = S[j],S[i] 
#     pivotpoint = j
#     S[low] , S[pivotpoint] = S[pivotpoint],S[low]
#     return pivotpoint 

# def quicksort(S,low,high):
#     if high >low:
#         pivotpoint = partition(S,low,high)
#         quicksort(S,low,pivotpoint-1)
#         quicksort(S,pivotpoint+1,high)
#     return S
# S = [6,5,1,4,7,2,3,8]
# print(quicksort(S,0,len(S)-1))

def partition(S,low,high):
    _tem = S[low]
    i = low + 1
    j = high
    while i <= j:
        while S[i] < _tem:
            i += 1
        while S[j] > _tem:
            j -= 1
        if i < j:
            S[i],S[j] = S[j],S[i]
    pivotpoint = j
    S[low] , S[pivotpoint] = S[pivotpoint],S[low]
    return pivotpoint 

def quicksort(S,low,high):
    if high > low:
        pivotpoint = partition(S,low,high)
        quicksort(S,low,pivotpoint-1)
        quicksort(S,pivotpoint+1,high)
    return S

S = [6,5,1,4,7,2,3,8]
print(quicksort(S,0,len(S)-1))