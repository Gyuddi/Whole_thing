# def binsearch(n,S,x):
#     low = 1
#     high = n
#     location = 0
#     while low <= high and location ==0:
#         mid = (low+high) // 2
#         if x == S[mid]:
#             location = mid
#         elif x < S[mid]:
#             high = mid -1
#         else:
#             low = mid+1
#     return location

def location(S,low,high):
    if low > high:
        return 0
    else:
        mid = (low+high)//2
        if x ==S[mid]:
            return mid
        elif x > S[mid]:
            return location(S,mid+1,high)
        else:
            return location(S,low,mid-1)
S = [-1,1,2,3,4,5,6,7]
n = len(S) - 1
x = 5
print(location(S,1,len(S)))