def make_map(arr1,n):
    arr_bin = []
    for arr in arr1:
        bin=[]
        while True:
            fraction = arr % 2
            bin.append(fraction)
            arr=arr//2
            if arr < 1: break
        if len(bin)<n:
            for i in range(n-len(bin)):
                bin.append(0)
        bin.reverse()
        arr_bin.append(bin)
    return(arr_bin)


def solution(n, arr1, arr2):
    answer = []
    map_first = make_map(arr1,n)
    map_second = make_map(arr2,n)
    for i in range(len(map_first)):
        line = ""
        for j in range(len(map_first[i])):
            if map_first[i][j] == 0 and map_second[i][j] == 0:
                line += " "
            else:
                line += "#"
        answer.append(line)
    return answer

arr1 = 	[9, 20, 28, 18, 11]
arr2 =  [30, 1, 21, 17, 28]
n = 5
print(solution(n, arr1, arr2))