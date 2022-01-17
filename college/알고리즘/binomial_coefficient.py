# def bin (n,k):
#     if k == 0 or n == k:
#         return 1 
#     else:
#         return bin(n-1,k-1) + bin(n-1,k)
# print(bin(5,2)) 함수 중복호출 문제 발생

# def bin2(n,k):
#     B = [[0] * (k+1) for a in range(n+1)]
#     for i in range(n+1):
#         for j in range(min(i,k)+1):
#             if j == 0 or  j == i:
#                 B[i][j] = 1
#             else: 
#                 B[i][j] = B[i-1][j-1] + B[i-1][j]
#     return B[n][k]



def bin3(n,k):
    if k > n//2:
        k = n-k
    B = [0] * (k+1)
    B[0] =1
    for i in range(1,n+1):
        j = min(i,k)
        while j > 0:
            B[j] = B[j] + B[j-1]
            j -=1
    return B[k]

for i in range(11):
    for j in range(i+1):
        print(bin3(i,j),end=" ")
    print()