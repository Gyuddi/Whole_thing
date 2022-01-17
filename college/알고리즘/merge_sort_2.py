# def merge(U,V):
#     S = []
#     i = j = 0
#     while i < len(U) and j < len(V):
#         if U[i] < V[j]:
#             S.append(U[i])
#             i += 1
#         else:
#             S.append(V[j])
#             j += 1
#     if i < len(U):
#         S += U[i:]
#     else:
#         S += V[j:]
#     return S

# def mergesort(S):
#     n = len(S)
#     if n <= 1:
#         return S
#     else:
#         mid = n//2
#         U = mergesort(S[0:mid])
#         V = mergesort(S[mid:n])
#         print(U)
#         print(V)
#         return merge(U,V)
# S = [27,10,12,20,25,13,15,22]
# print(mergesort(S))





def merge(U,V):
    S = []
    i = j = 0
    while i < len(U) and j < len(V):
        if U[i] < V[j]:
            S.append(U[i])
            i += 1
        else:
            S.append(V[j])
            j+=1
    if i < len(U):
        S += U[i:]
    else:
        S += V[j:]
    return S


def mergesort(S):
    n = len(S)
    if n <= 1:
        return S
    else:
        mid = n // 2
        U = mergesort(S[0:mid])
        V = mergesort(S[mid:n])
        print(U,V)
        return merge(U,V)

S = [27,10,12,20,25,13,15,22]
print(mergesort(S))